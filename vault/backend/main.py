from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client, Client
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Vault API", description="Human Vault System Backend")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Supabase client
supabase: Client = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Vault API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Data Models
from pydantic import BaseModel
from datetime import datetime
from typing import List, Dict, Any

class VaultEntry(BaseModel):
    id: str
    user_id: str
    data_type: str
    content: Dict[str, Any]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime

class SchemaField(BaseModel):
    name: str
    type: str
    unit: Optional[str] = None
    description: Optional[str] = None

class SchemaRegistryEntry(BaseModel):
    type: str
    display_name: str
    version: int = 1
    fields: list[SchemaField]
    category: Optional[str] = None
    visibility: Optional[str] = "private"
    ui_widget_hint: Optional[str] = None

# Routes
@app.post("/vault/entries")
async def create_entry(entry: VaultEntry):
    try:
        result = supabase.table("vault_entries").insert(entry.dict()).execute()
        return result.data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/vault/entries/{entry_id}")
async def get_entry(entry_id: str):
    try:
        result = supabase.table("vault_entries").select("*").eq("id", entry_id).execute()
        if not result.data:
            raise HTTPException(status_code=404, detail="Entry not found")
        return result.data[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/vault/entries")
async def list_entries(
    user_id: str,
    data_type: Optional[str] = None,
    limit: int = 100,
    offset: int = 0
):
    try:
        query = supabase.table("vault_entries").select("*").eq("user_id", user_id)
        if data_type:
            query = query.eq("data_type", data_type)
        result = query.range(offset, offset + limit - 1).execute()
        return result.data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/schemas/register")
async def register_schema(schema: SchemaRegistryEntry):
    # Check if schema with type and version already exists
    existing = supabase.table("schema_registry").select("*") \
        .eq("type", schema.type).eq("version", schema.version).execute()
    if existing.data:
        raise HTTPException(status_code=409, detail="Schema with this type and version already exists.")
    try:
        result = supabase.table("schema_registry").insert(schema.dict()).execute()
        return {"message": "Schema registered successfully", "schema": result.data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 