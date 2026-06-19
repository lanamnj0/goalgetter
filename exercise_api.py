"""
This class will communicate with ExerciseAPI for requests. 

It will search exercises by muscle group, name, or equipment. 
It will also view exercise details. 
"""

import requests 

# creating the class
class ExerciseAPI: 

    # creating a skeleton structure of the different files.. 
    # first the initialising structure
    def __init__(self): 
        self.url = ...
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

