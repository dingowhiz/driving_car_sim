#!/usr/bin/env python3
"""
Test script to verify command sequence functionality
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from car import Car
from main import process_command, add_car_to_list, add_command_to_car, cars_list

def test_command_sequences():
    print("Testing Command Sequence Functionality")
    print("=" * 50)
    
    # Create a test car
    car = Car("TestCar", [5, 5], 'N')
    add_car_to_list(car)
    
    print(f"Initial car state:")
    pos = car.get_car_position()
    print(f"  Position: ({pos[0]}, {pos[1]}), Facing: {car.get_facing()}")
    
    # Test sequence command
    print(f"\nTesting command sequence: FFRFFLF")
    process_command(car, "FFRFFLF")
    
    print(f"\nFinal car state:")
    pos = car.get_car_position()
    print(f"  Position: ({pos[0]}, {pos[1]}), Facing: {car.get_facing()}")
    
    # Show command history
    print(f"\nCommand history:")
    for car_data in cars_list:
        if car_data['car'] == car:
            commands_str = ''.join(car_data['commands'])
            print(f"  Commands executed: {commands_str}")
            break

if __name__ == "__main__":
    test_command_sequences()
