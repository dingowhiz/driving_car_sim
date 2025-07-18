#!/usr/bin/env python3
"""
Driving Car Simulation - Main Program

This is the main entry point for the driving car simulation program.
It demonstrates car creation, movement, and position tracking in a grid.
"""

import sys
import os

# Add the current directory to Python path to import our modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from car import Car

# Global list to store all cars
cars_list = []

def display_welcome():
    """Display welcome message and program information."""
    print("=" * 60)
    print("            Welcome to Auto Driving Car Simulation!")
    print("=" * 60)
    print("This program simulates a car driving on a grid.")
    print("Input format: Enter position as 'x y N' (e.g., '5 3 N')")
    print("\nCommands:")
    print("  L - Turn Left")
    print("  R - Turn Right")
    print("  F - Move Forward")
    print("\nYou can also enter command sequences:")
    print("  FFRFFLF - Execute multiple commands at once")
    print("  LLF - Turn left twice, then move forward")
    print("=" * 60)

def get_field_input():
    '''Get field input from user'''
    x, y = input("Please enter the width and height (e.g., '10 10'): ").strip().split()
    print(f"You have created a field of {x} x {y}.")
    return int(x), int(y)
    
def display_car_status(car):
    """Display current car status."""
    position = car.get_car_position()
    print(f"\nCar Status:")
    print(f"  Name: {car.get_car_name()}")
    print(f"  Position: ({position[0]}, {position[1]})")
    print(f"  Facing: {car.get_facing()}")


def display_cars_list():
    """Display current list of cars in format 'A, (x,y) N, FFLFRFF'."""
    if not cars_list:
        print("\nNo cars in the simulation.")
        return
    
    print("\nCurrent Cars:")
    for car_data in cars_list:
        car = car_data['car']
        commands = car_data['commands']
        position = car.get_car_position()
        commands_str = ''.join(commands) if commands else ''
        print(f"- {car.get_car_name()}, ({position[0]},{position[1]}) {car.get_facing()}, {commands_str}")
def add_car_to_list(car):
    """Add a car to the global cars list."""
    cars_list.append({
        'car': car,
        'name': car.get_car_name(),
        'position': car.get_car_position(),
        'facing': car.get_facing(),
        'commands': []
    })

def add_command_to_car(car, command):
    """Add a command to a car."""
    car_name = car.get_car_name() if hasattr(car, 'get_car_name') else str(car)
    for car_data in cars_list:
        if car_data['name'] == car_name:
            if isinstance(car_data['commands'], list):
                car_data['commands'].append(command)
            else:
                car_data['commands'] = [command]
            print(f"Command '{command}' added to car {car_name}")
            break
    else:
        print(f"Car {car_name} not found in cars list")
def get_user_commands(car):
    """Get commands from user and process them for the car."""
    display_car_status(car)
    
    while True:
        command = input(f"\nPlease enter the commands in sequence for car {car} (e.g., F, LLF, FFRFFLF): ").strip()
    
        # Validate the command sequence
        #valid_moves = set(['L', 'R', 'F'])
        if process_command(car, command):
            print(f"Commands '{command}' have been set for car {car.get_car_name()}.")
            return command
        else:
            print("Command processing failed. Please try again.")
            retry = input("Would you like to try again? (y/n): ").strip().lower()
            if retry != 'y':
                return None
            
def validate_car_name(name):
    """Validate that car name contains only letters."""
    if not name:
        return False, "Car name cannot be empty"
    if not name.isalpha():
        return False, "Car name must contain only letters"
    return True, "Valid name"


def get_car_input(field_bounds=None):
    """Get car creation input from user in format 'x y N'."""
    while True:
        name = input("\nEnter car name (letters only): ").strip()
        is_valid, message = validate_car_name(name)
        
        if is_valid:
            break
        else:
            print(f"Error: {message}. Please try again.")
    
    while True:
        try:
            position_input = input("Please enter initial position of car A in x y Direction format (e.g.'2 3 N'): ").strip()
            parts = position_input.split()
            
            if len(parts) != 3:
                raise ValueError("Invalid format. Use 'x y direction' (e.g., '5 3 N')")
            
            x = int(parts[0])
            y = int(parts[1])
            direction = parts[2].upper()
            
            if direction not in ['N', 'S', 'E', 'W']:
                raise ValueError("Direction must be N, S, E, or W")
            
             # Check for negative coordinates
            if x < 0 or y < 0:
                raise ValueError(f"Position cannot have negative coordinates: ({x}, {y})")
            
            # Check field bounds if provided
            if field_bounds:
                width, height = field_bounds
                if x >= width or y >= height:
                    raise ValueError(f"Position ({x}, {y}) is outside field bounds ({width-1}, {height-1})")
            
            # Create the car with field bounds and add to list
            car = Car(name, [x, y], direction, field_bounds)
            add_car_to_list(car)
            print(f"Car {name} created successfully!")
            
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")
    
    return car

