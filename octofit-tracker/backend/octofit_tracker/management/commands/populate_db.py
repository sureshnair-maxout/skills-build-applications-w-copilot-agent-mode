import sys
import os
from pymongo import MongoClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from octofit_tracker.test_data import test_data

# Connect to MongoDB directly without relying on Django
client = MongoClient('mongodb://localhost:27017')
db = client['octofit_db']

# Populate users collection
db.users.insert_many(test_data['users'])

# Populate teams collection
db.teams.insert_many(test_data['teams'])

# Populate activities collection
db.activity.insert_many(test_data['activities'])

# Populate leaderboard collection
db.leaderboard.insert_many(test_data['leaderboard'])

# Populate workouts collection
db.workouts.insert_many(test_data['workouts'])

print('Test data added successfully')
