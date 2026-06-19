"""
This class will communicate with ExerciseAPI for requests. 

It will search exercises by muscle group, name, or equipment. 
It will also view exercise details. 
"""
# template requests 
# https://rapidapi.com/ascendapi/api/edb-with-videos-and-images-by-ascendapi/playground/apiendpoint_667c8fb1-a826-47a8-b10c-d23c3b54d968

import os
import requests 
from dotenv import load_dotenv

# this will read the RAPIDAPI-KEY
# which is found in .env (hidden in gitignore)
load_dotenv() 

# creating the class
class ExerciseAPI: 

    # creating a skeleton structure of the different files.. 
    # first the initialising structure
    def __init__(self): 
        self.url = "https://edb-with-videos-and-images-by-ascendapi.p.rapidapi.com/api/v1/bodyparts"
        self.headers = {

        }

    def search_by_muscle_group(self, muscle):
        pass 

    def search_by_name(self, name):
        pass

    def search_by_equipment(self, equipment):
        pass 

    def get_exercise_details(self, exercise_id): 
        pass 

