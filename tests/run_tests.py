#!/usr/bin/env python3
"""
Test runner for the Number Guessing Game
This script provides an easy way to run all tests with different options
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"Command: {command}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        print(f"Return code: {e.returncode}")
        if e.stdout:
            print(f"STDOUT: {e.stdout}")
        if e.stderr:
            print(f"STDERR: {e.stderr}")
        return False

def check_pytest_installed():
    """Check if pytest is installed"""
    try:
        import pytest
        print(f"✓ pytest is installed (version: {pytest.__version__})")
        return True
    except ImportError:
        print("✗ pytest is not installed")
        return False

def install_pytest():
    """Install pytest if not installed"""
    if not check_pytest_installed():
        print("\nInstalling pytest...")
        success = run_command("pip install pytest", "Installing pytest")
        if success:
            print("✓ pytest installed successfully")
        else:
            print("✗ Failed to install pytest")
            return False
    return True

def run_tests(test_type="all", verbose=False, coverage=False):
    """Run tests based on the specified type"""
    
    # Ensure pytest is installed
    if not install_pytest():
        return False
    
    # Base pytest command
    cmd = "python -m pytest"
    
    # Add verbosity
    if verbose:
        cmd += " -v"
    else:
        cmd += " -q"
    
    # Add coverage if requested
    if coverage:
        cmd += " --cov=game --cov-report=html --cov-report=term-missing"
    
    # Add specific test patterns based on type
    if test_type == "unit":
        cmd += " tests/test_game_logic.py"
        description = "Unit Tests"
    elif test_type == "integration":
        cmd += " tests/test_integration.py"
        description = "Integration Tests"
    elif test_type == "performance":
        cmd += " tests/test_performance.py"
        description = "Performance Tests"
    elif test_type == "fast":
        cmd += " -m 'not slow'"
        description = "Fast Tests (excluding slow tests)"
    elif test_type == "slow":
        cmd += " -m 'slow'"
        description = "Slow Tests"
    else:
        cmd += " tests/"
        description = "All Tests"
    
    # Run the tests
    return run_command(cmd, description)

def lint_code():
    """Run code linting (if available)"""
    print("\nChecking code quality...")
    
    # Try flake8
    try:
        import flake8
        success = run_command("flake8 game.py tests/", "Code linting with flake8")
        if success:
            print("✓ Code passes flake8 checks")
    except ImportError:
        print("flake8 not installed, skipping linting")
    
    # Try black (code formatting check)
    try:
        import black
        success = run_command("black --check game.py tests/", "Code formatting check with black")
        if success:
            print("✓ Code formatting is correct")
    except ImportError:
        print("black not installed, skipping formatting check")

def generate_test_report():
    """Generate a comprehensive test report"""
    print("\nGenerating comprehensive test report...")
    
    if not install_pytest():
        return False
    
    # Create reports directory
    reports_dir = Path("test_reports")
    reports_dir.mkdir(exist_ok=True)
    
    # Run tests with HTML report
    cmd = f"python -m pytest tests/ --html={reports_dir}/test_report.html --self-contained-html"
    success = run_command(cmd, "Generating HTML test report")
    
    if success:
        print(f"✓ Test report generated: {reports_dir}/test_report.html")
    
    return success

def main():
    """Main function to handle command line arguments"""
    parser = argparse.ArgumentParser(description="Test runner for Number Guessing Game")
    
    parser.add_argument(
        "--type", 
        choices=["all", "unit", "integration", "performance", "fast", "slow"],
        default="all",
        help="Type of tests to run"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Run tests with verbose output"
    )
    
    parser.add_argument(
        "--coverage", "-c",
        action="store_true",
        help="Run tests with coverage analysis"
    )
    
    parser.add_argument(
        "--lint", "-l",
        action="store_true",
        help="Run code linting"
    )
    
    parser.add_argument(
        "--report", "-r",
        action="store_true",
        help="Generate HTML test report"
    )
    
    parser.add_argument(
        "--install-deps",
        action="store_true",
        help="Install test dependencies"
    )
    
    args = parser.parse_args()
    
    print("Number Guessing Game - Test Runner")
    print("=" * 50)
    
    # Install dependencies if requested
    if args.install_deps:
        print("Installing test dependencies...")
        deps = ["pytest", "pytest-html", "pytest-cov", "coverage"]
        for dep in deps:
            run_command(f"pip install {dep}", f"Installing {dep}")
    
    # Run linting if requested
    if args.lint:
        lint_code()
    
    # Run tests
    success = run_tests(args.type, args.verbose, args.coverage)
    
    # Generate report if requested
    if args.report:
        generate_test_report()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
