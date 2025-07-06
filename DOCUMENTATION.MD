# Number Guessing Game Documentation

## Overview
This is a modern GUI-based Number Guessing Game built with Python and CustomTkinter. The game provides an engaging and interactive experience where players attempt to guess a randomly generated number within a specified range.

## Features
- **Modern GUI Interface**: Built with CustomTkinter for a sleek, modern appearance
- **Customizable Difficulty**: Multiple difficulty levels with different number ranges
- **Score Tracking**: Keeps track of attempts and success rate
- **Interactive Feedback**: Real-time hints and feedback for each guess
- **Responsive Design**: Clean and intuitive user interface

## System Requirements
- Python 3.7 or higher
- CustomTkinter 5.2.2 or higher
- Standard Python libraries (tkinter, random, threading, time)

## Installation

### Option 1: Using Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Option 2: Direct Installation
```bash
pip install customtkinter>=5.2.2
```

## Running the Game
```bash
python game.py
```

## Game Rules
1. The computer generates a random number within the selected range
2. Player enters their guess in the input field
3. The game provides feedback:
   - "Too High" if the guess is above the target
   - "Too Low" if the guess is below the target
   - "Correct!" when the number is guessed
4. The game tracks the number of attempts
5. Player can start a new game at any time

## Difficulty Levels
- **Easy**: Numbers 1-10 (Perfect for beginners)
- **Medium**: Numbers 1-50 (Balanced challenge)
- **Hard**: Numbers 1-100 (Maximum challenge)
- **Custom**: Player-defined range

## File Structure
```
guess-the-number/
├── game.py              # Main game file
├── requirements.txt     # Python dependencies
├── README.md           # Basic project information
└── DOCUMENTATION.md    # This file
```

## Code Architecture
The game follows a modular design pattern:
- **GUI Components**: Built with CustomTkinter widgets
- **Game Logic**: Separated from UI for better maintainability
- **Event Handling**: Responsive to user interactions
- **State Management**: Tracks game state and statistics

## Development Notes
- The game uses threading for smooth GUI operations
- Error handling is implemented for invalid inputs
- The interface is designed to be accessible and user-friendly
- Code follows Python best practices and PEP 8 guidelines

## Future Enhancements
- [ ] High score persistence
- [ ] Sound effects and animations
- [ ] Multiplayer mode
- [ ] Additional game modes (e.g., reverse guessing)
- [ ] Themes and customization options

## Troubleshooting

### Common Issues
1. **ModuleNotFoundError**: Install CustomTkinter using pip
2. **GUI not displaying**: Ensure tkinter is available in your Python installation
3. **Performance issues**: Check if threading is working properly

### Getting Help
If you encounter issues:
1. Check that all dependencies are installed
2. Verify Python version compatibility
3. Ensure virtual environment is activated (if using one)

## License
This project is part of the Python Fundamentals course materials.

## Contributing
This is an educational project. Feel free to experiment and modify the code to enhance your learning experience.

---
*Last updated: July 6, 2025*
