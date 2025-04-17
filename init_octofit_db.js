// Initialize the octofit_db database and create collections
use octofit_db;
db.createCollection("users");
db.createCollection("teams");
db.createCollection("activity");
db.createCollection("leaderboard");
db.createCollection("workouts");
// Create a unique index for the email field in the users collection
db.users.createIndex({ email: 1 }, { unique: true });