def process_command(car, command):
    """Process a movement command or sequence of commands and return result."""
    command = command.upper().strip()
    
    # Check if it's a sequence of movement commands
    valid_moves = set(['L', 'R', 'F'])
    if all(c in valid_moves for c in command):
        try:
            print(f"Processing command sequence: {command}")
            
            # Add command to car's history
            add_command_to_car(car, command)
            
            for i, single_command in enumerate(command):    
                # Execute the movement
                car.move(single_command)
                
                # Show feedback for each command
                if single_command == 'L':
                    action = "turned left"
                elif single_command == 'R':
                    action = "turned right"
                elif single_command == 'F':
                    action = "moved forward"
                
                pos = car.get_car_position()
                print(f"  Step {i+1}: {single_command} - Car {action}. Position: ({pos[0]}, {pos[1]}), Facing: {car.get_facing()}")
            
            print(f"Command sequence completed!")
            return True
               
        except ValueError as e:
            print(f"Error executing command sequence: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error during command execution: {e}")
            return False 
    
    # Handle single commands
    elif command in valid_moves:
        try:
            add_command_to_car(car, command)
            
            car.move(command)
            
            if command == 'L':
                print(f"Car turned left. Now facing: {car.get_facing()}")
            elif command == 'R':
                print(f"Car turned right. Now facing: {car.get_facing()}")
            elif command == 'F':
                print(f"Car moved forward.")
            return True
        
        except ValueError as e:
            print(f"Error executing command '{command}': {e}")
            return False  # Failed due to boundary violation or invalid command
        except Exception as e:
            print(f"Unexpected error executing command '{command}': {e}")
            return False  # Failed due to unexpected error
   
    else:
        print("Invalid command. Use:")
        print("  - Single commands: L (left), R (right), F (forward)")
        print("  - Command sequences: FFRFFLF (multiple moves at once)")
        print("  - Special commands: LIST (show cars), Q (quit)")
        return True

def check_collisions(current_positions, step_number, collision_results):
    """Check for collisions between cars at current step."""
    collision_found = False
    new_collided_cars = set()
    car_names = list(current_positions.keys())
    
    # Check each pair of cars for collision
    for i in range(len(car_names)):
        for j in range(i + 1, len(car_names)):
            car1_name = car_names[i]
            car2_name = car_names[j]
            car1_pos = current_positions[car1_name]
            car2_pos = current_positions[car2_name]
            
            # Check if cars are at the same position
            if car1_pos == car2_pos:
                collision_found = True
                new_collided_cars.add(car1_name)
                new_collided_cars.add(car2_name)
                
                collision_msg1 = f"{car1_name}, collides with {car2_name} at ({car1_pos[0]},{car1_pos[1]}) at step {step_number}"
                collision_msg2 = f"{car2_name}, collides with {car1_name} at ({car2_pos[0]},{car2_pos[1]}) at step {step_number}"
                
                # Check if this collision has already been recorded (avoid duplicates)
                collision_exists = any(
                    ((car1_name in result and car2_name in result) or (car2_name in result and car1_name in result)) 
                    and f"({car1_pos[0]},{car1_pos[1]})" in result
                    for result in collision_results
                )
                
                if not collision_exists:
                    collision_results.append(collision_msg1)
                    collision_results.append(collision_msg2)
                    print(f"\n*** COLLISION DETECTED at step {step_number} ***")
                    print(f"Cars {car1_name} and {car2_name} collided at position ({car1_pos[0]},{car1_pos[1]})")
    
    return collision_found, new_collided_cars

