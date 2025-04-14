import unittest
import numpy as np
from Puzzle15Gym.puzzle15_env import Puzzle15Env

class TestPuzzle15Env(unittest.TestCase):
    def setUp(self):
        """Set up a test environment before each test."""
        # Use a known 3x3 puzzle state for testing
        # This is a specific configuration with the blank tile in the middle
        self.test_puzzle = "1 2 3|4 -1 5|6 7 8"
        self.env = Puzzle15Env(height=3, width=3, custom_puzzle=self.test_puzzle)
        self.initial_obs, _ = self.env.reset()
    
    
    def test_reset(self):
        """Test environment reset functionality."""
        
        # Make some moves
        self.env.step(0)  # up
        
        # Reset and verify we get back to initial state
        new_obs, _ = self.env.reset()
        np.testing.assert_array_equal(self.initial_obs, new_obs)
    
    def test_step_valid_moves(self):
        """Test step functionality with valid moves."""
        # Test move up
        obs, reward, done, _, _ = self.env.step(0)
        expected_grid = np.array([1, -1, 3, 4, 2, 5, 6, 7, 8])
        np.testing.assert_array_equal(obs, expected_grid)
        self.assertEqual(reward, -1)
        self.assertFalse(done)

        # Test move right
        self.env.reset()
        obs, reward, done, _, _ = self.env.step(1)
        expected_grid = np.array([1, 2, 3, 4, 5, -1, 6, 7, 8])
        np.testing.assert_array_equal(obs, expected_grid)
        self.assertEqual(reward, -1)
        self.assertFalse(done)

        # Test move down
        self.env.reset()
        obs, reward, done, _, _ = self.env.step(2)
        expected_grid = np.array([1, 2, 3, 4, 7, 5, 6, -1, 8])
        np.testing.assert_array_equal(obs, expected_grid)
        self.assertEqual(reward, -1)
        self.assertFalse(done)

        # Test move left
        self.env.reset()
        obs, reward, done, _, _ = self.env.step(3)
        expected_grid = np.array([1, 2, 3, -1, 4, 5, 6, 7, 8])
        np.testing.assert_array_equal(obs, expected_grid)
        self.assertEqual(reward, -1)
        self.assertFalse(done)
    
    def test_step_invalid_move(self):
        """Test step functionality with invalid moves."""
        self.env.step(0)
        obs, reward, done, _, _ = self.env.step(0)
        self.assertEqual(reward, -2)
        self.assertFalse(done)

        np.testing.assert_array_equal(obs, np.array([ 1, -1,  3,  4,  2,  5,  6,  7,  8]))
    
    def test_is_action_valid(self):
        """Test action validation with 3x3 puzzle."""
        # In initial state (blank in middle), all moves are valid
        self.assertTrue(self.env.is_action_valid(0))   # up
        self.assertTrue(self.env.is_action_valid(1))   # right
        self.assertTrue(self.env.is_action_valid(2))   # down
        self.assertTrue(self.env.is_action_valid(3))   # left
        
        # Move blank up
        self.env.step(0)

        # Now only 'down' and 'left' are valid
        self.assertFalse(self.env.is_action_valid(0))  # up
        self.assertTrue(self.env.is_action_valid(1))  # right
        self.assertTrue(self.env.is_action_valid(2))   # down
        self.assertTrue(self.env.is_action_valid(3))   # left

        # Move blank left
        self.env.step(3)

        # Now only 'down' and 'right' are valid
        self.assertFalse(self.env.is_action_valid(0))  # up
        self.assertTrue(self.env.is_action_valid(1))   # right
        self.assertTrue(self.env.is_action_valid(2))   # down
        self.assertFalse(self.env.is_action_valid(3))  # left
    
    def test_solved_state(self):
        """Test solved state detection with 3x3 puzzle."""
        # Create a solved puzzle
        solved_puzzle = "1 2 3|4 5 6|7 -1 8"
        env = Puzzle15Env(height=3, width=3, custom_puzzle=solved_puzzle)
        
        # Verify it's solved
        obs, reward, done, _, _ = env.step(1)  # Any move
        self.assertTrue(done)
        self.assertEqual(reward, 0)

if __name__ == '__main__':
    unittest.main() 