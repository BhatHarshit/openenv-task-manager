from fastapi import FastAPI, Request
from env.environment import TaskEnv

app = FastAPI()
env = TaskEnv()


# ✅ Root check (for HF health)
@app.get("/")
def root():
    return {"status": "running"}


# ✅ RESET endpoint (SAFE for empty body)
@app.post("/reset")
async def reset(request: Request):
    try:
        body = await request.json()
    except:
        body = {}

    difficulty = body.get("difficulty", "easy")

    state = env.reset(difficulty)

    return {
        "state": state
    }


# ✅ STEP endpoint (SAFE for empty body)
@app.post("/step")
async def step(request: Request):
    try:
        body = await request.json()
    except:
        body = {}

    action = body.get("action", None)

    state, reward, done, info = env.step(action)

    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }
def main():
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()