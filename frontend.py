from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)

# This is the dashboard homepage
@app.route('/')
def index():
    return render_template('calendar.html')

@app.route('/workouts')
def workouts():
    return render_template('workouts.html')

@app.route('/meals_and_recipes')
def meals_and_recipes():
    return render_template('meals_and_recipes.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/support', methods=['GET', 'POST'])
def support():
    if request.method == 'POST' and 'name' in request.form and 'email' in request.form and 'message' in request.form and 'support_category' in request.form:  # issue type not included in this yet
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        selected_issue = request.form.get('support_category')

        # These fields need to be saved into a support table within MySQL
        # Also need case handling
        counter = 0
        support_tickets = []
        if name and email and message:
            for i in support_tickets:
                counter += 1

        # flash() entirely relies on browser Sessions and Cookies not MySQL
        flash(f"Thank you! Your support ticket #{counter} has been submitted! A team member will email your shortly")
        print(f"User selected: {selected_issue}")


    return render_template('support.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

if __name__ == '__main__':
    app.run(debug=True)

# To run file: python frontend.py