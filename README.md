# 🎵 Music Recommender Simulation

## Project Summary

This project is a Python-based music recommendation system called VibeMatch 1.0. It recommends songs based on a user's preferred genre, mood, and energy level. I expanded the original dataset from 10 to 20 fictional songs and created a scoring system that ranks songs based on how closely they match a user's preferences.

---

## How The System Works

My recommender uses content-based filtering, which compares song characteristics with a user's preferences instead of using other people's listening histories. Real streaming platforms can also use collaborative filtering, which learns from likes, skips, playlists, and similar listeners. My Song objects contain information such as genre, mood, energy, tempo, valence, danceability, and acousticness. The UserProfile stores a preferred genre, mood, and target energy. The algorithm gives 2 points for a genre match, 1 point for a mood match, and up to 1 point for energy similarity, calculated using `1 - abs(song_energy - target_energy)`. Every song receives a score, and the top five are ranked from highest to lowest. One possible bias is that genre has the highest weight, so a song with the right genre might rank above a song with a better energy match.


---

## Getting Started


To run the project, create a virtual environment using `python3 -m venv .venv` and activate it with `source .venv/bin/activate` on Mac. Install dependencies using `pip install -r requirements.txt`, then run `python -m src.main` to generate recommendations. To run the automated tests, use `python -m pytest -q`. Both tests passed during my final testing.

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

I tested four different user profiles using the original scoring system. Below is the actual terminal output from `python -m src.main`.

### High-Energy Pop

```text
--- High-Energy Pop ---
1. Sunrise City - Score: 3.97
Because: Genre match (+2.0), Mood match (+1.0), Energy similarity (+0.97)

2. Gym Hero - Score: 2.92
Because: Genre match (+2.0), Energy similarity (+0.92)

3. Weekend Bounce - Score: 1.97
Because: Mood match (+1.0), Energy similarity (+0.97)

4. Electric Heart - Score: 1.95
Because: Mood match (+1.0), Energy similarity (+0.95)

5. Rooftop Lights - Score: 1.91
Because: Mood match (+1.0), Energy similarity (+0.91)
```

### Chill Lofi

```text
--- Chill Lofi ---
1. Library Rain - Score: 4.00
Because: Genre match (+2.0), Mood match (+1.0), Energy similarity (+1.00)

2. Midnight Coding - Score: 3.93
Because: Genre match (+2.0), Mood match (+1.0), Energy similarity (+0.93)

3. Focus Flow - Score: 2.95
Because: Genre match (+2.0), Energy similarity (+0.95)

4. Spacewalk Thoughts - Score: 1.93
Because: Mood match (+1.0), Energy similarity (+0.93)

5. Coffee Shop Stories - Score: 0.98
Because: Energy similarity (+0.98)
```

### Deep Intense Rock

```text
--- Deep Intense Rock ---
1. Storm Runner - Score: 3.96
Because: Genre match (+2.0), Mood match (+1.0), Energy similarity (+0.96)

2. Gym Hero - Score: 1.98
Because: Mood match (+1.0), Energy similarity (+0.98)

3. Street Rhythm - Score: 1.97
Because: Mood match (+1.0), Energy similarity (+0.97)

4. Desert Lights - Score: 0.99
Because: Energy similarity (+0.99)

5. Electric Heart - Score: 0.95
Because: Energy similarity (+0.95)
```

### Conflicting Sad Energy

```text
--- Conflicting Sad Energy ---
1. Blue Window - Score: 3.37
Because: Genre match (+2.0), Mood match (+1.0), Energy similarity (+0.37)

2. After Hours - Score: 2.68
Because: Genre match (+2.0), Energy similarity (+0.68)

3. Quiet Thoughts - Score: 1.25
Because: Mood match (+1.0), Energy similarity (+0.25)

4. Desert Lights - Score: 0.99
Because: Energy similarity (+0.99)

5. Gym Hero - Score: 0.98
Because: Energy similarity (+0.98)
```

---

## Experiments You Tried

I experimented with changing the scoring weights by reducing genre from 2 points to 1 point and increasing energy similarity from 1 point to 2 points. Mood remained worth 1 point. The top recommendation stayed the same for all four profiles, but some lower rankings changed. For High-Energy Pop, Weekend Bounce moved from third to second, while Gym Hero dropped from second to fourth. For Conflicting Sad Energy, Desert Lights moved from fourth to third, while Quiet Thoughts dropped out of the top five. This showed me that changing feature weights affects recommendations. I restored the original scoring system after the experiment.

---

## Limitations and Risks

One limitation is that the dataset only contains 20 fictional songs, so it cannot represent every genre or musical preference. The algorithm also does not consider listening history, lyrics, language, or user feedback. Since genre has the highest weight, it may recommend songs with matching genres even when their energy levels are less suitable. This could create a filter bubble by repeatedly favoring certain musical styles. In the future, I would expand the dataset, add more song features, and allow users to adjust the scoring weights.


---

## Reflection

This project helped me understand how recommendation systems use data and scoring rules to make personalized suggestions. The biggest surprise was that Blue Window ranked first for someone who wanted high-energy sad R&B, even though its energy was much lower than requested. This showed me that an algorithm can follow its rules correctly without producing the best recommendation for every user. I checked the suggestions by running the program, comparing results, and using automated tests. If I continued this project, I would add more songs and user feedback to make recommendations more personalized.

more info in the model_card.md

