from dataclasses import dataclass, field


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
                    name="Greek yoghurt bowl",
                    meal_type="breakfast",
                    food_items=[
                        {
                            "name": "Greek yoghurt, berries and chia seeds",
                            "calories": 330,
                            "protein": 28,
                            "carbs": 34,
                            "fat": 9
                        }
                    ]
                ),
                Meal(
                    name="Chicken salad",
                    meal_type="lunch",
                    food_items=[
                        {
                            "name": "Chicken breast salad with avocado",
                            "calories": 450,
                            "protein": 42,
                            "carbs": 22,
                            "fat": 20
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
                    name="Protein oats",
                    meal_type="breakfast",
                    food_items=[
                        {
                            "name": "Oats, banana and protein powder",
                            "calories": 650,
                            "protein": 42,
                            "carbs": 78,
                            "fat": 20
                        }
                    ]
                ),
                Meal(
                    name="Chicken rice bowl",
                    meal_type="lunch",
                    food_items=[
                        {
                            "name": "Chicken, rice and vegetables",
                            "calories": 720,
                            "protein": 55,
                            "carbs": 85,
                            "fat": 14
                        }
                    ]
                )
            ]
        )

    return MealPlan(
        title="Maintenance Meal Plan",
        goal="maintenance",
        meals=[
            Meal(
                name="Balanced eggs on toast",
                meal_type="breakfast",
                food_items=[
                    {
                        "name": "Eggs, toast and fruit",
                        "calories": 480,
                        "protein": 26,
                        "carbs": 48,
                        "fat": 18
                    }
                ]
            )
        ]
    )






if __name__ == "__main__":
    breakfast = Meal(
        name="Protein oats",
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
                        "name": "Protein powder",
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