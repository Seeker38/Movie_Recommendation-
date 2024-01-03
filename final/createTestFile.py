import pandas as pd
from datetime import datetime
import random

# Existing rating data
existing_ratings_data = {
    'userId': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'original_title': [
        'The Dark Knight', 'Inception', 'Forrest Gump',
        'Mad Max: Fury Road', 'John Wick', 'Mission: Impossible - Ghost Protocol',
        'The Raid: Redemption', 'The Avengers', 'The Bourne Ultimatum', 'Avatar'
    ],
    'rating': [4.5, 5.0, 4.0, 4.8, 4.2, 4.7, 4.3, 4.6, 4.4, 4.9],
    'date': [datetime.now()] * 10
}

# Create a DataFrame for existing ratings
existing_ratings_df = pd.DataFrame(existing_ratings_data)

# Generate random ratings for user 101 between 3 and 5 for each movie
random_ratings = [round(random.uniform(3, 5), 2) for _ in range(len(existing_ratings_df['original_title']))]

# Add ratings for user 101
new_ratings_data = {
    'userId': [101] * len(existing_ratings_df['original_title']),
    'original_title': existing_ratings_df['original_title'].tolist(),
    'rating': random_ratings,
    'date': [datetime.now()] * len(existing_ratings_df['original_title'])
}

# Create a DataFrame for new ratings
new_ratings_df = pd.DataFrame(new_ratings_data)

# Concatenate the existing and new ratings DataFrames
combined_ratings_df = pd.concat([existing_ratings_df, new_ratings_df], ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_ratings_df.to_csv('data/newRatings.csv', index=False)

print("Combined ratings data saved to 'newRatings.csv'")