def run_simulation():
    """Run the main simulation loop."""
    try:
        if not cars_list:
            print("No cars available. Please add a car first.")
            return 1
        
        print("\n" + "=" * 50)
        print("      RUNNING SIMULATION")
        print("=" * 50)
          
        # Execute commands for each car that has commands
        cars_with_commands = [car_data for car_data in cars_list if car_data['commands']]
        
        if not cars_with_commands:
            print("No cars have commands to execute.")
            print("Please add commands to cars first by selecting option 1 and adding commands.")
            return 1
        
        # Track all car positions during simulation for collision detection
        collision_results = []
        collided_cars = set() 
        boundary_violated_cars = set()
         
        # Find the maximum number of commands across all cars
        max_commands = 0
        for car_data in cars_with_commands:
            total_commands = sum(len(cmd_seq) for cmd_seq in car_data['commands'])
            max_commands = max(max_commands, total_commands)
            
        # Execute commands step by step for all cars simultaneously
        step_number = 0
        car_command_indices = {car_data['name']: {'seq_idx': 0, 'cmd_idx': 0} for car_data in cars_with_commands}
        
        print("\nExecuting commands for all cars simultaneously:")
  
        for step in range(max_commands):
            step_number += 1
            current_positions = {}
                           
            # Execute one command for each car if they have commands remaining
            for car_data in cars_with_commands:
                car = car_data['car']
                car_name = car.get_car_name()
                commands = car_data['commands']
                indices = car_command_indices[car_name]
                
                # Skip this car if it has already collided
                if car_name in collided_cars:
                    current_positions[car_name] = car.get_car_position()
                    continue
                
                # Check if this car still has commands to execute
                if indices['seq_idx'] < len(commands):
                    current_sequence = commands[indices['seq_idx']]
                    
                    if indices['cmd_idx'] < len(current_sequence):
                        # Execute the next command
                        single_command = current_sequence[indices['cmd_idx']]
                        
                        try:
                            car.move(single_command)
                            # Show feedback for each command
                            if single_command == 'L':
                                action = "turned left"
                            elif single_command == 'R':
                                action = "turned right"
                            elif single_command == 'F':
                                action = "moved forward"
                        
                            pos = car.get_car_position()
                            print(f"  Step {step_number}: {car_name} - {single_command} - {action}. Position: ({pos[0]}, {pos[1]}), Facing: {car.get_facing()}")
                            
                        except ValueError as e:
                            boundary_violated_cars.add(car_name)
                            print(f"  Step {step_number}: {car_name} - {single_command} - BOUNDARY VIOLATION!")
                            print(f"    Error: {e}")
                            print(f"    Car {car_name} has been stopped.")

                        # Move to next command
                        indices['cmd_idx'] += 1
                        
                        if indices['cmd_idx'] >= len(current_sequence):
                            indices['seq_idx'] += 1
                            indices['cmd_idx'] = 0
                            
                # Store current position for collision detection
                current_positions[car_name] = car.get_car_position()
            
            # Check for collisions at this step
            collision_found, new_collided_cars = check_collisions(current_positions, step_number, collision_results)
            
             # Add newly collided cars to the set of stopped cars
            if new_collided_cars:
                collided_cars.update(new_collided_cars)
                print(f"  Cars {', '.join(new_collided_cars)} have been stopped due to collision.") 
        
        print("\n" + "=" * 50)
        print("      SIMULATION COMPLETED")
        print("=" * 50)
        
        # Show final state of all cars
        print("\nFinal simulation state:")
        for car_data in cars_with_commands:
            car = car_data['car']
            car_name = car.get_car_name()
            status = ""
            if car_name in collided_cars:
                status = " (STOPPED - COLLIDED)"
            elif car_name in boundary_violated_cars:
                status = " (STOPPED - BOUNDARY VIOLATION)"
            
            print(f"- {car_name}: Final position {car.get_car_position()}, Facing: {car.get_facing()}{status}")
        
        # Display collision results
        if collision_results:
            print("\nAfter simulation, the result is:")
            for collision in collision_results:
                print(f"- {collision}")
        else:
            print("\nNo collisions detected during simulation.")
        
        # Display boundary violations
        if boundary_violated_cars:
            print(f"\nBoundary violations occurred for cars: {', '.join(boundary_violated_cars)}")
         
    except ValueError as ve:
        print(f"Error in simulation: {ve}")
        return 1
    except Exception as e:
        print(f"Unexpected error in simulation: {e}")
        return 1
    return 0


