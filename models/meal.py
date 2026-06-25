from dataclasses import dataclass, field
from copy import deepcopy


@dataclass
class Meal:
    name: str
    meal_type: str
    food_items: list = field(default_factory=list)

    def calculate_totals(self):
        return calculate_total_nutrition(self.food_items)


@dataclass
class MealPlan:
    title: str
    goal: str
    meals: list = field(default_factory=list)

    def add_meal(self, meal):
        self.meals.append(meal)

    def calculate_totals(self):
        return calculate_total_nutrition(self.meals)


def calculate_total_nutrition(data):
    totals = {
        "calories": 0,
        "protein": 0,
        "carbs": 0,
        "fat": 0
    }

    if data is None:
        return totals

    if isinstance(data, MealPlan):
        return calculate_total_nutrition(data.meals)

    if isinstance(data, Meal):
        return calculate_total_nutrition(data.food_items)

    if isinstance(data, list):
        for item in data:
            item_totals = calculate_total_nutrition(item)
            totals["calories"] += item_totals["calories"]
            totals["protein"] += item_totals["protein"]
            totals["carbs"] += item_totals["carbs"]
            totals["fat"] += item_totals["fat"]
        return totals

    if isinstance(data, dict):
        totals["calories"] += data.get("calories", 0)
        totals["protein"] += data.get("protein", 0)
        totals["carbs"] += data.get("carbs", 0)
        totals["fat"] += data.get("fat", 0)

        if "items" in data:
            nested_totals = calculate_total_nutrition(data["items"])
            totals["calories"] += nested_totals["calories"]
            totals["protein"] += nested_totals["protein"]
            totals["carbs"] += nested_totals["carbs"]
            totals["fat"] += nested_totals["fat"]

        return totals

    return totals


def suggest_meal_plan(goal):
    goal = goal.lower()

    if goal == "weight_loss":
        return MealPlan(
            title="Weight Loss Meal Plan",
            goal="weight_loss",
            meals=[
                Meal(
                    name="Greek Yoghurt Bowl",
                    meal_type="breakfast",
                    food_items=[
                        {
                            "name": "Greek Yoghurt, Berries and Chia Seeds",
                            "calories": 330,
                            "protein": 28,
                            "carbs": 34,
                            "fat": 9
                        }
                    ]
                ),
                Meal(
                    name="Chicken Salad",
                    meal_type="lunch",
                    food_items=[
                        {
                            "name": "Chicken Breast Salad with Avocado",
                            "calories": 450,
                            "protein": 42,
                            "carbs": 22,
                            "fat": 20
                        }
                    ]
                ),
                Meal(
                    name="Grilled Salmon Veg Plate",
                    meal_type="dinner",
                    food_items=[
                        {
                            "name": "Grilled Salmon with Mixed Vegetables and Roasted Sweet Potato",
                            "calories": 520,
                            "protein": 42,
                            "carbs": 35,
                            "fat": 22
                        }
                    ]
                )
            ]
        )

    if goal == "muscle_gain":
        return MealPlan(
            title="Muscle Gain Meal Plan",
            goal="muscle_gain",
            meals=[
                Meal(
                    name="Protein Oats",
                    meal_type="breakfast",
                    food_items=[
                        {
                            "name": "Oats, Banana and Protein Powder",
                            "calories": 650,
                            "protein": 42,
                            "carbs": 78,
                            "fat": 20
                        }
                    ]
                ),
                Meal(
                    name="Chicken Rice Bowl",
                    meal_type="lunch",
                    food_items=[
                        {
                            "name": "Chicken, Rice and Vegetables",
                            "calories": 720,
                            "protein": 55,
                            "carbs": 85,
                            "fat": 14
                        }
                    ]
                ),
                Meal(
                    name="Steak Rice Bowl",
                    meal_type="dinner",
                    food_items=[
                        {
                            "name": "Tender Steak Strips Served with Rice, Peppers, Greens and Garlic Dressing",
                            "calories": 690,
                            "protein": 52,
                            "carbs": 70,
                            "fat": 24
                        }
                    ]
                )
            ]
        )

    return suggest_meal_plan("weight_loss")


def generate_weekly_meal_variations(base_plan, total_days=7, current_day=1, variations=None):
    if variations is None:
        variations = []

    if current_day > total_days:
        return variations

    new_plan = deepcopy(base_plan)
    new_plan.title = f"{base_plan.title} Day {current_day}"

    if len(new_plan.meals) > 0:
        shift = (current_day - 1) % len(new_plan.meals)
        new_plan.meals = new_plan.meals[shift:] + new_plan.meals[:shift]

    variations.append(new_plan)

    return generate_weekly_meal_variations(
        base_plan,
        total_days,
        current_day + 1,
        variations
    )


if __name__ == "__main__":
    breakfast = Meal(
        name="Protein Oats",
        meal_type="breakfast",
        food_items=[
            {
                "name": "Oats",
                "calories": 300,
                "protein": 12,
                "carbs": 45,
                "fat": 8,
                "items": [
                    {
                        "name": "Protein Powder",
                        "calories": 120,
                        "protein": 24,
                        "carbs": 2,
                        "fat": 1
                    }
                ]
            }
        ]
    )

    plan = MealPlan(
        title="Muscle Gain Plan",
        goal="muscle_gain"
    )

    plan.add_meal(breakfast)

    print(plan.calculate_totals())