"""
    Blueprint Refactoring – Work in Progress

    This file demonstrates the implementation of Flask Blueprints to organise frontend routes.
    The blueprint is registered in app.py, and all frontend templates are served through it.

    Integration of teammates' backend functions is planned.
    Currently, mock data is used for frontend testing and demonstration.
    This follows industry-standard Flask architecture patterns.

NOTE:
    Inside the @frontend_bp.route(</route_name>) must be an identical match to the <href="/..."> in the layout.html file for the UI to correspond to the backend.

"""

import time
from flask import Blueprint, Flask, flash, redirect, render_template, request, url_for


# 'frontend' is the internal name, __name__ helps Flask locate templates
frontend_bp = Blueprint('frontend', __name__)

# This is the dashboard homepage
@frontend_bp.route('/')
def index():
    # Here is the calendar and widgets on the dashboard
    return render_template('dashboard.html')

@frontend_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@frontend_bp.route('/exercises', methods=['GET', 'POST'])
def exercises():
    # Hardcoded data provided by teammate
    body_parts = ['BACK', 'CALVES', 'CHEST', 'FOREARMS', 'HIPS', 'NECK', 'SHOULDERS', 'THIGHS', 'WAIST', 'HANDS', 'FEET', 'FACE', 'FULL BODY', 'BICEPS', 'UPPER ARMS', 'TRICEPS', 'HAMSTRINGS', 'QUADRICEPS']
    equipment = ['ASSISTED', 'BAND', 'BARBELL', 'BATTLING ROPE', 'BODY WEIGHT', 'BOSU BALL', 'CABLE', 'DUMBBELL', 'EZ BARBELL', 'HAMMER', 'KETTLEBELL', 'LEVERAGE MACHINE', 'MEDICINE BALL', 'OLYMPIC BARBELL', 'POWER SLED', 'RESISTANCE BAND', 'ROLL', 'ROLLBALL', 'ROPE', 'SLED MACHINE', 'SMITH MACHINE', 'STABILITY BALL', 'STICK', 'SUSPENSION', 'TRAP BAR', 'VIBRATE PLATE', 'WEIGHTED', 'WHEEL ROLLER']
    categories = ['STRENGTH', 'CARDIO', 'PLYOMETRICS', 'STRETCHING', 'WEIGHTLIFTING', 'YOGA', 'AEROBIC']
    muscles = ['ADDUCTOR LONGUS', 'ADDUCTOR BREVIS', 'ADDUCTOR MAGNUS', 'BICEPS BRACHII', 'BRACHIALIS', 'BRACHIORADIALIS', 'DEEP HIP EXTERNAL ROTATORS', 'ANTERIOR DELTOID', 'LATERAL DELTOID', 'POSTERIOR DELTOID', 'ERECTOR SPINAE', 'GASTROCNEMIUS', 'GLUTEUS MAXIMUS', 'GLUTEUS MEDIUS', 'GLUTEUS MINIMUS', 'GRACILIS', 'HAMSTRINGS', 'ILIOPSOAS', 'INFRASPINATUS', 'LATISSIMUS DORSI', 'LEVATOR SCAPULAE', 'OBLIQUES', 'PECTINEUS', 'PECTORALIS MAJOR CLAVICULAR HEAD', 'PECTORALIS MAJOR STERNAL HEAD', 'POPLITEUS', 'QUADRICEPS', 'RECTUS ABDOMINIS', 'SARTORIUS', 'SERRATUS ANTE', 'SERRATUS ANTERIOR', 'SOLEUS', 'SPLENIUS', 'STERNOCLEIDOMASTOID', 'SUBSCAPULARIS', 'TENSOR FASCIAE LATAE', 'TERES MAJOR', 'TERES MINOR', 'TIBIALIS ANTERIOR', 'TRANSVERSUS ABDOMINIS', 'TRAPEZIUS LOWER FIBERS', 'TRAPEZIUS MIDDLE FIBERS', 'TRAPEZIUS UPPER FIBERS', 'TRICEPS BRACHII', 'WRIST EXTENSORS', 'WRIST FLEXORS']

    # Just printing to terminal to see if it works. '.args' is for GET HTTP method only, '.form' is for POST method.
    selected_body = request.args.get('body_part') # e.g.WHERE body_part = 'Shoulders'
    selected_equipment = request.args.get('equipment') # e.g. WHERE equipment - 'Dumbells'
    selected_category = request.args.get('categories') # e.g. WHERE category = 'Strength'
    selected_muscle = request.args.get('muscles') # e.g. WHERE target_muscle = 'Biceps Brachii'

    print(f" Filters applied: Body={selected_body}, Equipment={selected_equipment},Category={selected_category}, Muscle={selected_muscle}")

    return render_template('workouts.html',
                           body_parts=body_parts,
                           equipment=equipment,
                           categories=categories,
                           muscles=muscles # Links variables names here to the template names
                           )

@frontend_bp.route('/meals_and_recipes')
def meals_and_recipes():
    # Hardcoded mock data – like an API response
    meals = [
        {
            'id': 1,
            'name': 'Greek Salad',
            'description': 'Fresh vegetables, feta cheese, olives, and a light dressing.',
            'image_url': '../static/greek-salad-test-image.jpeg',  # placeholder images
            'prep_time': 15,
            'calories': 320
        },
        {
            'id': 2,
            'name': 'Grilled Chicken',
            'description': 'Herb-marinated chicken breast with roasted vegetables.',
            'image_url': '../static/grilled-chicken-test-image.jpeg',
            'prep_time': 25,
            'calories': 420
        },
        {
            'id': 3,
            'name': 'Protein Smoothie',
            'description': 'Banana, berries, whey protein, and almond milk.',
            'image_url': '../static/protein-smoothie-test-image.jpeg',
            'prep_time': 5,
            'calories': 250
        },
        # Some examples, more could be added.
    ]
    return render_template('meals_and_recipes.html', meals=meals)

@frontend_bp.route('/history')
def history():
    return render_template('history.html')

@frontend_bp.route('/support', methods=['GET', 'POST'])
def support():
    if request.method == 'POST':
        # Grabs all data from form
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        selected_issue = request.form.get('support_category')

        # Mock validation to check required fields exist
        if name and email and message and selected_issue:
            # Generating a fake ticket number using time module, unique number every second
            fake_ticket_number = int(time.time()) # Do not want a float

            # flash() sucessful message with the fake ticket number
            flash(f"Thank you {name}! Your support ticket #{fake_ticket_number} has been submitted! A team member will email your shortly", "success")

        else: # If some or any of the fields are missing from the form
            flash("Please fill out all the required fields before submitting", "info")

    return render_template('support.html')

@frontend_bp.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')

        # Mock validation (no hashing yet, just checking for functionality)
        # if they are entered in the form and match
        if new_password and confirm_password and new_password == confirm_password:
            flash("Password updated successfully! (Mock result - hashing coming soon", "success")
        # if they are entered in the form but do not match
        elif new_password and confirm_password and new_password != confirm_password:
            flash("Passwords do not match. Please try again")
        else: # Error occurred, likely missing field
            flash("Please fill in both password fields to proceed","info")

        return redirect('/settings') # if incorrect/missing fields sends back to settings page

    return render_template('settings.html')

@frontend_bp.route('/logout')
def logout():
    return render_template('logout.html')

if __name__ == '__main__':
    frontend_bp.run(debug=True)
