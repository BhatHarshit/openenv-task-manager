from env.environment import TaskEnv
import os

# ✅ SAFE IMPORT
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except:
    OPENAI_AVAILABLE = False


def run():
    # ✅ ENV VARIABLES
    API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
    API_KEY = os.getenv("API_KEY", "dummy-key")
    MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")

    # ✅ SAFE CLIENT INIT
    client = None
    if OPENAI_AVAILABLE:
        client = OpenAI(
            base_url=API_BASE_URL,
            api_key=API_KEY
        )

    env = TaskEnv()
    state = env.reset("hard")

    total_reward = 0
    steps = 0

    print(f"[START] task=TaskManager env=hard model={MODEL_NAME}")

    done = False

    while not done and steps < 5:
        steps += 1

        error_msg = "null"

        # ✅ SAFE LLM BLOCK
        if OPENAI_AVAILABLE and client:
            try:
                response = client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=[
                        {"role": "system", "content": "You are a task manager agent. Choose one action: email, meeting, code."},
                        {"role": "user", "content": f"Remaining tasks: {state['remaining_tasks']}. What should be done next? Reply with only one word."}
                    ]
                )
                action = response.choices[0].message.content.strip().lower()
            except Exception as e:
                action = "email"
                error_msg = str(e)
        else:
            # ✅ FALLBACK IF OPENAI NOT AVAILABLE
            action = "email"
            error_msg = "openai_not_available"

        # ✅ SAFETY CHECK
        if action not in ["email", "meeting", "code"]:
            action = "email"

        next_state, reward, done, _ = env.step(action)
        total_reward += reward

        print(f"[STEP] step={steps} action={action} reward={reward:.2f} done={str(done).lower()} error={error_msg}")

        state = next_state

    total_tasks = len(state["completed_tasks"]) + len(state["remaining_tasks"])
    score = len(state["completed_tasks"]) / total_tasks if total_tasks > 0 else 1.0

    print(f"[END] success={str(done).lower()} steps={steps} score={score:.2f} rewards={total_reward:.2f}")


if __name__ == "__main__":
    run()