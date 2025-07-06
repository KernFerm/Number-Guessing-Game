# 🎯 Number Guessing Game

A modern, feature-rich GUI number guessing game built with Python and CustomTkinter. Test your guessing skills and strategic thinking while enjoying a beautiful dark-themed interface!

## 🎮 Game Overview

Try to guess the secret number between 0 and 100 in as few attempts as possible! With only 7 attempts per round, you'll need to use strategy and hints wisely to achieve a high win rate.

## ✨ Features

### 🎨 **Modern GUI Interface**
- Beautiful dark theme with cyan accents
- Responsive design that scales with window size
- Professional menubar with File and Help options
- Real-time status updates with color coding
- Smooth animations and transitions

### 🎯 **Strategic Gameplay**
- **Binary Search Strategy Tips**: Get optimal next guess suggestions
- **Range Tracking**: See exactly how many numbers are left after each guess
- **Improved Hint System**: Progressive hints that actually help you win
- **Attempt Logging**: Track all your guesses for analysis

### 🛡️ **Security & Validation**
- Comprehensive input sanitization
- Protection against malicious input
- Robust error handling
- Input validation with helpful error messages

### 📊 **Statistics & Analysis**
- Win rate tracking across multiple sessions
- Detailed game statistics
- Attempt logging and analysis
- Performance feedback based on your results

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- CustomTkinter library

### Installation

## ⭐ Support the Project
If you find this project useful, please give it a star! Your support is appreciated and helps keep the project growing. 🌟

## 📥 How to Download the Repo for First-Time Users
- Click the link to read [**Instructions**](https://www.gitprojects.fnbubbles420.org/how-to-download-repos).

2. **Install required dependencies**
   ```bash
   pip install customtkinter
   ```

3. **Run the game**
   ```bash
   python game.py
   ```

## 🎮 How to Play

### Basic Gameplay
1. **Start the game** - A secret number between 0-100 is randomly generated
2. **Make your guess** - Enter a number in the input field or use the Strategy Tip
3. **Get feedback** - The game tells you if your guess is too high or too low
4. **Use hints wisely** - You get 3 hints per round that become progressively more specific
5. **Win the round** - Guess the correct number within 7 attempts!

### 🎯 Winning Strategy

#### **Binary Search Method** (Recommended)
1. **Start with 50** - This splits the range in half
2. **Use the Strategy Tip button** - It calculates the optimal next guess
3. **Follow the range updates** - Pay attention to how many numbers are left
4. **Save hints for tight spots** - Use them when you have fewer than 10 possibilities

#### **Hint System Guide**
- **Hint 1**: Splits range in half (0-49 vs 50-100)
- **Hint 2**: Gives you a quarter range (25 numbers)
- **Hint 3**: Narrows to ~12-13 numbers
- **Bonus Hint**: Super specific range (6-7 numbers)

## 🔧 Game Controls

### **Main Interface**
- **Make Guess Button**: Submit your current guess
- **Get Hint Button**: Use one of your 3 hints
- **Strategy Tip Button**: Get the mathematically optimal next guess
- **New Session Button**: Start a new multi-round session
- **Show Stats Button**: View your performance statistics

### **Menu Options**
#### **📁 File Menu**
- New Session
- Show Statistics
- Restart Current Game
- View Attempt Log
- Clear Attempt Log
- Exit

#### **❓ Help Menu**
- How to Play
- Game Rules
- About

## 🎯 Pro Tips

1. **Always start with 50** - This gives you the best chance of winning
2. **Use the Strategy Tip button** - It's like having a math tutor!
3. **Watch the range tracker** - You'll see exactly how many numbers are left
4. **Don't waste hints early** - Save them for when you really need them
5. **Practice the binary search method** - It's mathematically optimal

## 📊 Technical Details

### **Built With**
- **Python 3.11.9** - Core programming language
- **CustomTkinter** - Modern GUI framework
- **Threading** - For smooth, non-blocking gameplay
- **Tkinter** - Additional GUI components

### **Key Features**
- **Input Sanitization** - Protects against malicious input
- **Range Validation** - Ensures all inputs are within acceptable limits
- **Error Handling** - Graceful handling of invalid inputs
- **Memory Management** - Efficient logging with automatic cleanup
- **Cross-platform** - Works on Windows, macOS, and Linux

### **Security Features**
- Malicious character detection
- Input length limits
- Type validation
- Range checking
- Comprehensive error messages

## 🎪 Game Modes

### **Single Round**
- Quick game for testing your skills
- Perfect for learning the strategy

### **Multi-Round Sessions**
- Play multiple rounds in sequence
- Track your win rate across rounds
- Challenge yourself to improve

### **Statistics Tracking**
- Win/loss ratio
- Performance analysis
- Attempt logging
- Strategic insights

## 🔄 Game Rules

### **Basic Rules**
- Secret number is between 0-100 (inclusive)
- You have exactly 7 attempts per round
- 3 hints available per round
- Integer numbers only

### **Winning Conditions**
- **Win**: Guess the correct number within 7 attempts
- **Lose**: Use all 7 attempts without finding the number

### **Hint System**
- Hints become more specific as you use them
- Once used, hints cannot be reused in the same round
- Hints are reset for each new round

## 🎨 Customization

The game features a beautiful dark theme with:
- **Background**: Dark gray (#2B2B2B)
- **Accent Color**: Cyan (#00BCD4)
- **Success Color**: Green (#4CAF50)
- **Warning Color**: Orange (#FF9800)
- **Error Color**: Red (#F44336)

## 🐛 Troubleshooting

### **Common Issues**
1. **"Module not found" error**: Install CustomTkinter with `pip install customtkinter`
2. **Window too small**: The window is resizable - drag the corners to expand
3. **Game not responding**: Check for error messages in the console
4. **Hints not working**: Make sure you haven't used all 3 hints for the round

### **Performance Tips**
- Close other applications if the game runs slowly
- The game automatically manages memory usage
- Attempt logs are limited to 100 entries for performance

## 📈 Version History

### **v1.0** - Initial Release
- Modern GUI with CustomTkinter
- Basic guessing game functionality
- Hint system
- Statistics tracking
- Input validation
- Strategy tips
- Binary search guidance
- Comprehensive help system

## 🎯 Future Enhancements

Potential features for future versions:
- Difficulty levels (different number ranges)
- Sound effects and animations
- Online leaderboards
- Custom themes
- Save/load game sessions
- Achievement system

## 🤝 Contributing

This is a learning project, but suggestions and improvements are welcome! Feel free to:
- Report bugs
- Suggest new features
- Improve the documentation
- Optimize the code

## 🎉 Have Fun!

Remember, the goal is to have fun while improving your logical thinking and strategic planning skills. With the right strategy, you should be able to achieve a high win rate!

**Good luck, and may your guesses be ever in your favor!** 🎯

---

*Built with ❤️ using Python and CustomTkinter*
