from abc import ABC, abstractmethod
from typing import Dict, Any, List
import json
from datetime import datetime

class BaseProcessor(ABC):
    """Base class for all data processors in the Signal Layer."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.processed_data = []
        self.quality_scores = {}
    
    @abstractmethod
    async def process(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process raw data into structured signals."""
        pass
    
    @abstractmethod
    async def validate(self, data: Dict[str, Any]) -> bool:
        """Validate the processed data."""
        pass
    
    async def score_quality(self, data: Dict[str, Any]) -> float:
        """Score the quality of the processed data."""
        # Implement quality scoring logic
        return 1.0
    
    async def generate_embeddings(self, data: Dict[str, Any]) -> List[float]:
        """Generate embeddings for the processed data."""
        # Implement embedding generation logic
        return []
    
    def to_json(self) -> str:
        """Convert processed data to JSON."""
        return json.dumps({
            "processor": self.__class__.__name__,
            "timestamp": datetime.utcnow().isoformat(),
            "data": self.processed_data,
            "quality_scores": self.quality_scores
        })
    
    @classmethod
    def from_json(cls, json_str: str) -> 'BaseProcessor':
        """Create a processor instance from JSON."""
        data = json.loads(json_str)
        instance = cls(data.get("config", {}))
        instance.processed_data = data.get("data", [])
        instance.quality_scores = data.get("quality_scores", {})
        return instance

class SpotifyProcessor(BaseProcessor):
    """Processor for Spotify data."""
    
    async def process(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        # Implement Spotify-specific processing
        return {
            "type": "spotify",
            "tracks": raw_data.get("tracks", []),
            "artists": raw_data.get("artists", []),
            "playlists": raw_data.get("playlists", [])
        }
    
    async def validate(self, data: Dict[str, Any]) -> bool:
        required_fields = ["type", "tracks", "artists", "playlists"]
        return all(field in data for field in required_fields)

class GmailProcessor(BaseProcessor):
    """Processor for Gmail data."""
    
    async def process(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        # Implement Gmail-specific processing
        return {
            "type": "gmail",
            "emails": raw_data.get("emails", []),
            "contacts": raw_data.get("contacts", []),
            "labels": raw_data.get("labels", [])
        }
    
    async def validate(self, data: Dict[str, Any]) -> bool:
        required_fields = ["type", "emails", "contacts", "labels"]
        return all(field in data for field in required_fields) 