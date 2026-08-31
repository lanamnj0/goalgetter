"""Frontend routes for GoalGetter's portfolio demonstration pages."""

import time
from flask import Blueprint, flash, redirect, render_template, request, url_for

SAMPLE_WORKOUTS = [
    {
        "date": "2026-06-18",
        "exercise": "Arm Day",
        "duration": 35,
        "calories": 240,
    },
    {
        "date": "2026-06-20",
        "exercise": "Upper Body",
        "duration": 40,
        "calories": 280,
    },
    {
        "date": "2026-06-22",
        "exercise": "Leg Day",
        "duration": 45,
        "calories": 320,
    },
]

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

@frontend_bp.route('/meals_and_recipes')
def meals_and_recipes():
    # Demo meal data used by the legacy recipe gallery.
    meals = [
        {
            'id': 1,
            'name': 'Greek Salad',
            'description': 'Fresh vegetables, feta cheese, olives, and a light dressing.',
            'image_url': '../static/greek-salad-test-image.jpeg',
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
    ]
    return render_template('meals_and_recipes.html', meals=meals)

@frontend_bp.route('/history')
def history():
    return render_template(
        'history.html',
        workouts=reversed(SAMPLE_WORKOUTS),
        )

@frontend_bp.route('/support', methods=['GET', 'POST'])
def support():
    if request.method == 'POST':
        # Grabs all data from form
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        selected_issue = request.form.get('support_category')

        # Validate that every required field was submitted.
        if name and email and message and selected_issue:
            # Generating a fake ticket number using time module, unique number every second
            fake_ticket_number = int(time.time()) # Do not want a float

            flash(
                f"Thank you {name}! Your support ticket #{fake_ticket_number} "
                "has been submitted. We will email you shortly.",
                "success",
            )

        else: # If some or any of the fields are missing from the form
            flash("Please fill out all the required fields before submitting", "info")

    return render_template('support.html')

@frontend_bp.get('/settings')
def settings():
    return render_template('settings.html')

@frontend_bp.get('/logout')
def logout():
    flash("Authentication is not enabled in this demo, so there is no active session to end.", "info")
    return redirect(url_for('login'))
