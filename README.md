# Puzzle15Gym

A Gym environment for the 15-puzzle game.

## Description

Puzzle15Gym is a custom OpenAI Gym environment for the 15-puzzle game. The environment allows reinforcement learning agents to solve the puzzle by moving tiles.

## Installation

```bash
pip install .
```

## Usage

### Using registered environments

```python
import gym
import Puzzle15Gym  # This automatically registers the environments

# Create a 3x3 puzzle
env_3x3 = gym.make('Puzzle3x3Random-v0')

# Create a 4x4 puzzle (standard 15-puzzle)
env_4x4 = gym.make('Puzzle4x4Random-v0')

# Create a 5x5 puzzle
env_5x5 = gym.make('Puzzle5x5Random-v0')

# Reset the environment
observation, info = env_3x3.reset()

# Take a step
action = env_3x3.action_space.sample()  # Random action
observation, reward, done, truncated, info = env_3x3.step(action)

# Render the environment
env_3x3.render()

# Close the environment
env_3x3.close()
```

### Using the environment directly

```python
from Puzzle15Gym import Puzzle15Env

# Create a custom-sized puzzle
env = Puzzle15Env(height=4, width=4)

# Reset the environment
observation, info = env.reset()

# Take a step
action = env.action_space.sample()  # Random action
observation, reward, done, truncated, info = env.step(action)

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