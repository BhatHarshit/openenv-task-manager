from env.environment import TaskEnv

def run():
    print("[START]")

    env = TaskEnv()
    state = env.reset("hard")

    actions = ["email", "meeting", "code"]

    for action in actions:
        state, reward, done, _ = env.step(action)
        print(f"[STEP] action={action}, reward={reward}, done={done}")

    print("[END]")


if __name__ == "__main__":
    run()   