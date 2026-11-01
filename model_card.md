# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

VibeMatch 1.0

VibeMatch is a simple music recommendation system that helps users discover songs based on their favorite genre, mood, and preferred energy level.
---

## 2. Intended Use  

My recommender is designed to suggest songs that match a user's music preferences. The user provides a favorite genre, preferred mood, and desired energy level. The system compares those preferences with the available songs and recommends the five highest-scoring matches.

This project is intended for classroom learning rather than a real music streaming service. It assumes that users can describe their music taste using three basic preferences.

---

## 3. How the Model Works  

My recommender uses content-based filtering. Instead of looking at what other people listen to, it compares the characteristics of each song with the user's preferences.

The scoring system works as follows:

Genre match: +2 points

Mood match: +1 point

Energy similarity: Up to +1 point

Energy similarity is calculated as:

1.0 - abs(song_energy - target_energy)

The maximum possible score is 4 points.

The system scores all songs, sorts them from highest to lowest, and returns the top five recommendations. It also explains why each song received its score.

---

## 4. Data  

My dataset contains 20 fictional songs. The starter dataset originally contained 10 songs, and I added 10 more to increase variety.

The catalog includes pop, lofi, rock, ambient, jazz, synthwave, indie pop, hip hop, R&B, EDM, folk, reggae, and dance pop.

Each song includes genre, mood, energy, tempo, valence, danceability, and acousticness. However, my scoring algorithm currently uses only genre, mood, and energy.

The dataset does not represent every genre, artist, language, or musical style.


---

## 5. Strengths  

My recommender works well when a user's preferences closely match songs in the dataset.

For example, the High-Energy Pop profile received Sunrise City as its top recommendation with a score of 3.97.

The Chill Lofi profile received Library Rain with a perfect score of 4.00, while the Deep Intense Rock profile received Storm Runner with a score of 3.96.

Another strength is that the system explains its recommendations by showing how each matching feature contributed to the final score.


---

## 6. Limitations and Bias 


My recommender has several limitations.

First, it only contains 20 fictional songs, so it cannot represent the full variety of music people listen to. Some genres have more songs than others, which may favor certain preferences.

Second, the algorithm only uses genre, mood, and energy. It does not consider lyrics, language, listening history, or user feedback.

Third, the scoring weights are chosen manually. Giving genre more importance may not work well for users who care more about energy or mood.

For example, the Conflicting Sad Energy profile wanted sad R&B music with high energy. Blue Window ranked first even though its energy was much lower than the user's preference.

The system also does not learn from user behavior.
---

## 7. Evaluation  

I tested the recommender using four user profiles.

User Profile

Top Recommendation

Original Score

High-Energy Pop

Sunrise City

3.97

Chill Lofi

Library Rain

4.00

Deep Intense Rock

Storm Runner

3.96

Conflicting Sad Energy

Blue Window

3.37

I also ran the automated tests using pytest, and both tests passed.

Scoring Experiment

I changed the algorithm to give genre matches 1 point instead of 2, and energy similarity up to 2 points instead of 1. Mood remained worth 1 point.
User Profile

Original Top Result

Experimental Top Result

High-Energy Pop

Sunrise City (3.97)

Sunrise City (3.94)

Chill Lofi

Library Rain (4.00)

Library Rain (4.00)

Deep Intense Rock

Storm Runner (3.96)

Storm Runner (3.92)

Conflicting Sad Energy

Blue Window (3.37)

Blue Window (2.74)

The top recommendation stayed the same for all four profiles, but some lower rankings changed.

For High-Energy Pop, Weekend Bounce moved from third to second, while Gym Hero dropped from second to fourth.

For Conflicting Sad Energy, Desert Lights moved from fourth to third, while Quiet Thoughts dropped out of the top five.

This experiment showed that changing feature weights can affect recommendation rankings. After the experiment, I restored the original scoring formula.


---

## 8. Future Work  
If I continued improving this project, I would expand the dataset to include more songs, genres, artists, and languages.

I would allow users to choose which preferences matter most to them. I would also include danceability, acousticness, and tempo in the scoring system.

Another improvement would be to collect user feedback, such as liking or skipping songs, so the system could improve its recommendations over time.

Finally, I would make the top five recommendations more diverse.

---

## 9. Personal Reflection  
This project helped me understand how music recommendation systems work and how different features influence their results. Before this project, I did not realize how much scoring weights could affect which songs appear at the top.

The most interesting part was testing a user with conflicting preferences. I expected the recommender to prioritize high-energy songs, but it preferred songs that matched the user's genre and mood. This helped me understand that an algorithm can follow its rules correctly while still producing recommendations that may not fully match what a user wants.

 I verified the implementation by running the recommender, checking the output for four user profiles, and running the automated tests.

This project changed how I think about music recommendation apps because I now understand that their results depend on the data, features, and decisions made when designing the algorithm.