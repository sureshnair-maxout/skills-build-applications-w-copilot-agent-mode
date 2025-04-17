# Test data for the octofit_db database

test_data = {
    "users": [
        {"email": "john.doe@example.com", "name": "John Doe", "password": "password123"},
        {"email": "jane.smith@example.com", "name": "Jane Smith", "password": "password123"},
        {"email": "alice.wonderland@example.com", "name": "Alice Wonderland", "password": "password123"},
        {"email": "bob.builder@example.com", "name": "Bob Builder", "password": "password123"}
    ],
    "teams": [
        {"name": "Team Alpha", "members": ["john.doe@example.com", "jane.smith@example.com"]},
        {"name": "Team Beta", "members": ["alice.wonderland@example.com", "bob.builder@example.com"]}
    ],
    "activities": [
        {"user": "john.doe@example.com", "activity": "Running", "duration": 30, "date": "2025-04-17"},
        {"user": "jane.smith@example.com", "activity": "Cycling", "duration": 45, "date": "2025-04-16"},
        {"user": "alice.wonderland@example.com", "activity": "Swimming", "duration": 60, "date": "2025-04-15"},
        {"user": "bob.builder@example.com", "activity": "Hiking", "duration": 120, "date": "2025-04-14"}
    ],
    "leaderboard": [
        {"team": "Team Alpha", "score": 100},
        {"team": "Team Beta", "score": 150}
    ],
    "workouts": [
        {"name": "Morning Run", "type": "Cardio", "duration": 30},
        {"name": "Evening Yoga", "type": "Flexibility", "duration": 60}
    ]
}
