import unittest

from models.meal import Meal, MealPlan, calculate_total_nutrition, suggest_meal_plan


class TestMealModels(unittest.TestCase):

    def test_meal_calculates_totals(self):
        breakfast = Meal(
            name="Protein oats",
            meal_type="breakfast",
            food_items=[
                {
                    "name": "Oats",
                    "calories": 300,
                    "protein": 12,
                    "carbs": 45,
                    "fat": 8
                }
            ]
        )

        totals = breakfast.calculate_totals()

        self.assertEqual(totals["calories"], 300)
        self.assertEqual(totals["protein"], 12)
        self.assertEqual(totals["carbs"], 45)
        self.assertEqual(totals["fat"], 8)

    def test_meal_plan_calculates_totals(self):
        breakfast = Meal(
            name="Protein oats",
            meal_type="breakfast",
            food_items=[
                {
                    "name": "Oats",
                    "calories": 300,
                    "protein": 12,
                    "carbs": 45,
                    "fat": 8
                }
            ]
        )

        lunch = Meal(
            name="Chicken rice bowl",
            meal_type="lunch",
            food_items=[
                {
                    "name": "Chicken and rice",
                    "calories": 600,
                    "protein": 45,
                    "carbs": 70,
                    "fat": 12
                }
            ]
        )

        plan = MealPlan(
            title="Muscle Gain Plan",
            goal="muscle_gain"
        )

        plan.add_meal(breakfast)
        plan.add_meal(lunch)

        totals = plan.calculate_totals()

        self.assertEqual(totals["calories"], 900)
        self.assertEqual(totals["protein"], 57)
        self.assertEqual(totals["carbs"], 115)
        self.assertEqual(totals["fat"], 20)

    def test_recursive_nested_food_items(self):
        food_items = [
            {
                "name": "Oats",
                "calories": 300,
                "protein": 12,
                "carbs": 45,
                "fat": 8,
                "items": [
                    {
                        "name": "Protein powder",
                        "calories": 120,
                        "protein": 24,
                        "carbs": 2,
                        "fat": 1
                    }
                ]
            }
        ]

        totals = calculate_total_nutrition(food_items)

        self.assertEqual(totals["calories"], 420)
        self.assertEqual(totals["protein"], 36)
        self.assertEqual(totals["carbs"], 47)
        self.assertEqual(totals["fat"], 9)

    def test_goal_based_meal_suggestion(self):
        plan = suggest_meal_plan("muscle_gain")

        self.assertEqual(plan.goal, "muscle_gain")
        self.assertEqual(plan.title, "Muscle Gain Meal Plan")
        self.assertGreater(len(plan.meals), 0)
        self.assertGreater(plan.calculate_totals()["calories"], 0)

if __name__ == "__main__":
    unittest.main()