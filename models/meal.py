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

def get_weekly_meal_pool(goal):
    goal = goal.lower()

    if goal == "muscle_gain":
        return {
            "breakfast": [
                Meal("Protein Oats", "breakfast", [
                    {"name": "Oats, Banana and Protein Powder", "calories": 650, "protein": 42, "carbs": 78, "fat": 20}
                ]),
                Meal("Egg and Avocado Toast", "breakfast", [
                    {"name": "Wholemeal Toast, Eggs and Avocado", "calories": 580, "protein": 32, "carbs": 48, "fat": 28}
                ]),
                Meal("Greek Yoghurt Protein Bowl", "breakfast", [
                    {"name": "Greek Yoghurt, Granola, Berries and Honey", "calories": 520, "protein": 35, "carbs": 62, "fat": 14}
                ]),
            ],
            "lunch": [
                Meal("Chicken Rice Bowl", "lunch", [
                    {"name": "Chicken, Rice and Vegetables", "calories": 720, "protein": 55, "carbs": 85, "fat": 14}
                ]),
                Meal("Turkey Pasta Bowl", "lunch", [
                    {"name": "Turkey Mince, Pasta and Tomato Sauce", "calories": 690, "protein": 48, "carbs": 82, "fat": 16}
                ]),
                Meal("Tuna Sweet Potato Bowl", "lunch", [
                    {"name": "Tuna, Sweet Potato, Sweetcorn and Salad", "calories": 610, "protein": 45, "carbs": 70, "fat": 13}
                ]),
            ],
            "dinner": [
                Meal("Steak Rice Bowl", "dinner", [
                    {"name": "Tender Steak Strips Served with Rice, Peppers, Greens and Garlic Dressing", "calories": 690, "protein": 52, "carbs": 70, "fat": 24}
                ]),
                Meal("Salmon Potato Plate", "dinner", [
                    {"name": "Salmon, Baby Potatoes and Green Vegetables", "calories": 680, "protein": 46, "carbs": 58, "fat": 30}
                ]),
                Meal("Chicken Couscous Bowl", "dinner", [
                    {"name": "Chicken Breast, Couscous and Roasted Vegetables", "calories": 640, "protein": 50, "carbs": 66, "fat": 18}
                ]),
            ],
        }

    return {
        "breakfast": [
            Meal("Greek Yoghurt Bowl", "breakfast", [
                {"name": "Greek Yoghurt, Berries and Chia Seeds", "calories": 330, "protein": 28, "carbs": 34, "fat": 9}
            ]),
            Meal("Berry Yoghurt Bowl", "breakfast", [
                {"name": "Oats, Berries and Low Fat Yoghurt", "calories": 360, "protein": 22, "carbs": 48, "fat": 8}
            ]),
            Meal("Avocado Egg Toast", "breakfast", [
                {"name": "Egg, Avocado and Wholemeal Toast", "calories": 390, "protein": 24, "carbs": 32, "fat": 18}
            ]),
        ],
        "lunch": [
            Meal("Chicken Salad", "lunch", [
                {"name": "Chicken Breast Salad with Avocado", "calories": 450, "protein": 42, "carbs": 22, "fat": 20}
            ]),
            Meal("Prawn Quinoa Bowl", "lunch", [
                {"name": "Prawns, Quinoa, Mango and Salad", "calories": 430, "protein": 36, "carbs": 45, "fat": 11}
            ]),
            Meal("Falafel Hummus Plate", "lunch", [
                {"name": "Falafel, Hummus, Salad and Flatbread", "calories": 470, "protein": 24, "carbs": 52, "fat": 18}
            ]),
        ],
        "dinner": [
            Meal("Grilled Salmon Veg Plate", "dinner", [
                {"name": "Grilled Salmon, Mixed Vegetables and Roasted Sweet Potato", "calories": 520, "protein": 42, "carbs": 35, "fat": 22}
            ]),
            Meal("Turkey Courgette Pasta", "dinner", [
                {"name": "Turkey Mince, Courgette and Light Tomato Pasta", "calories": 510, "protein": 40, "carbs": 48, "fat": 14}
            ]),
            Meal("Loaded Sweet Potato", "dinner", [
                {"name": "Sweet Potato, Beans, Avocado and Salad", "calories": 480, "protein": 22, "carbs": 62, "fat": 16}
            ]),
        ],
    }

def generate_weekly_meal_variations(base_plan, total_days=7, current_day=1, variations=None):
    if variations is None:
        variations = []

    if current_day > total_days:
        return variations

    meal_pool = get_weekly_meal_pool(base_plan.goal)

    breakfast_options = meal_pool["breakfast"]
    lunch_options = meal_pool["lunch"]
    dinner_options = meal_pool["dinner"]

    breakfast = deepcopy(breakfast_options[(current_day - 1) % len(breakfast_options)])
    lunch = deepcopy(lunch_options[(current_day - 1) % len(lunch_options)])
    dinner = deepcopy(dinner_options[(current_day - 1) % len(dinner_options)])

    daily_plan = MealPlan(
        title=f"{base_plan.title} Day {current_day}",
        goal=base_plan.goal,
        meals=[breakfast, lunch, dinner]
    )

    variations.append(daily_plan)

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