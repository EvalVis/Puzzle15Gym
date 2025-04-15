from typing import Optional, List

import gym
import numpy as np
from gym import spaces
from puzzle15.puzzle import Puzzle

class Puzzle15Env(gym.Env):
    """
    A Gym environment for the 15-puzzle game.
    
    The environment allows an agent to solve a 15-puzzle by moving tiles.
    The state is represented as a flattened grid of numbers, where -1 represents the blank space.
    The action space is discrete with 4 possible actions: up, right, down, left.
    """
    
    metadata = {'render.modes': ['human', 'rgb_array']}
    
    def __init__(self, height=4, width=4, custom_puzzle=None):
        """
        Initialize the environment.
        
        Args:
            height: The height of the puzzle grid. None if you are using a custom puzzle.
            width: The width of the puzzle grid. None if you are using a custom puzzle.
            custom_puzzle: A string representation of a custom puzzle.
                          Format: "1 2 3 4|5 6 7 8|9 10 11 12|13 14 -1 15"
                          where | separates rows and -1 represents the blank space.
        """
        super(Puzzle15Env, self).__init__()
        
        self._height = height
        self._width = width
        self._custom_puzzle = custom_puzzle
        self._puzzle = None
        self._initial_grid = None  # Store the initial grid state
        self._direction = {
            0: 'up',
            1: 'right',
            2: 'down',
            3: 'left'
        }
        
        # Define action and observation spaces
        self.action_space = spaces.Discrete(4)  # 0: up, 1: right, 2: down, 3: left
        
        # The observation space is a flattened grid of numbers
        self._observation_space = spaces.Box(
            low=-1, 
            high=height*width-1, 
            shape=(height*width,), 
            dtype=np.int32
        )
        
        self.reset()

    def reset(self, *, seed: Optional[int] = None, options: Optional[dict] = None):
        """
        Reset the environment to a new puzzle.
        
        Returns:
            The initial observation and valid actions.
        """
        if self._initial_grid is None:
            if self._custom_puzzle:
                self._puzzle = Puzzle.from_string(self._custom_puzzle)
            else:
                self._puzzle = Puzzle.from_dimensions(self._height, self._width)
        else:
            self._puzzle = Puzzle(self._initial_grid)

        valid_actions = [i for i, direction in self._direction.items() if direction in self._puzzle.possible_moves()]
        
        return self._get_observation(), {"valid_actions": valid_actions}
    
    def step(self, action):
        """
        Take a step in the environment.
        
        Args:
            action: An integer representing the action to take.
                   0: up, 1: right, 2: down, 3: left.
        
        Returns:
            observation: The new observation after taking the action.
            reward: The reward for taking the action.
            done: Whether the episode is done.
            truncated: Whether the episode was truncated.
            info: Additional information including valid actions.
        """
        # Get valid actions
        valid_actions = [i for i, direction in self._direction.items() if direction in self._puzzle.possible_moves()]
        
        # Check if action is valid
        if action not in valid_actions:
            return self._get_observation(), -2, False, False, {"valid_actions": valid_actions}
        
        self._puzzle.move(self._direction[action])
        
        done = self._puzzle.is_solved()
        reward = 0 if done else -1
        
        # Get updated valid actions after the move
        valid_actions = [i for i, direction in self._direction.items() if direction in self._puzzle.possible_moves()]\
            if not done else []
        
        return self._get_observation(), reward, done, False, {"valid_actions": valid_actions}
    
    def _get_observation(self):
        """
        Get the current observation.
        
        Returns:
            A flattened numpy array representing the current state.
        """
        # Flatten the grid
        flat_grid = [
            val 
            for row in self._puzzle.grid() 
            for val in row
        ]
        return np.array(flat_grid, dtype=np.int32)
    
    def render(self, mode='human'):
        """
        Render the environment.
        
        Args:
            mode: The rendering mode. 'human' for console output, 'rgb_array' for image.
        
        Returns:
            If mode is 'rgb_array', returns an RGB array. Otherwise, returns None.
        """
        if mode == 'human':
            print(self._puzzle)
            return None
        else:
            raise NotImplementedError(f"Rendering mode {mode} not implemented.")
        
    def close(self):
        """Clean up environment resources."""
        pass 