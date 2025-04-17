from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
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
        db.teams.insert_one({"name": "Team Beta", "members": ["alice.wonderland@example.com", "bob.builder@example.com"]})

        # Populate activity collection
        db.activity.insert_many([
            {"user": "john.doe@example.com", "type": "Running", "duration": 30, "date": "2025-04-17"},
            {"user": "jane.smith@example.com", "type": "Cycling", "duration": 45, "date": "2025-04-16"},
            {"user": "alice.wonderland@example.com", "type": "Swimming", "duration": 60, "date": "2025-04-15"},
            {"user": "bob.builder@example.com", "type": "Hiking", "duration": 120, "date": "2025-04-14"}
        ])

        # Populate leaderboard collection
        db.leaderboard.insert_many([
            {"user": "john.doe@example.com", "points": 100},
            {"user": "jane.smith@example.com", "points": 150},
            {"user": "alice.wonderland@example.com", "points": 200},
            {"user": "bob.builder@example.com", "points": 250}
        ])

        # Populate workouts collection
        db.workouts.insert_many([
            {"name": "Push-ups", "description": "Do 20 push-ups"},
            {"name": "Sit-ups", "description": "Do 30 sit-ups"},
            {"name": "Plank", "description": "Hold a plank for 1 minute"},
            {"name": "Jumping Jacks", "description": "Do 50 jumping jacks"}
        ])

        self.stdout.write(self.style.SUCCESS('Database populated with test data'))
