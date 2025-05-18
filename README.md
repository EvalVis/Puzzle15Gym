# Puzzle15Gym

[![codecov](https://codecov.io/gh/EvalVis/Puzzle15Gym/branch/main/graph/badge.svg)](https://codecov.io/gh/EvalVis/Puzzle15Gym)
[![PyPI version](https://badge.fury.io/py/puzzle15Gym.svg)](https://pypi.org/project/puzzle15Gym/)

A custom AI Gym environment for the 15-puzzle game: https://en.wikipedia.org/wiki/15_puzzle.

The blank space is represented by `-1`.

Library used: [![GitHub](https://img.shields.io/badge/GitHub-EvalVis/Puzzle15-black?style=flat&logo=github)](https://github.com/EvalVis/Puzzle15).

## Usage

### Initiating the env via gym

```python
import gym
import puzzle15Gym

env_3x3_random = gym.make('Puzzle3x3Random-v0')
env_3x3_fixed = gym.make('Puzzle3x3Fixed-v0')

env_4x4_random = gym.make('Puzzle4x4Random-v0')
env_4x4_fixed = gym.make('Puzzle4x4Fixed-v0')

env_5x5_random = gym.make('Puzzle5x5Random-v0')
env_5x5_fixed = gym.make('Puzzle5x5Fixed-v0')
```

### Initiating the env directly

```python
from puzzle15Gym import Puzzle15Env

env_random = Puzzle15Env(height=4, width=4)
env_random = Puzzle15Env(custom_puzzle="2 8 6|7 1 3|-1 5 4")
```

```python
env_3x3_random = gym.make('Puzzle3x3Random-v0')

# Reset the environment
observation, info = env_3x3.reset()

# Take a step
action = env_3x3.action_space.sample()
observation, reward, done, truncated, info = env_3x3.step(action)

# Render the environment. The only render mode is 'human' which renders visual output.
env_3x3.render()

# Close the environment
env_3x3.close()
```

## Environment Details

- **Action Space**: Discrete(4) - `0`: up, `1`: right, `2`: down, `3`: left.
- **Observation Space**: `Box(-1, height*width-1, (height*width), int32)`.
Contains unique values from `-1` to (`width * height - 1`), excluding `0`.
- **Reward**: `1` if the puzzle is solved, `0` if not, `-2` if invalid move.
- **Done**: `True` if the puzzle is solved, `False` otherwise.