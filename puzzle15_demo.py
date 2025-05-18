#!/usr/bin/env python3
import time
import random
import numpy as np
import gym
from puzzle15Gym.puzzle15_env import Puzzle15Env

def main():
    # Initialize the environment
    env = gym.make('Puzzle3x3Fixed-v0')
    
    # Reset the environment
    observation, info = env.reset()
    
    # Render the initial state
    env.render()
    time.sleep(0.5)  # Pause a bit longer at the start
    
    print("Starting random walk demonstration (100 moves)...")
    
    # Perform 100 random moves
    for i in range(100):
        # Get valid actions
        valid_actions = info["valid_actions"]
        
        if not valid_actions:
            print("No valid actions available. Resetting the environment.")
            observation, info = env.reset()
            continue
        
        # Choose a random valid action
        action = random.choice(valid_actions)
        
        # Take the action
        observation, reward, done, truncated, info = env.step(action)
        
        # Print information
        print(f"Move {i+1}/100 - Action: {action}, Reward: {reward}, Done: {done}")
        
        # Render the new state
        env.render()
        
        # Sleep to slow down the visualization
        time.sleep(0.1)
        
        # If puzzle is solved, reset it
        if done:
            print("Puzzle solved! Resetting the environment.")
            observation, info = env.reset()
    
    # Clean up
    env.close()
    print("Demonstration complete.")

if __name__ == "__main__":
    main() 