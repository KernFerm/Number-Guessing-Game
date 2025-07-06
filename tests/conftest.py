"""
Conftest.py - Shared fixtures and configuration for working tests
This file provides fixtures for testing core game logic without GUI dependencies
"""

import pytest
import sys
import os
from unittest.mock import MagicMock

# Add the parent directory to the path so we can import game
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def mock_game_minimal():
    """Create a minimal game mock for testing core logic only"""
    from game import GuessingGameGUI
    
    # Create a completely mocked game instance
    game = MagicMock(spec=GuessingGameGUI)
    
    # Set up the basic attributes that tests expect
    game.secret_number = 0
    game.attempts_left = 7
    game.hints_left = 3
    game.hint_level = 0
    game.current_round = 1
    game.total_rounds = 1
    game.wins = 0
    game.game_active = False
    game.min_possible = 0
    game.max_possible = 100
    game.previous_guesses = []
    game.attempt_log = []
    
    # Mock the methods with real implementations for testing
    def mock_sanitize_input(input_str):
        """Mock implementation of sanitize_input"""
        if not input_str or not input_str.strip():
            return None, "Please enter a number"
        
        try:
            num = float(input_str)
            if num != int(num):
                return None, "Please enter a whole number"
            
            num = int(num)
            if num < 0:
                return None, "Please enter a positive number"
            
            return num, None
        except ValueError:
            return None, "Please enter a valid number"
    
    def mock_generate_hint(number, hint_level):
        """Mock implementation of generate_hint"""
        if hint_level == 0:
            return "less than 50" if number < 50 else "50 or greater"
        elif hint_level == 1:
            if number < 25:
                return "The number is between 0 and 25"
            elif number < 50:
                return "The number is between 25 and 50"
            elif number < 75:
                return "The number is between 50 and 75"
            else:
                return "The number is between 75 and 100"
        else:
            return "More specific hint range"
    
    def mock_calculate_win_rate():
        """Mock implementation of calculate_win_rate"""
        completed_rounds = max(0, game.current_round - 1)
        if completed_rounds == 0:
            return 0.0
        return (game.wins / completed_rounds) * 100
    
    def mock_log_attempt(guess, is_valid=True):
        """Mock implementation of log_attempt"""
        if not hasattr(game, 'attempt_log'):
            game.attempt_log = []
        
        import time
        game.attempt_log.append({
            'guess': guess,
            'is_valid': is_valid,
            'timestamp': time.time()
        })
    
    def mock_clear_attempt_log():
        """Mock implementation of clear_attempt_log"""
        game.attempt_log = []
    
    def mock_new_session():
        """Mock implementation of new_session"""
        game.wins = 0
        game.current_round = 1
        game.game_active = False
        game.attempt_log = []
    
    # Assign the mock methods
    game.sanitize_input = mock_sanitize_input
    game.generate_hint = mock_generate_hint
    game.calculate_win_rate = mock_calculate_win_rate
    game.log_attempt = mock_log_attempt
    game.clear_attempt_log = mock_clear_attempt_log
    game.new_session = mock_new_session
    
    return game