def check_final_collisions(final_positions, collision_results):
    """Check for collisions in final positions that might have been missed."""
    collision_found = False
    new_collided_cars = set()
    car_names = list(final_positions.keys())
    
    # Check each pair of cars for collision
    for i in range(len(car_names)):
        for j in range(i + 1, len(car_names)):
            car1_name = car_names[i]
            car2_name = car_names[j]
            car1_pos = final_positions[car1_name]
            car2_pos = final_positions[car2_name]
            
            # Check if cars are at the same position
            if car1_pos == car2_pos:
                collision_already_exists = any(
                    ((car1_name in result and car2_name in result) or (car2_name in result and car1_name in result))
                    and f"({car1_pos[0]},{car1_pos[1]})" in result
                    for result in collision_results
                )
       
                if not collision_already_exists:
                    collision_found = True
                    new_collided_cars.add(car1_name)
                    new_collided_cars.add(car2_name)
                    
                    collision_msg1 = f"{car1_name}, collides with {car2_name} at ({car1_pos[0]},{car1_pos[1]}) at final position"
                    collision_msg2 = f"{car2_name}, collides with {car1_name} at ({car2_pos[0]},{car2_pos[1]}) at final position"
                    collision_results.append(collision_msg1)
                    collision_results.append(collision_msg2)
                
                    print(f"\n*** FINAL COLLISION DETECTED ***")
                    print(f"Cars {car1_name} and {car2_name} ended at the same position ({car1_pos[0]},{car1_pos[1]})")
                else:
                    new_collided_cars.add(car1_name)
                    new_collided_cars.add(car2_name)
                    
    return collision_found, new_collided_cars

def run_demo():
    """Run a demonstration of the car simulation."""
    print("\n" + "=" * 50)
    print("      DEMO MODE")
    print("=" * 50)
    
    # Create demo cars
    demo_cars = [
        ("Tesla", [0, 0], 'N'),
        ("BMW", [5, 5], 'E'),
        ("Ford", [10, 3], 'S')
    ]
    
    for name, position, direction in demo_cars:
        print(f"\nCreating car: {name}")
        car = Car(name, position, direction)
        add_car_to_list(car)
        display_car_status(car)
        
        # Demo some movements
        print(f"\nDemo movements for {name}:")
        movements = ['F', 'F', 'L', 'F', 'R', 'F', 'F']
        for move in movements:
            print(f"  Command: {move}")
            add_command_to_car(car, move)
            car.move(move)
            pos = car.get_car_position()
            print(f"    Result: Position ({pos[0]}, {pos[1]}), Facing {car.get_facing()}")
    
    # Show final cars list
    print("\nFinal Cars List:")
    display_cars_list()


def main():
    """Main program entry point."""
    # if len(sys.argv) > 1 and sys.argv[1] == '--demo':
    #     run_demo()
    #     return 0
    display_welcome()
    
    # Create smulation field in x y format
    print("\nLet's create the simulation field!")
    field_width, field_height = get_field_input()
    field_bounds = (field_width, field_height)
    
    # Main program loop
    while True:
        # Show current cars list
        print("\nYour current list of cars are:")
        if not cars_list:
            print("- No cars in the simulation.")
        else:
            display_cars_list()
        
        # Display menu options
        print("\nPlease choose from the following options:"
          "\n  1. Add a car to field"
          "\n  2. Run simulation")
    
        choice = input("Enter your choice: ").strip()
    
        if choice == '1':
            try:
                car = get_car_input(field_bounds)
                command = get_user_commands(car)
                if command:
                #    add_command_to_car(car, command)
                    print(f"\nCar {car.get_car_name()} is ready for simulation!")
                else:
                    print(f"\nNo commands were added to car {car.get_car_name()}.")
  
            except Exception as e:
                print(f"Error adding car: {e}")
                continue
         
        elif choice == '2':
            try:
                if not cars_list:
                    print("\nNo cars available. Please add a car first.")
                    continue
                    
                # Run simulation
                result = run_simulation()
                
                # After simulation, ask if user wants to continue
                continue_choice = input("\nWould you like to continue? (y/n): ").strip().lower()
                if continue_choice != 'y':
                    print("\nThank you for using the Driving Car Simulation!")
                    break
                    
            except KeyboardInterrupt:
                print("\n\nProgram interrupted by user.")
                break
            except Exception as e:
                print(f"\nUnexpected error: {e}")
                continue
                
        else:
            print("Invalid choice. Please enter 1 or 2.")
            continue

if __name__ == "__main__":
    sys.exit(main())