"""
Tests package for the driving car simulation.

This module contains test cases for the driving car simulation functionality.
"""

import sys
import os

# Add the parent directory to the Python path so we can import the main module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the main car class for testing
try:
    from car import car
except ImportError:
    # Handle the case where the main module might not be available
    car = None

# Test configuration
TEST_CONFIG = {
    'verbose': True,
    'test_data_dir': os.path.join(os.path.dirname(__file__), 'test_data'),
    'temp_dir': os.path.join(os.path.dirname(__file__), 'temp')
}

# Common test utilities
def setup_test_environment():
    """Set up the test environment."""
    # Create temp directory if it doesn't exist
    os.makedirs(TEST_CONFIG['temp_dir'], exist_ok=True)

def teardown_test_environment():
    """Clean up the test environment."""
    # Clean up temp files if needed
    import shutil
    if os.path.exists(TEST_CONFIG['temp_dir']):
        shutil.rmtree(TEST_CONFIG['temp_dir'])

# Make important items available at package level
__all__ = ['car', 'TEST_CONFIG', 'setup_test_environment', 'teardown_test_environment']