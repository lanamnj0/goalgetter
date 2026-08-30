"""
frontend.py

This file provides the Flask routes used to demonstrate the application's Minimum Viable Product (MVP) frontend. The routes currently utilise mocked backend data to showcase the intended user interface and frontend functionality prior to full backend integration.

For an initial attempt at modularising the application's routing using Flask Blueprints, please refer to frontend_blueprinting.py. This file demonstrates the proposed structure for integrating frontend routes with the team's backend components as development progressed.
"""
import os 
from app import app

if __name__ == '__main__':
   app.run(debug=os.getenv("FLASK_DEBUG", "false").lower() == "true",
           port=int(os.getenv("PORT", "5000")))
