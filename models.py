
from pydantic import BaseModel
from typing import List

class ClubProfile(BaseModel):
    name: str
    location: str
    reach: int
    online_presence: int
    sponsor_fit: List[int]

class SponsorProfile(BaseModel):
    name: str
    target_region: str
    budget: int
    channel_focus: int
    brand_values: List[int]
