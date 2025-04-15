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
        self.env.step(0)

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
        obs, reward, done, _, info = self.env.step(0)
        self.assertEqual(reward, -2)
        self.assertFalse(done)

        np.testing.assert_array_equal(obs, np.array([ 1, -1,  3,  4,  2,  5,  6,  7,  8]))
    
    def test_valid_actions(self):
        """Test valid actions returned in info dictionary with 3x3 puzzle."""
        obs, _, _, _, info = self.env.step(0)
        np.testing.assert_array_equal(obs, np.array([1, -1, 3, 4, 2, 5, 6, 7, 8]))
    
    def test_solved_state(self):
        """Test solved state detection with 3x3 puzzle."""
        solved_puzzle = "1 2 3|4 5 6|7 -1 8"
        env = Puzzle15Env(height=3, width=3, custom_puzzle=solved_puzzle)

        obs, reward, done, _, info = env.step(1)
        self.assertTrue(done)
        self.assertEqual(reward, 0)
        self.assertIn("valid_actions", info)
        self.assertEqual(set(info["valid_actions"]), set())
    
    def test_reset_valid_actions(self):
        """Test that reset returns valid actions in the info dictionary."""
        # Reset the environment
        _, info = self.env.reset()
        
        # Check that valid_actions is in the info dictionary
        self.assertIn("valid_actions", info)
        
        # Check that valid_actions is a list
        self.assertIsInstance(info["valid_actions"], list)
        
        # In initial state (blank in middle), all moves are valid
        self.assertEqual(set(info["valid_actions"]), {0, 1, 2, 3})
        
        # Make some moves and reset again
        self.env.step(0)  # up
        _, info = self.env.reset()
        
        # Check that valid_actions is still correct after reset
        self.assertEqual(set(info["valid_actions"]), {0, 1, 2, 3})
    
    def test_step_valid_actions(self):
        """Test that step returns valid actions in the info dictionary."""
        # Reset the environment
        self.env.reset()
        
        # Take a step and check valid_actions
        _, _, _, _, info = self.env.step(0)  # up
        self.assertIn("valid_actions", info)
        self.assertIsInstance(info["valid_actions"], list)
        self.assertEqual(set(info["valid_actions"]), {1, 2, 3})
        
        # Take another step and check valid_actions
        _, _, _, _, info = self.env.step(3)  # left
        self.assertIn("valid_actions", info)
        self.assertIsInstance(info["valid_actions"], list)
        self.assertEqual(set(info["valid_actions"]), {1, 2})
        
        # Try an invalid move and check valid_actions
        _, _, _, _, info = self.env.step(3)  # left (invalid)
        self.assertIn("valid_actions", info)
        self.assertIsInstance(info["valid_actions"], list)
        self.assertEqual(set(info["valid_actions"]), {1, 2})

if __name__ == '__main__':
    unittest.main() 