from flask import Flask
from config import Config

from flask import Flask
from config import Config


def create_app():
    # Create and configure the Flask aplication
    app = Flask(__name__)
    app.config.from_object(Config)

    # Home route confirms the API is running
    @app.route("/")
    def home():
        # return a JSON response with application status
        return {
            "message": "Welcome to GoalGetter - Track workouts, meals and fitness goals",
            "status": "running"
        }, 200

    # Users endpoint
    @app.route("/users")
    def users():
        # return a JSON response
        return {"message": "Users endpoint ready"}, 200

    # Meals endpoint
    @app.route("/meals")
    def meals():
        return {"message": "Meals endpoint ready"}, 200

    # Goals endpoint
    @app.route("/goals")
    def goals():
        return {"message": "Goals endpoint ready"}, 200

    # Workouts endpoint
    @app.route("/workouts")
    def workouts():
        return {"message": "Workouts endpoint ready"}, 200

    # exercises endpoint
    @app.route("/exercises")
    def exercises():
        return {"message": "Exercises endpoint ready"}, 200

    # workout-exercises endpoint
    @app.route("/workout-exercises")
    def workout_exercises():
        return {"message": "Workout Exercises endpoint ready"}, 200

    return app

# create application instance 
app = create_app()

# run the application in debug mode 
if __name__ == "__main__":
    app.run(debug=True)
