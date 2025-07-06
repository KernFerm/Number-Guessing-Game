import random
import customtkinter as ctk
from tkinter import messagebox
import threading
import time
import tkinter as tk

class GuessingGameGUI:
    def __init__(self):
        # Set appearance mode and color theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Initialize main window
        self.root = ctk.CTk()
        self.root.title("🎯 Number Guessing Game")
        self.root.geometry("1000x800")
        self.root.resizable(True, True)
        
        # Game variables
        self.secret_number = 0
        self.attempts_left = 7
        self.hints_left = 3
        self.hint_level = 0
        self.current_round = 1
        self.total_rounds = 1
        self.wins = 0
        self.game_active = False
        
        # Strategy tracking
        self.min_possible = 0
        self.max_possible = 100
        self.previous_guesses = []
        
        self.setup_ui()
        
    def setup_ui(self):
        # Create menubar
        self.create_menubar()
        
        # Main title
        title_label = ctk.CTkLabel(
            self.root,
            text="🎯 Number Guessing Game",
            font=ctk.CTkFont(size=32, weight="bold")
        )
        title_label.pack(pady=20)
        
        # Game info frame
        info_frame = ctk.CTkFrame(self.root)
        info_frame.pack(pady=10, padx=20, fill="x")
        
        self.round_label = ctk.CTkLabel(
            info_frame,
            text="Round 1 of 1",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.round_label.pack(pady=10)
        
        self.instructions_label = ctk.CTkLabel(
            info_frame,
            text="Guess a number between 0 and 100!\nYou have 7 attempts and 3 hints.",
            font=ctk.CTkFont(size=14)
        )
        self.instructions_label.pack(pady=5)
        
        # Game status frame
        status_frame = ctk.CTkFrame(self.root)
        status_frame.pack(pady=10, padx=20, fill="x")
        
        status_inner_frame = ctk.CTkFrame(status_frame)
        status_inner_frame.pack(pady=15, padx=15, fill="x")
        
        self.attempts_label = ctk.CTkLabel(
            status_inner_frame,
            text="Attempts left: 7",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#4CAF50"
        )
        self.attempts_label.grid(row=0, column=0, padx=20, pady=5, sticky="w")
        
        self.hints_label = ctk.CTkLabel(
            status_inner_frame,
            text="Hints left: 3",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#FF9800"
        )
        self.hints_label.grid(row=0, column=1, padx=20, pady=5, sticky="e")
        
        status_inner_frame.grid_columnconfigure(0, weight=1)
        status_inner_frame.grid_columnconfigure(1, weight=1)
        
        # Input frame
        input_frame = ctk.CTkFrame(self.root)
        input_frame.pack(pady=20, padx=20, fill="x")
        
        guess_label = ctk.CTkLabel(
            input_frame,
            text="Enter your guess:",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        guess_label.pack(pady=(15, 5))
        
        self.guess_entry = ctk.CTkEntry(
            input_frame,
            placeholder_text="Enter a number between 0 and 100",
            font=ctk.CTkFont(size=14),
            width=300,
            height=40
        )
        self.guess_entry.pack(pady=5)
        self.guess_entry.bind("<Return>", lambda e: self.make_guess())
        
        # Buttons frame
        buttons_frame = ctk.CTkFrame(input_frame)
        buttons_frame.pack(pady=15, fill="x")
        
        self.guess_button = ctk.CTkButton(
            buttons_frame,
            text="🎲 Make Guess",
            command=self.make_guess,
            font=ctk.CTkFont(size=16, weight="bold"),
            height=40,
            width=150
        )
        self.guess_button.pack(side="left", padx=10)
        
        self.hint_button = ctk.CTkButton(
            buttons_frame,
            text="💡 Get Hint",
            command=self.get_hint,
            font=ctk.CTkFont(size=16, weight="bold"),
            height=40,
            width=150,
            fg_color="#FF9800",
            hover_color="#F57C00"
        )
        self.hint_button.pack(side="right", padx=10)
        
        # Strategic hint button
        self.strategy_button = ctk.CTkButton(
            buttons_frame,
            text="🎯 Strategy Tip",
            command=self.get_strategy_tip,
            font=ctk.CTkFont(size=16, weight="bold"),
            height=40,
            width=150,
            fg_color="#9C27B0",
            hover_color="#7B1FA2"
        )
        self.strategy_button.pack(side="right", padx=10)
        
        # Messages frame
        messages_frame = ctk.CTkFrame(self.root)
        messages_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        messages_label = ctk.CTkLabel(
            messages_frame,
            text="🎮 Game Messages:",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#00BCD4"
        )
        messages_label.pack(pady=(15, 5))
        
        self.messages_text = ctk.CTkTextbox(
            messages_frame,
            font=ctk.CTkFont(size=14),
            height=250,
            corner_radius=10,
            border_width=2,
            border_color="#00BCD4",
            fg_color="#1e1e1e",
            text_color="#ffffff",
            scrollbar_button_color="#00BCD4",
            scrollbar_button_hover_color="#0097A7"
        )
        self.messages_text.pack(pady=(5, 15), padx=15, fill="both", expand=True)
        
        # Control buttons frame
        control_frame = ctk.CTkFrame(self.root)
        control_frame.pack(pady=10, padx=20, fill="x")
        
        self.new_session_button = ctk.CTkButton(
            control_frame,
            text="🎮 New Session",
            command=self.new_session,
            font=ctk.CTkFont(size=16, weight="bold"),
            height=40,
            width=150,
            fg_color="#4CAF50",
            hover_color="#45a049"
        )
        self.new_session_button.pack(side="left", padx=10, pady=10)
        
        self.stats_button = ctk.CTkButton(
            control_frame,
            text="📊 Show Stats",
            command=self.show_stats,
            font=ctk.CTkFont(size=16, weight="bold"),
            height=40,
            width=150,
            fg_color="#9C27B0",
            hover_color="#7B1FA2"
        )
        self.stats_button.pack(side="right", padx=10, pady=10)
        
        # Start first game
        self.add_message("🎉 Welcome to the Number Guessing Game!")
        self.add_message("🎯 Game loaded successfully - ready to play!")
        self.start_new_game()
        
    def create_menubar(self):
        """Create the top menubar"""
        # Create a frame for the menubar
        menubar_frame = ctk.CTkFrame(self.root, height=40)
        menubar_frame.pack(fill="x", padx=5, pady=(5, 0))
        menubar_frame.pack_propagate(False)
        
        # File menu button
        file_menu_button = ctk.CTkButton(
            menubar_frame,
            text="📁 File",
            command=self.show_file_menu,
            width=80,
            height=30,
            font=ctk.CTkFont(size=12, weight="bold"),
            fg_color="transparent",
            hover_color="#2B2B2B"
        )
        file_menu_button.pack(side="left", padx=5, pady=5)
        
        # Help menu button
        help_menu_button = ctk.CTkButton(
            menubar_frame,
            text="❓ Help",
            command=self.show_help_menu,
            width=80,
            height=30,
            font=ctk.CTkFont(size=12, weight="bold"),
            fg_color="transparent",
            hover_color="#2B2B2B"
        )
        help_menu_button.pack(side="left", padx=5, pady=5)
        
        # Version info (right side)
        version_label = ctk.CTkLabel(
            menubar_frame,
            text="v1.0",
            font=ctk.CTkFont(size=10),
            text_color="#666666"
        )
        version_label.pack(side="right", padx=10, pady=5)
        
    def show_file_menu(self):
        """Show file menu options"""
        file_menu = tk.Menu(self.root, tearoff=0, bg="#2B2B2B", fg="white", 
                           activebackground="#1f538d", activeforeground="white")
        
        file_menu.add_command(label="🎮 New Session", command=self.new_session)
        file_menu.add_command(label="📊 Show Statistics", command=self.show_stats)
        file_menu.add_separator()
        file_menu.add_command(label="🔄 Restart Current Game", command=self.restart_game)
        file_menu.add_separator()
        file_menu.add_command(label="🔍 View Attempt Log", command=self.show_attempt_log)
        file_menu.add_command(label="🗑️ Clear Attempt Log", command=self.clear_attempt_log)
        file_menu.add_separator()
        file_menu.add_command(label="❌ Exit", command=self.exit_game)
        
        # Get button position for popup
        try:
            file_menu.tk_popup(self.root.winfo_x() + 50, self.root.winfo_y() + 80)
        finally:
            file_menu.grab_release()
            
    def show_help_menu(self):
        """Show help menu options"""
        help_menu = tk.Menu(self.root, tearoff=0, bg="#2B2B2B", fg="white",
                           activebackground="#1f538d", activeforeground="white")
        
        help_menu.add_command(label="🎯 How to Play", command=self.show_how_to_play)
        help_menu.add_command(label="🎮 Game Rules", command=self.show_game_rules)
        help_menu.add_separator()
        help_menu.add_command(label="ℹ️ About", command=self.show_about)
        
        # Get button position for popup
        try:
            help_menu.tk_popup(self.root.winfo_x() + 130, self.root.winfo_y() + 80)
        finally:
            help_menu.grab_release()
            
    def show_how_to_play(self):
        """Show how to play instructions"""
        how_to_play = """
🎯 HOW TO PLAY THE NUMBER GUESSING GAME

🎮 OBJECTIVE:
Guess the secret number between 0 and 100 in as few attempts as possible!

🎲 GAMEPLAY:
1. Enter a number between 0 and 100 in the input field
2. Click "Make Guess" or press Enter
3. The game will tell you if your guess is too high or too low
4. You have 7 attempts to guess correctly
5. Use hints wisely - you only get 3 per round!

💡 HINTS:
• First hint: Tells you if the number is above or below 50
• Second hint: Tells you if it's between 5 and 80
• Third hint: Gives you a more specific range

🏆 WINNING:
• Guess the correct number to win the round
• Play multiple rounds in a session
• Track your win rate and improve your skills!

🎯 TIPS:
• Start with 50 to divide the range in half
• Use the elimination method
• Save hints for when you really need them
• Pay attention to the feedback after each guess
        """
        
        messagebox.showinfo("How to Play", how_to_play)
        
    def show_game_rules(self):
        """Show detailed game rules"""
        rules = """
📋 GAME RULES

🎲 BASIC RULES:
• Secret number is randomly generated between 0-100
• You have exactly 7 attempts per round
• You get 3 hints per round
• Numbers must be integers only

⚠️ RESTRICTIONS:
• Guesses outside 0-100 range are invalid
• Non-numeric entries are rejected
• Hints can only be used once per round
• Game ends when attempts reach 0

🎯 SCORING:
• Win: Guess the correct number
• Lose: Use all 7 attempts without success
• Win Rate: Percentage of rounds won

🏆 SESSION PLAY:
• Choose number of rounds (1-unlimited)
• Statistics tracked across all rounds
• New session resets win/loss count
• Each round is independent

💡 HINT SYSTEM:
• Hint 1: Above/below 50
• Hint 2: Inside/outside 5-80 range  
• Hint 3: Specific range (20-number segments)
• Hints become more specific as you use them
        """
        
        messagebox.showinfo("Game Rules", rules)
        
    def show_about(self):
        """Show about information"""
        about_text = """
🎯 NUMBER GUESSING GAME v1.0

🎮 A modern GUI guessing game built with Python and CustomTkinter

👨‍💻 FEATURES:
• Beautiful dark theme interface
• Multiple rounds gameplay
• Intelligent hint system
• Real-time statistics
• Responsive design

🛠️ TECHNOLOGY:
• Python 3.x
• CustomTkinter GUI Framework
• Threading for smooth gameplay
• Cross-platform compatibility

🎯 ENJOY THE GAME!
Test your guessing skills and see how high you can get your win rate!
        """
        
        messagebox.showinfo("About", about_text)
        
    def restart_game(self):
        """Restart the current game"""
        if messagebox.askyesno("Restart Game", "Are you sure you want to restart the current round?"):
            self.start_new_game()
            self.add_message("🔄 Game restarted!")
            
    def exit_game(self):
        """Exit the application"""
        if messagebox.askyesno("Exit Game", "Are you sure you want to exit?"):
            self.root.quit()
            
    def add_message(self, message, color="#FFFFFF"):
        """Add a message to the messages textbox"""
        self.messages_text.configure(state="normal")
        # Add timestamp for better readability
        timestamp = time.strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {message}\n"
        self.messages_text.insert("end", formatted_message)
        self.messages_text.configure(state="disabled")
        self.messages_text.see("end")
        # Force update to ensure visibility
        self.root.update_idletasks()
        
    def start_new_game(self):
        """Start a new game round"""
        self.secret_number = random.randint(0, 100)
        self.attempts_left = 7
        self.hints_left = 3
        self.hint_level = 0
        self.game_active = True
        
        # Reset strategy tracking
        self.min_possible = 0
        self.max_possible = 100
        self.previous_guesses = []
        
        self.update_labels()
        self.guess_entry.delete(0, "end")
        self.guess_entry.focus()
        
        self.add_message(f"🎮 Round {self.current_round} of {self.total_rounds} started!")
        self.add_message("🎯 I'm thinking of a number between 0 and 100...")
        self.add_message("💡 Pro tip: Start with 50 to use binary search strategy!")
        
    def update_labels(self):
        """Update the status labels"""
        self.round_label.configure(text=f"Round {self.current_round} of {self.total_rounds}")
        
        # Update attempts label with color coding
        if self.attempts_left > 4:
            attempts_color = "#4CAF50"  # Green
        elif self.attempts_left > 2:
            attempts_color = "#FF9800"  # Orange
        else:
            attempts_color = "#F44336"  # Red
            
        self.attempts_label.configure(
            text=f"Attempts left: {self.attempts_left}",
            text_color=attempts_color
        )
        
        # Update hints label
        hints_color = "#FF9800" if self.hints_left > 0 else "#757575"
        self.hints_label.configure(
            text=f"Hints left: {self.hints_left}",
            text_color=hints_color
        )
        
        # Enable/disable hint button
        self.hint_button.configure(state="normal" if self.hints_left > 0 and self.game_active else "disabled")
        
    def make_guess(self):
        """Process the player's guess"""
        if not self.game_active:
            return
            
        # Get and sanitize input
        raw_input = self.guess_entry.get()
        sanitized_guess, error_message = self.sanitize_input(raw_input)
        
        if error_message:
            self.add_message(error_message)
            self.log_attempt(raw_input, is_valid=False)
            return
            
        # Validate game range
        if sanitized_guess < 0 or sanitized_guess > 100:
            self.add_message("❌ Number must be between 0 and 100!")
            self.log_attempt(sanitized_guess, is_valid=False)
            return
            
        # Log valid attempt
        self.log_attempt(sanitized_guess, is_valid=True)
        
        # Track the guess for strategy
        self.previous_guesses.append(sanitized_guess)
        
        self.attempts_left -= 1
        
        if sanitized_guess == self.secret_number:
            self.add_message(f"🎉 Correct! You won! The number was {self.secret_number}")
            self.wins += 1
            self.end_round(True)
        else:
            if sanitized_guess < self.secret_number:
                self.add_message(f"📈 {sanitized_guess} is too low!")
                self.min_possible = max(self.min_possible, sanitized_guess + 1)
            else:
                self.add_message(f"📉 {sanitized_guess} is too high!")
                self.max_possible = min(self.max_possible, sanitized_guess - 1)
                
            if self.attempts_left == 0:
                self.add_message(f"💀 Game Over! The number was {self.secret_number}")
                self.end_round(False)
            else:
                self.add_message(f"🎯 Try again! {self.attempts_left} attempts remaining.")
                range_size = self.max_possible - self.min_possible + 1
                self.add_message(f"🔍 Possible range: {self.min_possible} to {self.max_possible} ({range_size} numbers left)")
                
        self.update_labels()
        self.guess_entry.delete(0, "end")
        
    def get_hint(self):
        """Provide a hint to the player"""
        if not self.game_active or self.hints_left == 0:
            return
            
        self.hints_left -= 1
        hint_message = self.generate_hint(self.secret_number, self.hint_level)
        self.add_message(f"💡 Hint: {hint_message}")
        self.hint_level += 1
        self.update_labels()
        
    def generate_hint(self, number, hint_level):
        """Generate a hint based on the hint level - improved for better strategy"""
        if hint_level == 0:
            # First hint: Split the range in half
            return "The number is less than 50" if number < 50 else "The number is 50 or greater"
        elif hint_level == 1:
            # Second hint: Give a more specific quarter range
            if number < 25:
                return "The number is between 0 and 25"
            elif number < 50:
                return "The number is between 25 and 50"
            elif number < 75:
                return "The number is between 50 and 75"
            else:
                return "The number is between 75 and 100"
        elif hint_level == 2:
            # Third hint: Give an even more specific range (roughly 12-13 numbers)
            if number < 13:
                return "The number is between 0 and 12"
            elif number < 25:
                return "The number is between 13 and 25"
            elif number < 38:
                return "The number is between 25 and 38"
            elif number < 50:
                return "The number is between 38 and 50"
            elif number < 63:
                return "The number is between 50 and 63"
            elif number < 75:
                return "The number is between 63 and 75"
            elif number < 88:
                return "The number is between 75 and 88"
            else:
                return "The number is between 88 and 100"
        else:
            # Bonus hint: Give a very specific range (about 6-7 numbers)
            if number < 7:
                return "The number is between 0 and 6"
            elif number < 13:
                return "The number is between 7 and 13"
            elif number < 19:
                return "The number is between 13 and 19"
            elif number < 25:
                return "The number is between 19 and 25"
            elif number < 31:
                return "The number is between 25 and 31"
            elif number < 38:
                return "The number is between 31 and 38"
            elif number < 44:
                return "The number is between 38 and 44"
            elif number < 50:
                return "The number is between 44 and 50"
            elif number < 56:
                return "The number is between 50 and 56"
            elif number < 63:
                return "The number is between 56 and 63"
            elif number < 69:
                return "The number is between 63 and 69"
            elif number < 75:
                return "The number is between 69 and 75"
            elif number < 81:
                return "The number is between 75 and 81"
            elif number < 88:
                return "The number is between 81 and 88"
            elif number < 94:
                return "The number is between 88 and 94"
            else:
                return "The number is between 94 and 100"
            
    def end_round(self, won):
        """End the current round"""
        self.game_active = False
        
        if self.current_round < self.total_rounds:
            self.current_round += 1
            self.add_message("⏳ Starting next round in 3 seconds...")
            # Use threading to avoid blocking the GUI
            threading.Thread(target=self.delayed_next_round, daemon=True).start()
        else:
            self.add_message("🏁 Session complete!")
            self.show_stats()
            
    def delayed_next_round(self):
        """Start the next round after a delay"""
        time.sleep(3)
        self.root.after(0, self.start_new_game)
        
    def new_session(self):
        """Start a new game session"""
        dialog = ctk.CTkInputDialog(
            text="How many rounds would you like to play?",
            title="New Session"
        )
        
        raw_input = dialog.get_input()
        if raw_input is None:  # User cancelled
            return
            
        # Sanitize the input
        sanitized_rounds, error_message = self.sanitize_rounds_input(raw_input)
        
        if error_message:
            messagebox.showerror("Invalid Input", error_message)
            return
            
        # Reset session variables
        self.total_rounds = sanitized_rounds
        self.current_round = 1
        self.wins = 0
        
        # Clear messages
        self.messages_text.configure(state="normal")
        self.messages_text.delete("1.0", "end")
        self.messages_text.configure(state="disabled")
        
        self.add_message(f"🎮 New session started with {sanitized_rounds} rounds!")
        self.start_new_game()
        
    def show_stats(self):
        """Show game statistics"""
        win_rate = (self.wins / self.total_rounds) * 100 if self.total_rounds > 0 else 0
        
        stats_message = f"""
🏆 Game Statistics

Wins: {self.wins}
Total Rounds: {self.total_rounds}
Win Rate: {win_rate:.1f}%

{"🎉 Excellent performance!" if win_rate >= 75 else 
 "👍 Good job!" if win_rate >= 50 else 
 "💪 Keep practicing!"}
        """
        
        messagebox.showinfo("Statistics", stats_message)
        
    def sanitize_input(self, user_input):
        """Sanitize and validate user input"""
        if not user_input:
            return None, "❌ Input cannot be empty!"
            
        # Remove whitespace and convert to string
        sanitized = str(user_input).strip()
        
        # Check for malicious characters or patterns
        dangerous_chars = ['<', '>', '&', '"', "'", '\\', '/', ';', '|', '`', '$']
        if any(char in sanitized for char in dangerous_chars):
            return None, "❌ Invalid characters detected!"
            
        # Check length limit
        if len(sanitized) > 10:
            return None, "❌ Input too long! Maximum 10 characters."
            
        # Remove non-numeric characters except minus sign
        cleaned = ''.join(char for char in sanitized if char.isdigit() or char == '-')
        
        if not cleaned:
            return None, "❌ Please enter a valid number!"
            
        try:
            # Convert to integer
            number = int(cleaned)
            
            # Validate range
            if number < -999 or number > 999:
                return None, "❌ Number out of acceptable range!"
                
            return number, None
            
        except ValueError:
            return None, "❌ Please enter a valid integer!"
    
    def sanitize_rounds_input(self, user_input):
        """Sanitize input for number of rounds"""
        if not user_input:
            return None, "❌ Please enter number of rounds!"
            
        # Remove whitespace and convert to string
        sanitized = str(user_input).strip()
        
        # Check for dangerous characters
        if not sanitized.isdigit():
            return None, "❌ Please enter only numbers!"
            
        # Check length limit
        if len(sanitized) > 3:
            return None, "❌ Maximum 999 rounds allowed!"
            
        try:
            rounds = int(sanitized)
            
            # Validate range
            if rounds < 1:
                return None, "❌ Must be at least 1 round!"
            elif rounds > 999:
                return None, "❌ Maximum 999 rounds allowed!"
                
            return rounds, None
            
        except ValueError:
            return None, "❌ Please enter a valid number!"
    
    def log_attempt(self, guess, is_valid=True):
        """Log user attempts for monitoring"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        status = "VALID" if is_valid else "INVALID"
        
        # Simple logging - in a real application, you might want to use proper logging
        log_entry = f"[{timestamp}] {status} - Guess: {guess}"
        
        # Store in a simple list (in memory)
        if not hasattr(self, 'attempt_log'):
            self.attempt_log = []
        
        self.attempt_log.append(log_entry)
        
        # Keep only last 100 entries to prevent memory issues
        if len(self.attempt_log) > 100:
            self.attempt_log = self.attempt_log[-100:]
    
    def show_attempt_log(self):
        """Show the attempt log for debugging/monitoring"""
        if not hasattr(self, 'attempt_log') or not self.attempt_log:
            messagebox.showinfo("Attempt Log", "No attempts logged yet.")
            return
            
        # Show last 20 entries
        recent_logs = self.attempt_log[-20:]
        log_text = "🔍 RECENT ATTEMPTS LOG\n\n" + "\n".join(recent_logs)
        
        messagebox.showinfo("Attempt Log", log_text)
        
    def clear_attempt_log(self):
        """Clear the attempt log"""
        if hasattr(self, 'attempt_log'):
            self.attempt_log.clear()
            self.add_message("🗑️ Attempt log cleared!")
        
    def get_strategy_tip(self):
        """Provide strategic advice for the next guess"""
        if not self.game_active:
            return
            
        # Calculate the optimal next guess using binary search
        optimal_guess = (self.min_possible + self.max_possible) // 2
        
        # Check if this guess was already made
        if optimal_guess in self.previous_guesses:
            # Find the next best guess
            if optimal_guess + 1 <= self.max_possible and optimal_guess + 1 not in self.previous_guesses:
                optimal_guess = optimal_guess + 1
            elif optimal_guess - 1 >= self.min_possible and optimal_guess - 1 not in self.previous_guesses:
                optimal_guess = optimal_guess - 1
            else:
                # Find any number in range not guessed yet
                for num in range(self.min_possible, self.max_possible + 1):
                    if num not in self.previous_guesses:
                        optimal_guess = num
                        break
        
        range_size = self.max_possible - self.min_possible + 1
        
        strategy_message = f"🎯 Strategic Suggestion: Try {optimal_guess}\n"
        strategy_message += f"📊 This will divide the remaining {range_size} possibilities optimally!\n"
        strategy_message += f"🔍 Current range: {self.min_possible} to {self.max_possible}"
        
        if len(self.previous_guesses) == 0:
            strategy_message += "\n💡 Binary search tip: Always start with 50 to split the range in half!"
        elif range_size <= 3:
            strategy_message += "\n🎉 You're very close! Only a few numbers left!"
        
        self.add_message(strategy_message)
        
    def run(self):
        """Start the GUI application"""
        self.root.mainloop()

if __name__ == "__main__":
    game = GuessingGameGUI()
    game.run()
