"""
Example test file demonstrating the testing framework
This file shows how to write tests for the Number Guessing Game
"""

import pytest
import unittest.mock as mock
from unittest.mock import MagicMock, patch
import sys
import os

# Add the parent directory to the path so we can import game
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game import GuessingGameGUI


class TestExampleUsage:
    """Example tests showing how to use the testing framework"""
    
    def test_simple_example(self, mock_game_minimal):
        """Example: Test basic game functionality"""
        game = mock_game_minimal
        
        # Test that we can access game attributes
        assert game.secret_number == 0
        assert game.attempts_left == 7
        assert game.game_active == False
    
    def test_input_validation_example(self, mock_game_minimal):
        """Example: Test input validation with different inputs"""
        game = mock_game_minimal
        
        # Test valid input
        result, error = game.sanitize_input("42")
        assert result == 42
        assert error is None
        
        # Test invalid input
        result, error = game.sanitize_input("not_a_number")
        assert result is None
        assert error is not None
        assert "valid number" in error
    
    @pytest.mark.parametrize("input_val,expected_valid", [
        ("25", True),
        ("75", True),
        ("50", True),
        ("abc", False),
        ("12.5", False),
        ("", False),
    ])
    def test_guess_validation_example(self, input_val, expected_valid, mock_game_minimal):
        """Example: Parameterized test for input validation"""
        game = mock_game_minimal
        
        result, error = game.sanitize_input(input_val)
        
        if expected_valid:
            assert result is not None
            assert error is None
        else:
            assert result is None
            assert error is not None
    
    def test_hint_system_example(self, mock_game_minimal):
        """Example: Test the hint system"""
        game = mock_game_minimal
        
        # Test different hint levels
        hint_0 = game.generate_hint(42, 0)
        hint_1 = game.generate_hint(42, 1)
        hint_2 = game.generate_hint(42, 2)
        
        # All hints should be different
        assert hint_0 != hint_1
        assert hint_1 != hint_2
        
        # Test specific hint content
        assert "50" in hint_0  # Should mention 50 as reference point
    
    def test_multiple_rounds_example(self, mock_game_minimal):
        """Example: Test game state management"""
        game = mock_game_minimal
        
        # Test initial state
        assert game.wins == 0
        assert game.current_round == 1
        
        # Simulate winning a round
        game.wins = 1
        game.current_round = 2
        
        # Test new session reset
        game.new_session()
        assert game.wins == 0
        assert game.current_round == 1
    
    def test_edge_case_example(self, mock_game_minimal):
        """Example: Test edge cases"""
        game = mock_game_minimal
        
        # Test boundary values
        result, error = game.sanitize_input("0")
        assert result == 0
        assert error is None
        
        result, error = game.sanitize_input("100")
        assert result == 100
        assert error is None
        
        # Test out of bounds
        result, error = game.sanitize_input("-1")
        assert result is None
        assert error is not None
    
    def test_error_handling_example(self, mock_game_minimal):
        """Example: Test error handling"""
        game = mock_game_minimal
        
        # Test various invalid inputs
        invalid_inputs = ["abc", "12.5", "", "  ", "-10"]
        
        for invalid_input in invalid_inputs:
            result, error = game.sanitize_input(invalid_input)
            assert result is None
            assert error is not None
            assert isinstance(error, str)
    
    def test_performance_example(self, mock_game_minimal):
        """Example: Basic performance test"""
        import time
        game = mock_game_minimal
        
        # Measure time for input validation
        start_time = time.time()
        
        # Test many inputs
        for i in range(100):
            game.sanitize_input(str(i))
        
        end_time = time.time()
        processing_time = end_time - start_time
        
        # Should process quickly
        assert processing_time < 0.1  # Less than 100ms
    
    def test_state_consistency_example(self, mock_game_minimal):
        """Example: Test that game state remains consistent"""
        game = mock_game_minimal
        
        # Test attempt logging
        game.log_attempt(25, is_valid=True)
        
        # Check that state is consistent
        assert len(game.attempt_log) == 1
        assert game.attempt_log[0]['guess'] == 25
        assert game.attempt_log[0]['is_valid'] == True
    
    def test_mocking_example(self, mock_game_minimal):
        """Example: Working with mocks"""
        game = mock_game_minimal
        
        # Test that we can call methods
        game.log_attempt(42, is_valid=True)
        
        # Test that we can access attributes
        assert hasattr(game, 'attempt_log')
        assert hasattr(game, 'wins')
        assert hasattr(game, 'current_round')
        
        # Test method calls
        win_rate = game.calculate_win_rate()
        assert isinstance(win_rate, float)
        assert win_rate >= 0.0


# Additional example: How to run these tests
if __name__ == "__main__":
    # You can run this file directly to see the tests in action
    pytest.main([__file__, "-v"])
