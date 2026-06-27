# GoalGetter Fitness Tracker - ReadME (Setup and Run Guide)

## Project Overview

GoalGetter is a fitness tracking application designed to help users monitor their fitness journey
Users can log workouts, track exercises, record meals and set personal fitness goals
The application aims to provide a simple and organised way to manage health and fitness progress

## Technologies used

- Python
- Flask
- MySQL
- DBeaver
- Git/GitHub
- ExerciseDB API

### Group Members

- Tosin
- Shalesa
- Lana
- Adeyosola
- Neha
- Thelma

## Features

- Create and manage a user profile
- Log workouts and track exercise activity
- Search for exercises using ExerciseDB
- Set and moitor fitness goals
  Track meals and calories intake
- View workout history
- Store fitness data for future reference

## Prerequisites

Before running this project, ensure the following software is installed:

- Python 3.11 or later
- MySQL Server
- DBeaver (or another MySQL client)
- Git
- pip (Python package manager)

## Clone the Repository

Clone the repository and navigate into the project folder.

```python
git clone https://github.com/Tosino97/CFG-Group-Project.git
```

## Install Dependencies

Install the required Python packages:

```python
pip install -r requirements.txt
```

If you don't already have python-dotenv installed, run:

```python
pip install python-dotenv
```

## Database Setup

1. Install MySQL and DBeaver.
2. Open DBeaver and connect to your local MySQL server.
3. Open `goalgetter_schema.sql`.
4. Execute the script to create the GoalGetter database and tables.
5. Open `sample_data.sql`.
6. Execute the script to populate the database with sample records.
7. Refresh the database navigator to confirm that all tables have been created successfully

## ExerciseDB API Setup

The Exercise Search feature uses ExerciseDB API hosted on RapidAPI. A personal RapidAPI key is required to access this functionality.

### 1. Create a RapidAPI Account.

Visit: https://rapidapi.com/ascendapi/api/edb-with-videos-and-images-by-ascendapi

1. Create a free RapidAPI account or sign in if you already have an account.
2. Subscribe to the Free plan (or another plan if you prefer another subscription).

### 2. Obtain your API Key

After subscribing: 

1. Click on MCP Playground to locate the API key 
2. Open the App section of the API page.
3. Locate your X-RapidAPI-Key (this must be kept a secret). 
4. Copy the key. 

### 3. Create a `.env` File

Create a `.env` file in the root project directory.

Add your RapidAPI key replacing the placeholder:

`RAPIDAPI_KEY=your_rapidapi_key_here`

Example:

`RAPIDAPI_KEY=1234567890abcdefghijklmnopqrstuvwxyz`

The `.env` file should not be committed to GitHub and should be listed in `.gitignore`.

### API Documentation

For the most up-to-date API endpoints and documentation, refer to the official AscendAPI documentation:

<https://docs.ascendapi.com/>

To use the API in this project, subscribe to the API through RapidAPI to obtain your API key.

## Running the application 

### Start MySQL

### Run `python app.py`

From the project root directory, run:
`python app.py`

### Open the Flask URL

The Flask development server should start and display something similar to:

```python
Running on http://127.0.0.1:5000
```

Open the URL in your browser.

## Using the application

### Register/ login (Shalesa)

### Manage workouts (Thelma)

- This application manages workouts using the full CRUD flask routes.
- Can create, read, update and delete workouts. These routes handle user requests, interact with the database and ensure workout data can be managed through this application.
- The application has a workout history endpoint where users can receive all past workouts. This allows the user to see their fitness journey details and progress such as when the user worked out and burned the most calories.

### Search exercises

The application integrates with ExerciseDB API to search for exercises.

Example routes:

Search by body part:

`http://127.0.0.1:5000/exercises?body_part=CHEST`

Search by equipment:

`http://127.0.0.1:5000/exercises?equipment=DUMBBELL`

Search by target muscle:

`http://127.0.0.1:5000/exercises?muscle=QUADRICEPS`

Search by exercise name:

`http://127.0.0.1:5000/exercises?name=bench`

Search by exercise type:

`http://127.0.0.1:5000/exercises?exercise_type=STRENGTH`

The application displays exercise cards showing:

- Exercise name
- Exercise type
- Body part
- Target muscle
- Equipment
- Exercise image

This image below shows you an example of the exercise cards:

![sample-img](sample-img.png)

### Create meal plans (Yosola)

### Dashboard/ progress (Neha)

#### Frontend & Backend Setup

This section covers the implementation of the dashboard and calendar components of the application.

#### Files Implemented

##### Frontend:

- `frontend.py` - Flask frontend routes using mocked data for UI demonstration.
- `frontend_blueprinting.py` - Initial Flask Blueprint implementation to support modular routing.
- `layout.html` - Base HTML template providing global structure and sidebar navigation.
- `dashboard.html` - Dashboard interface featuring widget statistics, and a Calendar UI
- `workouts.html` - Workouts page with dropdown filtering to display mock data
- `meals_and_recipes.html` - Recipe interface displaying mock API response cards
- `history.html` - Past history user workout data rendered in a structured table
- `settings.html` - User settings interface implementation
- `support.html` - Support form allowing users to submit issues or bugs reports.
- `logout.html` - Logout route and interface element.

##### Backend:

- `dashboard_logic.py` - Dashboard widget calculation logic.
- `calendar_logic.py` - Calendar scheduling logic using a Breadth First Search (BFS) implementation.

##### Unit Test:

- `test_dashboard_logic.py` - Unit tests for dashboard calculation logic
- `test_calendar_logic.py` - Unit tests for calendar scheduling logic

##### Running the frontend UI application

- Install project dependencies
- Run the Flask application (e.g. `python frontend.py`)
- Open the application in a web browser
- Navigate using the sidebar to access dashboard, calendar, workouts, meals, history, settings, and support pages

##### Notes

- The frontend demonstrates a Minimum Viable Product (MVP) using mocked data for demonstration purposes.
- Dashboard widget values and calendar events are also powered by mock data to demonstrate frontend functionality.
- Unit tests are provided for the dashboard and calendar backend modules to verify the isolated logic of both components.

## Running Unit Tests

Run all project tests from the root project directory:

```python
python -m unittest discover -s tests
```

If successful, the output should look something like:

```python

Ran X tests in 0.XXXs

OK
```

## Troubleshooting

### Database connection fails

### Exercise API returns an authentication error

- Confirm that a valid `RAPIDAPI_KEY` has been added to the `.env` file
- Restart the Flask application after updating the `.env` file

## Future Improvements

- Progress charts and analytics
- Improved meal planning features
- Additional fitness APIs
- Mobile application support
