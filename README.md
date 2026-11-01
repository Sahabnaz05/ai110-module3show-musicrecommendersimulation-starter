# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

This project creates a simple music recommendation system using Python. It recommends songs based on a user's favorite genre, mood, and preferred energy level. The system uses content-based filtering to compare song features with user preferences. Each song receives a score, and the songs with the highest scores are recommended first. The goal is to understand how music platforms turn data into personalized recommendations.
Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

My music recommender uses content-based filtering. Unlike collaborative filtering, which looks at other users' listening habits, content-based filtering compares the features of songs with a user's preferences.

Each song has features such as genre, mood, energy, tempo, valence, danceability, and acousticness.

The user profile stores three preferences: favorite genre, favorite mood, and target energy.

The recommender will use these scoring rules:

Genre match: +2.0 points

Mood match: +1.0 point

Energy similarity: Up to +1.0 point

Energy similarity is calculated using:

1.0 - abs(song_energy - target_energy)

The system scores every song, sorts the results from highest to lowest, and recommends the top five songs.

One limitation is that the system might favor certain genres too much because genre has the highest weight.
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:
## Sample Recommendation Output

The recommender loaded 20 songs and tested three different user profiles.

### High-Energy Pop
```text
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

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



