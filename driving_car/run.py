#!/usr/bin/env python3
"""
Simple runner script for the driving car simulation.
Run this file to start the program.
"""

import os
import sys

# Add the directory containing our modules to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Import and run the main program
try:
    from main import main
    if __name__ == "__main__":
        sys.exit(main())
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Make sure all required files are in the same directory.")
    sys.exit(1)
