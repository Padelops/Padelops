
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def calculate_match_score(club_features, sponsor_features):
    club_vec = np.array(club_features).reshape(1, -1)
    sponsor_vec = np.array(sponsor_features).reshape(1, -1)
    score = cosine_similarity(club_vec, sponsor_vec)[0][0]
    return float(score)
