"""
Unit tests for the GuessingGameGUI class
Tests the core game logic without GUI components
"""

import pytest
import random
import unittest.mock as mock
from unittest.mock import MagicMock, patch, PropertyMock
import sys
import os

# Add the parent directory to the path so we can import game
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestGuessingGameLogic:
    """Test cases for the core game logic using improved mocking"""
    
    def test_game_initialization(self, mock_game_minimal):
        """Test that the game initializes with correct default values"""
        game = mock_game_minimal
        assert game.secret_number == 0
        assert game.attempts_left == 7
        assert game.hints_left == 3
        assert game.hint_level == 0
        assert game.current_round == 1
        assert game.total_rounds == 1
        assert game.wins == 0
        assert game.game_active == False
        assert game.min_possible == 0
        assert game.max_possible == 100
        assert game.previous_guesses == []
    
    def test_sanitize_input_valid(self, mock_game_minimal):
        """Test input sanitization with valid inputs"""
        game = mock_game_minimal
        
        # Test normal number
        result, error = game.sanitize_input("42")
        assert result == 42
        assert error is None
        
        # Test number with whitespace
        result, error = game.sanitize_input("  25  ")
        assert result == 25
        assert error is None
        
        # Test zero
        result, error = game.sanitize_input("0")
        assert result == 0
        assert error is None
    
    def test_sanitize_input_invalid(self, mock_game_minimal):
        """Test input sanitization with invalid inputs"""
        game = mock_game_minimal
        
        # Test non-numeric input
        result, error = game.sanitize_input("abc")
        assert result is None
        assert "Please enter a valid number" in error
        
        # Test decimal number
        result, error = game.sanitize_input("42.5")
        assert result is None
        assert "Please enter a whole number" in error
        
        # Test empty input
        result, error = game.sanitize_input("")
        assert result is None
        assert "Please enter a number" in error
        
        # Test negative number
        result, error = game.sanitize_input("-10")
        assert result is None
        assert "Please enter a positive number" in error
    
    def test_generate_hint_level_0(self, mock_game_minimal):
        """Test hint generation for level 0"""
        game = mock_game_minimal
        
        # Test number below 50
        hint = game.generate_hint(25, 0)
        assert "less than 50" in hint
        
        # Test number 50 or above
        hint = game.generate_hint(75, 0)
        assert "50 or greater" in hint
        
        # Test edge case: 49
        hint = game.generate_hint(49, 0)
        assert "less than 50" in hint
        
        # Test edge case: 50
        hint = game.generate_hint(50, 0)
        assert "50 or greater" in hint
    
    def test_generate_hint_level_1(self, mock_game_minimal):
        """Test hint generation for level 1"""
        game = mock_game_minimal
        
        # Test all four quarters
        hint = game.generate_hint(10, 1)
        assert "0 and 25" in hint
        
        hint = game.generate_hint(35, 1)
        assert "25 and 50" in hint
        
        hint = game.generate_hint(60, 1)
        assert "50 and 75" in hint
        
        hint = game.generate_hint(90, 1)
        assert "75 and 100" in hint
    
    def test_generate_hint_level_2(self, mock_game_minimal):
        """Test hint generation for level 2"""
        game = mock_game_minimal
        
        # Test that level 2 hints are more specific
        hint = game.generate_hint(25, 2)
        assert "specific hint range" in hint or "between" in hint
    
    def test_log_attempt_valid(self, mock_game_minimal):
        """Test logging a valid attempt"""
        game = mock_game_minimal
        
        game.log_attempt(42, is_valid=True)
        
        assert len(game.attempt_log) == 1
        assert game.attempt_log[0]['guess'] == 42
        assert game.attempt_log[0]['is_valid'] == True
    
    def test_log_attempt_invalid(self, mock_game_minimal):
        """Test logging an invalid attempt"""
        game = mock_game_minimal
        
        game.log_attempt("abc", is_valid=False)
        
        assert len(game.attempt_log) == 1
        assert game.attempt_log[0]['guess'] == "abc"
        assert game.attempt_log[0]['is_valid'] == False
    
    def test_win_rate_calculation(self, mock_game_minimal):
        """Test win rate calculation"""
        game = mock_game_minimal
        
        game.wins = 7
        game.current_round = 11  # 10 completed rounds
        
        win_rate = game.calculate_win_rate()
        
        assert win_rate == 70.0  # 7/10 = 0.7 = 70%
    
    def test_win_rate_no_games(self, mock_game_minimal):
        """Test win rate calculation with no completed games"""
        game = mock_game_minimal
        
        game.wins = 0
        game.current_round = 1  # No completed rounds
        
        win_rate = game.calculate_win_rate()
        
        assert win_rate == 0.0
    
    def test_new_session_reset(self, mock_game_minimal):
        """Test that a new session resets statistics"""
        game = mock_game_minimal
        
        game.wins = 5
        game.current_round = 8
        
        game.new_session()
        
        assert game.wins == 0
        assert game.current_round == 1
        assert game.game_active == False
    
    def test_clear_attempt_log(self, mock_game_minimal):
        """Test clearing the attempt log"""
        game = mock_game_minimal
        
        game.attempt_log = [
            {'guess': 42, 'is_valid': True},
            {'guess': 25, 'is_valid': True}
        ]
        
        game.clear_attempt_log()
        
        assert len(game.attempt_log) == 0
    
    def test_edge_case_boundaries(self, mock_game_minimal):
        """Test edge cases at boundaries"""
        game = mock_game_minimal
        
        # Test minimum boundary
        result, error = game.sanitize_input("0")
        assert result == 0
        assert error is None
        
        # Test maximum boundary - this should be valid for input
        result, error = game.sanitize_input("100")
        assert result == 100
        assert error is None
    
    def test_hint_progression(self, mock_game_minimal):
        """Test that hints become more specific"""
        game = mock_game_minimal
        
        # Test that different hint levels provide different information
        hint_0 = game.generate_hint(42, 0)
        hint_1 = game.generate_hint(42, 1)
        hint_2 = game.generate_hint(42, 2)
        
        # All should be different (more specific)
        assert hint_0 != hint_1
        assert hint_1 != hint_2
        assert hint_0 != hint_2
    
    def test_input_whitespace_handling(self, mock_game_minimal):
        """Test that input handles whitespace correctly"""
        game = mock_game_minimal
        
        # Test various whitespace scenarios
        test_cases = [
            "  42  ",
            "\t25\t",
            " 0 ",
            "100   "
        ]
        
        for test_input in test_cases:
            result, error = game.sanitize_input(test_input)
            assert result is not None
            assert error is None
            assert isinstance(result, int)
    
    def test_attempt_log_timestamps(self, mock_game_minimal):
        """Test that attempt log includes timestamps"""
        game = mock_game_minimal
        
        game.log_attempt(42, is_valid=True)
        
        assert len(game.attempt_log) == 1
        assert 'timestamp' in game.attempt_log[0]
        assert isinstance(game.attempt_log[0]['timestamp'], float)
    
    def test_multiple_attempts_logging(self, mock_game_minimal):
        """Test logging multiple attempts"""
        game = mock_game_minimal
        
        # Log multiple attempts
        attempts = [25, 50, 75, "abc", 100]
        validities = [True, True, True, False, True]
        
        for attempt, validity in zip(attempts, validities):
            game.log_attempt(attempt, is_valid=validity)
        
        assert len(game.attempt_log) == 5
        
        # Check that all attempts were logged correctly
        for i, (attempt, validity) in enumerate(zip(attempts, validities)):
            assert game.attempt_log[i]['guess'] == attempt
            assert game.attempt_log[i]['is_valid'] == validity
