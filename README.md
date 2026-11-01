# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

This project is a Python-based music recommendation system called VibeMatch 1.0. It recommends songs based on a user's preferred genre, mood, and energy level. I expanded the original dataset from 10 to 20 fictional songs and created a scoring system that ranks songs based on how closely they match a user's preferences.

---

## How The System Works

My recommender uses content-based filtering to compare song features with user preferences. Each song contains information such as genre, mood, energy, tempo, danceability, and acousticness. The algorithm gives 2 points for matching genre, 1 point for matching mood, and up to 1 point for energy similarity. It then sorts the songs by score and recommends the top five, explaining why each song was selected.


---

## Getting Started

### Setup

To run the project, first install the required dependencies using pip install -r requirements.txt. Then run python -m src.main to generate recommendations. To check that the program works correctly, run python -m pytest -q. Both automated tests passed during my final testing.

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

I tested four user profiles with different preferences. High-Energy Pop received Sunrise City as its top recommendation with a score of 3.97. Chill Lofi received Library Rain with a perfect score of 4.00, while Deep Intense Rock received Storm Runner with 3.96. The Conflicting Sad Energy profile received Blue Window with 3.37, even though its energy was lower than the user's preference. These results showed how the algorithm prioritizes different features.## Sample Recommendation Output

I tested four user profiles using the original scoring system. Below is the actual terminal output from python -m src.main.

High-Energy Pop

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

Chill Lofi

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

Deep Intense Rock

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

Conflicting Sad Energy

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

---

## Experiments You Tried

I experimented with changing the scoring weights by reducing genre from 2 points to 1 point and increasing energy similarity from 1 point to 2 points. The top recommendation remained the same for all four profiles, but some lower rankings changed. For example, Weekend Bounce moved from third to second for High-Energy Pop, while Gym Hero dropped from second to fourth. This showed me how adjusting feature weights can influence recommendations. I restored the original scoring system after testing.

---

## Limitations and Risks

One limitation is that the dataset only contains 20 fictional songs, so it does not represent every genre or music preference. The algorithm also does not consider listening history, lyrics, language, or user feedback. Since genre has the highest weight, it may favor songs with matching genres even when their energy levels are less suitable. In the future, I would expand the dataset, add more features, and allow users to customize the scoring weights.

---

## Reflection

This project helped me understand how recommendation systems use data and scoring rules to make personalized suggestions. I learned that small changes in an algorithm can affect rankings and that recommendations may not always match what users expect. Testing different profiles helped me recognize how bias can appear through manually chosen weights. Overall, I gained a better understanding of content-based filtering, algorithm design, and the importance of evaluating results.


