class TaskEnv:
    def __init__(self):
        self.tasks = []
        self.completed = []

    def reset(self, difficulty="easy"):
        if difficulty == "easy":
            self.tasks = ["email"]
        elif difficulty == "medium":
            self.tasks = ["email", "meeting"]
        elif difficulty == "hard":
            self.tasks = ["email", "meeting", "code"]

        self.completed = []

        return self._get_state()

    def step(self, action):
        reward = 0

        if action in self.tasks:
            self.tasks.remove(action)
            self.completed.append(action)
            reward = 1
        else:
            reward = -0.5

        done = len(self.tasks) == 0

        if done:
            reward += 2  # bonus for finishing all tasks

        return self._get_state(), reward, done, {}

    def _get_state(self):
        return {
            "remaining_tasks": self.tasks,
            "completed_tasks": self.completed
        }