from typing import List


class TaskEnv:
    def __init__(self):
        self.tasks: List[str] = []
        self.completed: List[str] = []
        self.total_tasks: int = 0

    def reset(self, difficulty: str = "easy"):
        if difficulty == "easy":
            self.tasks = ["email"]
        elif difficulty == "medium":
            self.tasks = ["email", "meeting"]
        elif difficulty == "hard":
            self.tasks = ["email", "meeting", "code"]
        else:
            raise ValueError(f"Invalid difficulty: {difficulty}")

        self.completed = []
        self.total_tasks = len(self.tasks)
        return self._get_state()

    def step(self, action: str):
        reward = 0

        if action in self.tasks:
            self.tasks.remove(action)
            self.completed.append(action)
            reward = 1
        else:
            reward = -0.5

        done = len(self.tasks) == 0

        if done:
            reward += 2

        score = len(self.completed) / self.total_tasks if self.total_tasks > 0 else 0.0

        return self._get_state(), reward, done, {"score": round(score, 2)}

    def _get_state(self):
        return {
            "remaining_tasks": self.tasks.copy(),
            "completed_tasks": self.completed.copy()
        }

    def state(self):
        return self._get_state()