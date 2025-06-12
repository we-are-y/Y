from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
import numpy as np
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

class DividendCalculator:
    """Calculates and routes dividends based on data usage and value."""
    
    def __init__(self):
        self.supabase: Client = create_client(
            os.getenv("SUPABASE_URL"),
            os.getenv("SUPABASE_KEY")
        )
        self.base_rates = {
            "spotify": 0.01,  # $0.01 per play
            "gmail": 0.005,   # $0.005 per email
            "location": 0.002, # $0.002 per location point
            "health": 0.05,   # $0.05 per health data point
            "default": 0.001  # Default rate for other data types
        }
    
    async def calculate_dividend(self,
                               user_id: str,
                               data_type: str,
                               usage_count: int,
                               quality_score: float = 1.0) -> float:
        """Calculate dividend for data usage."""
        base_rate = self.base_rates.get(data_type, self.base_rates["default"])
        dividend = base_rate * usage_count * quality_score
        
        # Store dividend calculation
        calculation = {
            "user_id": user_id,
            "data_type": data_type,
            "usage_count": usage_count,
            "quality_score": quality_score,
            "base_rate": base_rate,
            "dividend": dividend,
            "calculated_at": datetime.utcnow().isoformat()
        }
        
        result = self.supabase.table("dividend_calculations").insert(calculation).execute()
        return dividend
    
    async def get_user_dividends(self,
                               user_id: str,
                               start_date: Optional[datetime] = None,
                               end_date: Optional[datetime] = None) -> List[Dict[str, Any]]:
        """Get all dividend calculations for a user within a date range."""
        query = self.supabase.table("dividend_calculations")\
            .select("*")\
            .eq("user_id", user_id)
        
        if start_date:
            query = query.gte("calculated_at", start_date.isoformat())
        if end_date:
            query = query.lte("calculated_at", end_date.isoformat())
        
        result = query.execute()
        return result.data
    
    async def process_payout(self,
                           user_id: str,
                           amount: float,
                           payment_method: str) -> Dict[str, Any]:
        """Process a dividend payout."""
        payout = {
            "user_id": user_id,
            "amount": amount,
            "payment_method": payment_method,
            "status": "pending",
            "created_at": datetime.utcnow().isoformat()
        }
        
        result = self.supabase.table("payouts").insert(payout).execute()
        return result.data[0]
    
    async def update_payout_status(self,
                                 payout_id: str,
                                 status: str,
                                 transaction_id: Optional[str] = None) -> Dict[str, Any]:
        """Update the status of a payout."""
        updates = {
            "status": status,
            "updated_at": datetime.utcnow().isoformat()
        }
        
        if transaction_id:
            updates["transaction_id"] = transaction_id
        
        result = self.supabase.table("payouts")\
            .update(updates)\
            .eq("id", payout_id)\
            .execute()
        
        return result.data[0]
    
    async def get_payout_history(self,
                               user_id: str,
                               limit: int = 100,
                               offset: int = 0) -> List[Dict[str, Any]]:
        """Get payout history for a user."""
        result = self.supabase.table("payouts")\
            .select("*")\
            .eq("user_id", user_id)\
            .order("created_at", desc=True)\
            .range(offset, offset + limit - 1)\
            .execute()
        
        return result.data
    
    async def calculate_total_earnings(self,
                                     user_id: str,
                                     start_date: Optional[datetime] = None,
                                     end_date: Optional[datetime] = None) -> Dict[str, Any]:
        """Calculate total earnings for a user."""
        query = self.supabase.table("dividend_calculations")\
            .select("data_type, sum(dividend) as total")\
            .eq("user_id", user_id)
        
        if start_date:
            query = query.gte("calculated_at", start_date.isoformat())
        if end_date:
            query = query.lte("calculated_at", end_date.isoformat())
        
        result = query.group("data_type").execute()
        
        totals = {item["data_type"]: item["total"] for item in result.data}
        grand_total = sum(totals.values())
        
        return {
            "by_type": totals,
            "total": grand_total
        } 