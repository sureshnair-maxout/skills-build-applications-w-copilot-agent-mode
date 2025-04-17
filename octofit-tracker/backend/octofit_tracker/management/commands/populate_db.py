from pymongo import MongoClient

# Connect to MongoDB directly without relying on Django
client = MongoClient('mongodb://localhost:27017')
db = client['octofit_db']

# Populate users collection
db.users.insert_many([
    {"email": "john.doe@example.com", "name": "John Doe", "password": "password123"},
    {"email": "jane.smith@example.com", "name": "Jane Smith", "password": "password123"},
    {"email": "alice.wonderland@example.com", "name": "Alice Wonderland", "password": "password123"},
    {"email": "bob.builder@example.com", "name": "Bob Builder", "password": "password123"}
])

# Populate teams collection
db.teams.insert_one({"name": "Team Alpha", "members": ["john.doe@example.com", "jane.smith@example.com"]})

# Populate activity collection
db.activity.insert_many([
    {"user": "john.doe@example.com", "activity": "Running", "duration": 30},
    {"user": "jane.smith@example.com", "activity": "Cycling", "duration": 45}
])

# Populate leaderboard collection
db.leaderboard.insert_one({"team": "Team Alpha", "score": 100})

# Populate workouts collection
db.workouts.insert_many([
    {"name": "Morning Run", "type": "Cardio", "duration": 30},
    {"name": "Evening Yoga", "type": "Flexibility", "duration": 60}
])

print('Test data added successfully')
