from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

class Gatekeeper:
    """Gatekeeper agent for managing access control and permissions."""
    
    def __init__(self):
        self.supabase: Client = create_client(
            os.getenv("SUPABASE_URL"),
            os.getenv("SUPABASE_KEY")
        )
        self.security = HTTPBearer()
        self.jwt_secret = os.getenv("JWT_SECRET")
    
    async def verify_token(self, credentials: HTTPAuthorizationCredentials = Security(HTTPBearer())) -> Dict[str, Any]:
        """Verify JWT token and return user information."""
        try:
            token = credentials.credentials
            payload = jwt.decode(token, self.jwt_secret, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token has expired")
        except jwt.JWTError:
            raise HTTPException(status_code=401, detail="Invalid token")
    
    async def check_permission(self, user_id: str, resource: str, action: str) -> bool:
        """Check if user has permission for specific resource and action."""
        result = self.supabase.table("permissions")\
            .select("*")\
            .eq("user_id", user_id)\
            .eq("resource", resource)\
            .eq("action", action)\
            .execute()
        
        return len(result.data) > 0
    
    async def grant_permission(self, user_id: str, resource: str, action: str, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Grant permission to user."""
        permission = {
            "user_id": user_id,
            "resource": resource,
            "action": action,
            "metadata": metadata or {},
            "created_at": datetime.utcnow().isoformat()
        }
        
        result = self.supabase.table("permissions").insert(permission).execute()
        return result.data[0]
    
    async def revoke_permission(self, user_id: str, resource: str, action: str) -> bool:
        """Revoke permission from user."""
        result = self.supabase.table("permissions")\
            .delete()\
            .eq("user_id", user_id)\
            .eq("resource", resource)\
            .eq("action", action)\
            .execute()
        
        return len(result.data) > 0
    
    async def list_permissions(self, user_id: str) -> List[Dict[str, Any]]:
        """List all permissions for a user."""
        result = self.supabase.table("permissions")\
            .select("*")\
            .eq("user_id", user_id)\
            .execute()
        
        return result.data
    
    async def create_consent(self, user_id: str, data_type: str, purpose: str, duration_days: int) -> Dict[str, Any]:
        """Create a new consent record."""
        consent = {
            "user_id": user_id,
            "data_type": data_type,
            "purpose": purpose,
            "expires_at": (datetime.utcnow() + timedelta(days=duration_days)).isoformat(),
            "created_at": datetime.utcnow().isoformat()
        }
        
        result = self.supabase.table("consents").insert(consent).execute()
        return result.data[0]
    
    async def check_consent(self, user_id: str, data_type: str, purpose: str) -> bool:
        """Check if user has given consent."""
        result = self.supabase.table("consents")\
            .select("*")\
            .eq("user_id", user_id)\
            .eq("data_type", data_type)\
            .eq("purpose", purpose)\
            .gt("expires_at", datetime.utcnow().isoformat())\
            .execute()
        
        return len(result.data) > 0
    
    async def revoke_consent(self, user_id: str, data_type: str, purpose: str) -> bool:
        """Revoke user consent."""
        result = self.supabase.table("consents")\
            .delete()\
            .eq("user_id", user_id)\
            .eq("data_type", data_type)\
            .eq("purpose", purpose)\
            .execute()
        
        return len(result.data) > 0
    
    async def track_usage(self, user_id: str, resource: str, action: str, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Track resource usage for attribution and billing."""
        usage = {
            "user_id": user_id,
            "resource": resource,
            "action": action,
            "metadata": metadata or {},
            "timestamp": datetime.utcnow().isoformat()
        }
        
        result = self.supabase.table("usage_logs").insert(usage).execute()
        return result.data[0] 