
"""
Command line runner for the Music Recommender Simulation.
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    print(f"Loaded songs: {len(songs)}")

    user_profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.85
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.35
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.95
        },
        "Conflicting Sad Energy": {
            "genre": "r&b",
            "mood": "sad",
             "energy": 0.95
        }
    }

    for profile_name, user_prefs in user_profiles.items():
        print(f"\n--- {profile_name} ---")

        recommendations = recommend_songs(
            user_prefs, songs, k=5
        )

        for i, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec

            print(f"{i}. {song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
