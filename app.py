from config import Config
from exercise_api import ExerciseAPI
from flask import Flask, request, jsonify, render_template
from frontend import frontend_bp



def create_app():

    # Create and configure the Flask aplication
    app = Flask(__name__)
    app.config.from_object(Config)

    # Registering blueprint onto app.py
    app.register_blueprint(frontend_bp)

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

        api = ExerciseAPI()

        equipment = request.args.get("equipment")
        body_part = request.args.get("body_part")
        exercise_type = request.args.get("exercise_type")
        name = request.args.get("name")
        muscle = request.args.get("muscle")

        try:

            if equipment:
                results = api.search_by_equipment(equipment)
            elif body_part:
                results = api.search_by_body_part(body_part)
            elif exercise_type:
                results = api.search_by_exercise_type(exercise_type)
            elif name:
                results = api.search_by_name(name)
            elif muscle:
                results = api.search_by_target_muscle(muscle)
            else:
                return {
                    "error": "Please provide your chosen exercise_type, body_part, muscle, equipment or name"
                }, 400  #  400 error - server didnt recognise the request

            # returning the html exercise card
            return render_template(
                "exercise_cards.html",
                exercises=results
            )

        except Exception as e:
            return {"error": str(e)}, 500  # unexpected

    #  Equipment endpoint - getting all equipments
    @app.route("/equipments")
    def equipments():
        api = ExerciseAPI()
        try:
            results = api.get_all_equipments()
            return jsonify(results), 200
        except Exception as e:
            return {"error": str(e)}, 500

            # body part endpoint - getting all body parts

    @app.route("/bodyparts")
    def bodyparts():
        api = ExerciseAPI()
        try:
            results = api.get_all_body_parts()
            return jsonify(results), 200
        except Exception as e:
            return {"error": str(e)}, 500

            # exercise_type endpoint - getting all exercise types

    @app.route("/exercisetypes")
    def exercisetypes():
        api = ExerciseAPI()
        try:
            results = api.get_all_exercise_types()
            return jsonify(results), 200
        except Exception as e:
            return {"error": str(e)}, 500

            # target_muscles endpoint - getting all target muscles

    @app.route("/targetmuscles")
    def targetmuscles():
        api = ExerciseAPI()
        try:
            results = api.get_all_target_muscles()
            return jsonify(results), 200
        except Exception as e:
            return {"error": str(e)}, 500

            # Exercise detail route

    @app.route("/exercises/<exercise_id>")
    def exercise_detail(exercise_id):

        api = ExerciseAPI()

        try:
            exercise = api.get_exercise_details(exercise_id)
            return jsonify(exercise), 200  # success

        except Exception as e:
            return {"error": str(e)}, 500

            # # workout-exercises endpoint

    # @app.route("/workout-exercises")
    # def workout_exercises():
    #     return {"message": "Workout Exercises endpoint ready"}, 200

    return app


# create application instance
app = create_app()

# run the application in debug mode
if __name__ == "__main__":
    app.run(debug=True)