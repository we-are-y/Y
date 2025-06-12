-- Enable necessary extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "vector";

-- Users table (extends Supabase auth.users)
CREATE TABLE users (
    id UUID REFERENCES auth.users(id) PRIMARY KEY,
    username TEXT UNIQUE,
    email TEXT UNIQUE,
    full_name TEXT,
    avatar_url TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Schema Registry Table
CREATE TABLE schema_registry (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    type TEXT NOT NULL,
    display_name TEXT NOT NULL,
    version INTEGER NOT NULL DEFAULT 1,
    fields JSONB NOT NULL, -- [{ name, type, unit, ... }]
    category TEXT,
    visibility TEXT DEFAULT 'private', -- private, public, api_visible
    ui_widget_hint TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);
CREATE UNIQUE INDEX idx_schema_registry_type_version ON schema_registry(type, version);

-- Update vault_entries
DROP TABLE IF EXISTS vault_entries CASCADE;
CREATE TABLE vault_entries (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    schema_type TEXT NOT NULL, -- e.g. 'blood_test', 'journal_entry'
    schema_version INTEGER NOT NULL DEFAULT 1,
    data JSONB NOT NULL, -- the actual entry
    metadata JSONB, -- e.g. tags, source, device, etc.
    embedding VECTOR(1536),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    FOREIGN KEY (schema_type, schema_version) REFERENCES schema_registry(type, version)
);
CREATE INDEX idx_vault_entries_user_id ON vault_entries(user_id);
CREATE INDEX idx_vault_entries_schema_type ON vault_entries(schema_type);
CREATE INDEX idx_vault_entries_created_at ON vault_entries(created_at);

-- Echo memories
CREATE TABLE echo_memories (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    content JSONB NOT NULL,
    embedding VECTOR(1536),
    metadata JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Contexts
CREATE TABLE contexts (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    context_type TEXT NOT NULL,
    data JSONB NOT NULL,
    metadata JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Permissions
CREATE TABLE permissions (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    resource TEXT NOT NULL,
    action TEXT NOT NULL,
    metadata JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(user_id, resource, action)
);

-- Consents
CREATE TABLE consents (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    data_type TEXT NOT NULL,
    purpose TEXT NOT NULL,
    expires_at TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(user_id, data_type, purpose)
);

-- Usage logs
CREATE TABLE usage_logs (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    resource TEXT NOT NULL,
    action TEXT NOT NULL,
    metadata JSONB,
    timestamp TIMESTAMPTZ DEFAULT NOW()
);

-- Dividend calculations
CREATE TABLE dividend_calculations (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    data_type TEXT NOT NULL,
    usage_count INTEGER NOT NULL,
    quality_score FLOAT NOT NULL,
    base_rate FLOAT NOT NULL,
    dividend FLOAT NOT NULL,
    calculated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Payouts
CREATE TABLE payouts (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    amount FLOAT NOT NULL,
    payment_method TEXT NOT NULL,
    status TEXT NOT NULL,
    transaction_id TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_vault_entries_user_id ON vault_entries(user_id);
CREATE INDEX idx_vault_entries_data_type ON vault_entries(data_type);
CREATE INDEX idx_vault_entries_created_at ON vault_entries(created_at);

CREATE INDEX idx_echo_memories_user_id ON echo_memories(user_id);
CREATE INDEX idx_echo_memories_created_at ON echo_memories(created_at);

CREATE INDEX idx_contexts_user_id ON contexts(user_id);
CREATE INDEX idx_contexts_context_type ON contexts(context_type);
CREATE INDEX idx_contexts_created_at ON contexts(created_at);

CREATE INDEX idx_permissions_user_id ON permissions(user_id);
CREATE INDEX idx_permissions_resource ON permissions(resource);

CREATE INDEX idx_consents_user_id ON consents(user_id);
CREATE INDEX idx_consents_expires_at ON consents(expires_at);

CREATE INDEX idx_usage_logs_user_id ON usage_logs(user_id);
CREATE INDEX idx_usage_logs_timestamp ON usage_logs(timestamp);

CREATE INDEX idx_dividend_calculations_user_id ON dividend_calculations(user_id);
CREATE INDEX idx_dividend_calculations_calculated_at ON dividend_calculations(calculated_at);

CREATE INDEX idx_payouts_user_id ON payouts(user_id);
CREATE INDEX idx_payouts_status ON payouts(status);
CREATE INDEX idx_payouts_created_at ON payouts(created_at);

-- Vector similarity search function for vault entries
CREATE OR REPLACE FUNCTION match_vault_entries(
    query_embedding VECTOR(1536),
    match_threshold FLOAT,
    match_count INT,
    p_user_id UUID
)
RETURNS TABLE (
    id UUID,
    user_id UUID,
    data_type TEXT,
    content JSONB,
    metadata JSONB,
    similarity FLOAT
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        vault_entries.id,
        vault_entries.user_id,
        vault_entries.data_type,
        vault_entries.content,
        vault_entries.metadata,
        1 - (vault_entries.embedding <=> query_embedding) as similarity
    FROM vault_entries
    WHERE vault_entries.user_id = p_user_id
    AND 1 - (vault_entries.embedding <=> query_embedding) > match_threshold
    ORDER BY vault_entries.embedding <=> query_embedding
    LIMIT match_count;
END;
$$;

-- Vector similarity search function for echo memories
CREATE OR REPLACE FUNCTION match_memories(
    query_embedding VECTOR(1536),
    match_threshold FLOAT,
    match_count INT,
    p_user_id UUID
)
RETURNS TABLE (
    id UUID,
    user_id UUID,
    content JSONB,
    metadata JSONB,
    similarity FLOAT
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        echo_memories.id,
        echo_memories.user_id,
        echo_memories.content,
        echo_memories.metadata,
        1 - (echo_memories.embedding <=> query_embedding) as similarity
    FROM echo_memories
    WHERE echo_memories.user_id = p_user_id
    AND 1 - (echo_memories.embedding <=> query_embedding) > match_threshold
    ORDER BY echo_memories.embedding <=> query_embedding
    LIMIT match_count;
END;
$$;

-- Row Level Security (RLS) Policies
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
ALTER TABLE vault_entries ENABLE ROW LEVEL SECURITY;
ALTER TABLE echo_memories ENABLE ROW LEVEL SECURITY;
ALTER TABLE contexts ENABLE ROW LEVEL SECURITY;
ALTER TABLE permissions ENABLE ROW LEVEL SECURITY;
ALTER TABLE consents ENABLE ROW LEVEL SECURITY;
ALTER TABLE usage_logs ENABLE ROW LEVEL SECURITY;
ALTER TABLE dividend_calculations ENABLE ROW LEVEL SECURITY;
ALTER TABLE payouts ENABLE ROW LEVEL SECURITY;

-- Users policies
CREATE POLICY "Users can view their own data"
    ON users FOR SELECT
    USING (auth.uid() = id);

CREATE POLICY "Users can update their own data"
    ON users FOR UPDATE
    USING (auth.uid() = id);

-- Vault entries policies
CREATE POLICY "Users can view their own vault entries"
    ON vault_entries FOR SELECT
    USING (auth.uid() = user_id);

CREATE POLICY "Users can insert their own vault entries"
    ON vault_entries FOR INSERT
    WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update their own vault entries"
    ON vault_entries FOR UPDATE
    USING (auth.uid() = user_id);

CREATE POLICY "Users can delete their own vault entries"
    ON vault_entries FOR DELETE
    USING (auth.uid() = user_id);

-- Echo memories policies
CREATE POLICY "Users can view their own memories"
    ON echo_memories FOR SELECT
    USING (auth.uid() = user_id);

CREATE POLICY "Users can insert their own memories"
    ON echo_memories FOR INSERT
    WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update their own memories"
    ON echo_memories FOR UPDATE
    USING (auth.uid() = user_id);

CREATE POLICY "Users can delete their own memories"
    ON echo_memories FOR DELETE
    USING (auth.uid() = user_id);

-- Contexts policies
CREATE POLICY "Users can view their own contexts"
    ON contexts FOR SELECT
    USING (auth.uid() = user_id);

CREATE POLICY "Users can insert their own contexts"
    ON contexts FOR INSERT
    WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update their own contexts"
    ON contexts FOR UPDATE
    USING (auth.uid() = user_id);

CREATE POLICY "Users can delete their own contexts"
    ON contexts FOR DELETE
    USING (auth.uid() = user_id);

-- Permissions policies
CREATE POLICY "Users can view their own permissions"
    ON permissions FOR SELECT
    USING (auth.uid() = user_id);

CREATE POLICY "Users can manage their own permissions"
    ON permissions FOR ALL
    USING (auth.uid() = user_id);

-- Consents policies
CREATE POLICY "Users can view their own consents"
    ON consents FOR SELECT
    USING (auth.uid() = user_id);

CREATE POLICY "Users can manage their own consents"
    ON consents FOR ALL
    USING (auth.uid() = user_id);

-- Usage logs policies
CREATE POLICY "Users can view their own usage logs"
    ON usage_logs FOR SELECT
    USING (auth.uid() = user_id);

-- Dividend calculations policies
CREATE POLICY "Users can view their own dividend calculations"
    ON dividend_calculations FOR SELECT
    USING (auth.uid() = user_id);

-- Payouts policies
CREATE POLICY "Users can view their own payouts"
    ON payouts FOR SELECT
    USING (auth.uid() = user_id);

CREATE POLICY "Users can manage their own payouts"
    ON payouts FOR ALL
    USING (auth.uid() = user_id); 