
from fastapi import FastAPI
from models import ClubProfile, SponsorProfile
from matcher import calculate_match_score

app = FastAPI()

@app.post("/match/")
def match(club: ClubProfile, sponsor: SponsorProfile):
    score = calculate_match_score(club.sponsor_fit, sponsor.brand_values)
    return {
        "match_score": round(score * 100, 2),
        "club": club.name,
        "sponsor": sponsor.name
    }
