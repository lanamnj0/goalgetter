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
        image url, and equipment needed for the selected body part. 

        Request: "GET", "/api/v1/exercises" with bodyParts query param
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
        return [self._format_exercise(exercise) for exercise in data] 
        #     self._format_exercise(exercise)
        #     exercise for exercise in data
        #     if body_part.upper() in exercise["bodyParts"]
        # ][:limit]


    def search_by_target_muscle(self, target_muscle, limit=15 ):
        """
        Search exercise by target muscle. 

        This should return:
        ExerciseID, Exercise name, body part, secondary muscles,
        image url and equipment needed for the selected target muscle. 

        Request: "GET", "/api/v1/exercises" with targetMuscles query param
        """
        url = f"{self.base_url}/exercises"

        params = {
            "targetMuscle": target_muscle,
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
        return [self._format_exercise(exercise) for exercise in data] 

    def search_by_name(self, name, limit = 15):
        """
        Search exercise by exercise name. 

        This should return:
        ExerciseID, body part, target muscle, secondary muscles,
        image url and equipment needed for the selected exercise name. 

        Request: "GET", "/api/v1/exercises"
        """
        url = f"{self.base_url}/exercises"

        params = {
            "name": name,
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
        return [self._format_exercise(exercise) for exercise in data]

    def search_by_equipment(self, equipments, limit=15):
        """
        Search exercise by equipment, e.g. body weight. 

        This should return:
        ExerciseID, Exercise name, body part, target muscle, secondary muscles
        and image url for the selected equipment

        Request: "GET", "/api/v1/exercises" with equipments query param
        """
        url = f"{self.base_url}/exercises"

        params = {
            "equipments": equipments,
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
        return [self._format_exercise(exercise) for exercise in data] 

    def get_exercise_details(self, exerciseId): 
        """
        Getting full exercise details for a single exercise by its ID
        Request: "GET", "api/v1/exercises/{exerciseId}
        """
        url = f"{self.base_url}/exercises/{exerciseId}"

        response = requests.get(
            url, 
            headers=self.headers
            )
    
        response.raise_for_status()

        return self._format_exercise(response.json()["data"])

    def _format_exercise(self, exercise):
        # """
        # To make the format look pretty + easier to use later.
        return {
            "exerciseId: ", exercise.get("exerciseId"), 
            "name: ", exercise.get("name"),
            "exerciseType: ", exercise.get("exerciseType"),
            "imageUrl: ", exercise.get("imageUrl"),
            "targetMuscles: ", exercise.get("targetMuscles"),
            "bodyParts: ", exercise.get("bodyParts"),
            "equipments: ", exercise.get("equipments"),
            "secondaryMuscles: ", exercise.get("secondaryMuscles")

        }
        
    
