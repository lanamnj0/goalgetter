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
        """
        Initialising function.
        This contains the API url with headers. 
        The key is stored in .env as this must be secure
        but is retrieved using os.getenv. 
        """
        self.base_url = "https://edb-with-videos-and-images-by-ascendapi.p.rapidapi.com/api/v1"
        self.headers = {
            'Content-Type': "application/json", 
            'X-RapidAPI-Host': "edb-with-videos-and-images-by-ascendapi.p.rapidapi.com", 
            'X-RapidAPI-Key': os.getenv("RAPIDAPI_KEY"), 
        }

    def search_by_body_part(self, body_part, limit=15):
        """
        Search exercise by target body part e.g. chest.
        Comma-separated for multiple body parts e.g. Chest, Shoulers

        This should return:
        ExerciseID, Exercise name, target muscles, secondary muscles,
        image url, equipment needed and instructions for the selected body part. 

        Request: "GET", "/api/v1/bodyparts"
        """
        url = f"{self.base_url}/exercises"

        params = {
            "bodyParts": body_part,
            "limit": limit 
        }

        response = requests.get(
            url, 
            headers=self.headers, 
            params=params
            )

        response.raise_for_status()

        # the API filters the data
        # this will just return the data. 
        data = response.json()["data"]
    
        # filter in Python
        return [
            exercise for exercise in data
            if body_part.upper() in exercise["bodyParts"]
        ][:limit]


    def search_by_target_muscle(self, targetMuscles):
        pass

    def search_by_name(self, name):
        pass

    def search_by_equipment(self, equipments):
        pass 

    def get_exercise_details(self, exerciseId): 
        pass 

    def _format_exercise(self, exercise):
        # """
        # To make the format look pretty + easier to use later.
        # """
        # return {
        #     "id": exercise.get("id"), 

        # }
        pass 
    
