# Task Manager RL Environment

## Overview
This project implements a simple reinforcement learning environment where an agent completes tasks.

## Features
- 3 difficulty levels: easy, medium, hard
- Reward-based task completion
- Simple and interpretable state

## Files
- env/environment.py → core environment
- inference.py → runs environment
- openenv.yaml → configuration

## How to Run
```bash
python inference.py

update trigger

---
title: Task Manager Env
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: docker
app_file: inference.py
pinned: false
---

# Task Manager RL Environment

## Overview
This environment simulates a real-world task management system where an AI agent must complete daily tasks such as handling emails, attending meetings, and coding tasks.

It is designed to evaluate how effectively an agent can prioritize and complete tasks with increasing difficulty.

---

## Real-World Motivation
Task management is a fundamental human activity in professional environments. This environment models a simplified version of real-world workflows, making it useful for evaluating AI agents in productivity, planning, and sequential decision-making scenarios.

---

## Action Space
The agent can take the following actions:

- `"email"` → Complete email-related tasks  
- `"meeting"` → Attend scheduled meetings  
- `"code"` → Complete coding tasks  

Each action corresponds to completing a specific task.

---

## Observation Space
The environment returns a dictionary representing the current state:

```json
{
  "remaining_tasks": [...],
  "completed_tasks": [...]
}
---

## Tasks & Difficulty Levels

### Easy
- Tasks: ["email"]

### Medium
- Tasks: ["email", "meeting"]

### Hard
- Tasks: ["email", "meeting", "code"]

---

## Reward Function

- +1 → Correct task completion  
- -0.5 → Incorrect action  
- +2 → Bonus for completing all tasks  

---

## Scoring System

Score is calculated as:

score = completed_tasks / total_tasks

Range:
- 0.0 → No progress  
- 1.0 → All tasks completed  

Example:
- 1/3 → 0.33  
- 2/3 → 0.67  
- 3/3 → 1.0  

---

## How to Run

```bash
python inference.py

[START] task=TaskManager env=hard model=dummy-model
[STEP] step=1 action=email reward=1.00 done=False error=null
[STEP] step=2 action=meeting reward=1.00 done=False error=null
[STEP] step=3 action=code reward=3.00 done=True error=null
[END] success=True steps=3 score=1.00 rewards=5.00

update trigger