class WorkoutNode:
    def __init__(self, workout):
        self.workout = workout
        self.next = None

class WorkoutHistoryList:
    def __init__(self):
        self.head = None


def add_workout(self, workout):
    new_node = WorkoutNode(workout)

    if self.head is None:
        self.head = new_node
        return

    current = self.head

    while current.next:
        current = current.next

    current.next = new_node

    def get_workouts(self):
        workouts = []
        current = self.head
        while current:
            workouts.append(current.workout)
            current = current.next

            return workouts