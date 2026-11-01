import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class Song:
    """Represents a song and its attributes."""
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """Stores a user's music preferences."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file."""
    songs = []

    with open(csv_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["id"] = int(row["id"])

            for feature in [
                "energy",
                "tempo_bpm",
                "valence",
                "danceability",
                "acousticness"
            ]:
                row[feature] = float(row[feature])

            songs.append(row)

    return songs


def score_song(
    user_prefs: Dict,
    song: Dict
) -> Tuple[float, List[str]]:
    """Score a song and explain its matches."""
    score = 0.0
    reasons = []

    genre = user_prefs.get(
        "genre", user_prefs.get("favorite_genre", "")
    )
    mood = user_prefs.get(
        "mood", user_prefs.get("favorite_mood", "")
    )
    energy = float(user_prefs.get(
        "energy", user_prefs.get("target_energy", 0.5)
    ))

    if song["genre"].lower() == genre.lower():
        score += 2.0
        reasons.append("Genre match (+2.0)")

    if song["mood"].lower() == mood.lower():
        score += 1.0
        reasons.append("Mood match (+1.0)")

    energy_gap = abs(song["energy"] - energy)
    energy_points = max(0.0, 1.0 - energy_gap)

    score += energy_points
    reasons.append(
        f"Energy similarity (+{energy_points:.2f})"
    )

    return round(score, 2), reasons
def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5
) -> List[Tuple[Dict, float, str]]:
    """Return the top k songs ranked by score."""
    results = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        results.append((song, score, explanation))

    results.sort(key=lambda item: item[1], reverse=True)

    return results[:max(0, k)]


class Recommender:
    """Object-oriented music recommender."""

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def _score(self, user: UserProfile, song: Song) -> float:
        """Calculate a score for a Song object."""
        song_data = {
            "genre": song.genre,
            "mood": song.mood,
            "energy": song.energy
        }

        preferences = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy
        }

        score, _ = score_song(preferences, song_data)

        return score

    def recommend(
        self,
        user: UserProfile,
        k: int = 5
    ) -> List[Song]:
        """Return the highest-ranked Song objects."""
        ranked = sorted(
            self.songs,
            key=lambda song: self._score(user, song),
            reverse=True
        )

        return ranked[:max(0, k)]

    def explain_recommendation(
        self,
        user: UserProfile,
        song: Song
    ) -> str:
        """Explain why a song was recommended."""
        preferences = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy
        }

        song_data = {
            "genre": song.genre,
            "mood": song.mood,
            "energy": song.energy
        }

        score, reasons = score_song(
            preferences, song_data
        )

        return (
            f"{song.title} scored {score:.2f}: "
            + ", ".join(reasons)
        )
