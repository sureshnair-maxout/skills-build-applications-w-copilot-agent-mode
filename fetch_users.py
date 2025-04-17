from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['octofit_db']

# Fetch all users
users = db.users.find()

# Print user data
for user in users:
    print(user)
