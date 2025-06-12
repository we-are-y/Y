from typing import Dict, Any, List, Optional
import json
from datetime import datetime, timedelta
import numpy as np
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

class MemoryStore:
    """Persistent memory store for Echo."""
    
    def __init__(self):
        self.supabase: Client = create_client(
            os.getenv("SUPABASE_URL"),
            os.getenv("SUPABASE_KEY")
        )
        self.vector_dimension = 1536  # OpenAI embedding dimension
    
    async def store_memory(self, 
                          user_id: str,
                          content: Dict[str, Any],
                          embedding: Optional[List[float]] = None,
                          metadata: Optional[Dict[str, Any]] = None) -> str:
        """Store a new memory with optional embedding."""
        memory = {
            "user_id": user_id,
            "content": content,
            "embedding": embedding,
            "metadata": metadata or {},
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat()
        }
        
        result = self.supabase.table("echo_memories").insert(memory).execute()
        return result.data[0]["id"]
    
    async def retrieve_memory(self, memory_id: str) -> Dict[str, Any]:
        """Retrieve a specific memory by ID."""
        result = self.supabase.table("echo_memories").select("*").eq("id", memory_id).execute()
        if not result.data:
            raise ValueError(f"Memory {memory_id} not found")
        return result.data[0]
    
    async def search_memories(self,
                            user_id: str,
                            query_embedding: List[float],
                            limit: int = 10) -> List[Dict[str, Any]]:
        """Search memories using vector similarity."""
        # Convert query embedding to PostgreSQL vector format
        query_vector = f"[{','.join(map(str, query_embedding))}]"
        
        # Perform vector similarity search
        result = self.supabase.rpc(
            "match_memories",
            {
                "query_embedding": query_vector,
                "match_threshold": 0.7,
                "match_count": limit,
                "p_user_id": user_id
            }
        ).execute()
        
        return result.data
    
    async def update_memory(self,
                          memory_id: str,
                          content: Optional[Dict[str, Any]] = None,
                          embedding: Optional[List[float]] = None,
                          metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Update an existing memory."""
        updates = {
            "updated_at": datetime.utcnow().isoformat()
        }
        
        if content is not None:
            updates["content"] = content
        if embedding is not None:
            updates["embedding"] = embedding
        if metadata is not None:
            updates["metadata"] = metadata
        
        result = self.supabase.table("echo_memories").update(updates).eq("id", memory_id).execute()
        return result.data[0]
    
    async def delete_memory(self, memory_id: str) -> bool:
        """Delete a memory."""
        result = self.supabase.table("echo_memories").delete().eq("id", memory_id).execute()
        return len(result.data) > 0
    
    async def list_memories(self,
                          user_id: str,
                          limit: int = 100,
                          offset: int = 0) -> List[Dict[str, Any]]:
        """List memories for a user with pagination."""
        result = self.supabase.table("echo_memories")\
            .select("*")\
            .eq("user_id", user_id)\
            .order("created_at", desc=True)\
            .range(offset, offset + limit - 1)\
            .execute()
        
        return result.data
    
    async def prune_memories(self,
                           user_id: str,
                           max_age_days: int = 30) -> int:
        """Prune old memories."""
        cutoff_date = (datetime.utcnow() - timedelta(days=max_age_days)).isoformat()
        
        result = self.supabase.table("echo_memories")\
            .delete()\
            .eq("user_id", user_id)\
            .lt("created_at", cutoff_date)\
            .execute()
        
        return len(result.data) 