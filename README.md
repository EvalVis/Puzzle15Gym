# Puzzle15Gym

A Gym environment for the 15-puzzle game.

## Description

Puzzle15Gym is a custom OpenAI Gym environment for the 15-puzzle game. The environment allows reinforcement learning agents to solve the puzzle by moving tiles.

## Installation

```bash
pip install .
```

## Usage

```python
from Puzzle15Gym.puzzle15_env import Puzzle15Env

env = Puzzle15Env(3, 3)

# Reset the environment
observation, _ = env.reset()

# Take a step
action = env.action_space.sample()  # Random action
observation, reward, done, info = env.step(action)

# Render the environment
env.render()

# Close the environment
env.close()
```

## Environment Details

- **Action Space**: Discrete(4) - 0: up, 1: right, 2: down, 3: left
- **Observation Space**: Box(-1, height*width-1, (height*width,), int32) - Flattened grid of numbers
- **Reward**: 1 if the puzzle is solved, 0 if not, -2 if invalid move
- **Done**: True if the puzzle is solved, False otherwise