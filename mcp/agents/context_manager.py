from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
import json
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

class ContextManager:
    """Manages context and state across the Y system."""
    
    def __init__(self):
        self.supabase: Client = create_client(
            os.getenv("SUPABASE_URL"),
            os.getenv("SUPABASE_KEY")
        )
    
    async def create_context(self,
                           user_id: str,
                           context_type: str,
                           data: Dict[str, Any],
                           metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Create a new context."""
        context = {
            "user_id": user_id,
            "context_type": context_type,
            "data": data,
            "metadata": metadata or {},
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat()
        }
        
        result = self.supabase.table("contexts").insert(context).execute()
        return result.data[0]
    
    async def get_context(self, context_id: str) -> Dict[str, Any]:
        """Get a specific context by ID."""
        result = self.supabase.table("contexts").select("*").eq("id", context_id).execute()
        if not result.data:
            raise ValueError(f"Context {context_id} not found")
        return result.data[0]
    
    async def update_context(self,
                           context_id: str,
                           data: Optional[Dict[str, Any]] = None,
                           metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Update an existing context."""
        updates = {
            "updated_at": datetime.utcnow().isoformat()
        }
        
        if data is not None:
            updates["data"] = data
        if metadata is not None:
            updates["metadata"] = metadata
        
        result = self.supabase.table("contexts")\
            .update(updates)\
            .eq("id", context_id)\
            .execute()
        
        return result.data[0]
    
    async def delete_context(self, context_id: str) -> bool:
        """Delete a context."""
        result = self.supabase.table("contexts").delete().eq("id", context_id).execute()
        return len(result.data) > 0
    
    async def list_contexts(self,
                          user_id: str,
                          context_type: Optional[str] = None,
                          limit: int = 100,
                          offset: int = 0) -> List[Dict[str, Any]]:
        """List contexts for a user with optional filtering."""
        query = self.supabase.table("contexts")\
            .select("*")\
            .eq("user_id", user_id)
        
        if context_type:
            query = query.eq("context_type", context_type)
        
        result = query.order("created_at", desc=True)\
            .range(offset, offset + limit - 1)\
            .execute()
        
        return result.data
    
    async def merge_contexts(self,
                           context_ids: List[str],
                           merge_strategy: str = "latest") -> Dict[str, Any]:
        """Merge multiple contexts into one."""
        contexts = []
        for context_id in context_ids:
            context = await self.get_context(context_id)
            contexts.append(context)
        
        if merge_strategy == "latest":
            # Use the most recent data for each field
            merged_data = {}
            for context in sorted(contexts, key=lambda x: x["updated_at"], reverse=True):
                for key, value in context["data"].items():
                    if key not in merged_data:
                        merged_data[key] = value
        
        elif merge_strategy == "combine":
            # Combine all data, with lists concatenated
            merged_data = {}
            for context in contexts:
                for key, value in context["data"].items():
                    if key in merged_data:
                        if isinstance(merged_data[key], list):
                            merged_data[key].extend(value)
                        else:
                            merged_data[key] = [merged_data[key], value]
                    else:
                        merged_data[key] = value
        
        # Create new merged context
        merged_context = {
            "user_id": contexts[0]["user_id"],
            "context_type": contexts[0]["context_type"],
            "data": merged_data,
            "metadata": {
                "merged_from": context_ids,
                "merge_strategy": merge_strategy
            },
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat()
        }
        
        result = self.supabase.table("contexts").insert(merged_context).execute()
        return result.data[0]
    
    async def get_active_contexts(self,
                                user_id: str,
                                current_time: Optional[datetime] = None) -> List[Dict[str, Any]]:
        """Get all active contexts for a user."""
        if current_time is None:
            current_time = datetime.utcnow()
        
        result = self.supabase.table("contexts")\
            .select("*")\
            .eq("user_id", user_id)\
            .lte("created_at", current_time.isoformat())\
            .gte("updated_at", (current_time - timedelta(hours=24)).isoformat())\
            .execute()
        
        return result.data 