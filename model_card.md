# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  
VibeMatch 1.0 is a simple music recommendation system that suggests songs based on a user's favorite genre, mood, and energy level.

---

## 2. Intended Use  

My recommender is designed for classroom learning and demonstrating how content-based filtering works. Users provide their preferred genre, mood, and energy level, and the system recommends the five highest-scoring songs. It is not intended to replace a real streaming platform or accurately predict someone's long-term listening habits.


---

## 3. How the Model Works  

My recommender uses content-based filtering to compare song features with user preferences. A matching genre adds 2 points, a matching mood adds 1 point, and energy similarity adds up to 1 point using `1 - abs(song_energy - target_energy)`. The maximum score is 4 points. The system scores every song, sorts the results from highest to lowest, and returns the top five with explanations.


---

## 4. Data  

My dataset contains 20 fictional songs. I expanded the original dataset of 10 songs by adding 10 more songs with different genres and moods. Each song includes genre, mood, energy, tempo, valence, danceability, and acousticness. However, the current algorithm only uses genre, mood, and energy. The dataset does not represent every artist, genre, language, or musical style.



---

## 5. Strengths  
The recommender works well when a user's preferences closely match the available songs. For example, Sunrise City ranked first for High-Energy Pop with 3.97, Library Rain ranked first for Chill Lofi with 4.00, and Storm Runner ranked first for Deep Intense Rock with 3.96. Another strength is that the system explains how each song earned its score, making its decisions easier to understand.


---

## 6. Limitations and Bias 

The system has a small dataset of only 20 fictional songs, and some genres are represented more often than others. It also ignores lyrics, language, listening history, and user feedback. Since genre receives the highest weight, the algorithm may favor genre matches over songs with better energy similarity. For example, Blue Window ranked first for Conflicting Sad Energy even though its energy was much lower than requested. This could create a filter bubble where users repeatedly receive similar types of music. The system does not learn from user behavior.


---

## 7. Evaluation  

I tested four profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and Conflicting Sad Energy. Their top recommendations were Sunrise City (3.97), Library Rain (4.00), Storm Runner (3.96), and Blue Window (3.37). The first three profiles tested different musical preferences, while the fourth tested conflicting preferences. I also ran `python -m pytest -q`, and both automated tests passed.

### Profile Comparisons

High-Energy Pop and Chill Lofi received different top songs because one preferred energetic pop while the other preferred calm lofi. High-Energy Pop and Deep Intense Rock both preferred high energy, but their genre and mood differences led to different first-place songs. High-Energy Pop and Conflicting Sad Energy both had high target energy, but the sad R&B profile ranked Blue Window first because genre and mood outweighed energy.

Chill Lofi and Deep Intense Rock produced different recommendations because they had opposite energy preferences and different genres. Chill Lofi and Conflicting Sad Energy both favored more emotional or relaxed musical characteristics in some songs, but their different genre and energy targets changed the rankings. Deep Intense Rock and Conflicting Sad Energy both wanted high energy, yet Storm Runner ranked first for rock while Blue Window ranked first for sad R&B. This showed that genre and mood strongly influence the recommendations.

### Scoring Experiment

I changed the genre weight from 2 points to 1 point and increased energy similarity from a maximum of 1 point to 2 points. Mood remained worth 1 point.

| Profile | Original Top Result | Experimental Top Result |
|---|---|---|
| High-Energy Pop | Sunrise City (3.97) | Sunrise City (3.94) |
| Chill Lofi | Library Rain (4.00) | Library Rain (4.00) |
| Deep Intense Rock | Storm Runner (3.96) | Storm Runner (3.92) |
| Conflicting Sad Energy | Blue Window (3.37) | Blue Window (2.74) |

The top recommendation remained the same for every profile, but some lower rankings changed. For High-Energy Pop, Weekend Bounce moved from third to second while Gym Hero dropped from second to fourth. For Conflicting Sad Energy, Desert Lights moved from fourth to third and Quiet Thoughts dropped out of the top five. The experiment showed how manually chosen weights can affect rankings. I restored the original scoring formula afterward.



---

## 8. Future Work  
I would expand the dataset to include more songs, genres, artists, and languages. I would also allow users to choose which preferences matter most and include additional features such as danceability, tempo, and acousticness. Another improvement would be collecting user feedback, such as likes and skips, to make recommendations more personalized and diverse.


---

## 9. Personal Reflection  

This project helped me understand how recommendation systems use data and scoring rules to generate suggestions. My biggest learning moment was seeing how changing feature weights affected the rankings. I was also surprised that Blue Window ranked first for someone who preferred high-energy sad R&B, even though its energy was much lower than requested. This showed me that an algorithm can follow its rules correctly while still producing recommendations that may not fully match a user's expectations.

I used claude to help like how we were taught in this course. I double-checked the suggestions by running the recommender for four profiles, reviewing the scores, and running the automated tests. In the future, I would expand the dataset, include user feedback, and experiment with additional features to improve the recommendations.