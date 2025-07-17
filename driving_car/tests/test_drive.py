import sys
import os
import unittest

# Add the parent directory to Python path to import the car module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from car import Car


class DrivingCarTest(unittest.TestCase):
    def test_create_car(self):
        """Test car creation with valid and invalid names."""
        # Test valid car name (only letters)
        valid_name = "CarA"
        initial_position = [5, 5]
        initial_direction = 'N'
        car = Car(valid_name, initial_position, initial_direction)
        
        # Test that the car name is set correctly
        self.assertEqual(car.get_car_name(), valid_name)
        
        # Test that the name contains only letters
        self.assertTrue(car.get_car_name().isalpha(), 
                       f"Car name '{car.get_car_name()}' should contain only letters")
        
        # Test valid car names with different cases
        valid_names = ["A", "Tesla", "BMW", "Ford", "CarOne", "VehicleA"]
        for name in valid_names:
            test_car = Car(name, [0, 0], 'N')
            self.assertEqual(test_car.get_car_name(), name)
            self.assertTrue(test_car.get_car_name().isalpha(),
                           f"Car name '{name}' should contain only letters")
        
        # Test invalid car names - should raise ValueError
        invalid_names = ["5","Car123", "Car-A", "Car_B", "Car 1", "123", "Car@"]
        for invalid_name in invalid_names:
            with self.subTest(name=invalid_name):
                with self.assertRaises(ValueError):
                    Car(invalid_name, [0, 0], 'N')
        
    def test_move_left(self):
        """Test that the car moves left and updates position correctly."""
        # Initialize car at position (5, 5) facing North
        car_name = "TestCar"
        initial_position = [5, 5]
        initial_direction = 'N'
        car = Car(car_name, initial_position, initial_direction)
        
        # Get initial position (should be the position we set)
        initial_pos = car.get_car_position()
        self.assertEqual(initial_pos[0], 5)  # x coordinate should be 5
        self.assertEqual(initial_pos[1], 5)  # y coordinate should be 5
        
        # Test moving left (turn left)
        car.move('L')
        
        # After turning left, the car should be facing West
        current_pos = car.get_car_position()
        self.assertEqual(current_pos[0], 5)  # x should remain same
        self.assertEqual(current_pos[1], 5)  # y should remain same
        self.assertEqual(car.get_facing(), 'W')  # should now face West
        
        # Move forward after turning left (should move West, decreasing x)
        car.move('F')
        final_pos = car.get_car_position()
        self.assertEqual(final_pos[0], 4)  # x should decrease when moving West
        self.assertEqual(final_pos[1], 5)  # y should remain same  
    def test_move_right(self):
        """Test that the car moves right and updates position correctly."""
        # Initialize car at position (5, 5) facing North
        car_name = "TestCar"
        initial_position = [5, 5]
        initial_direction = 'N'
        car = Car(car_name, initial_position, initial_direction)
        
        # Get initial position (should be the position we set)
        initial_pos = car.get_car_position()
        self.assertEqual(initial_pos[0], 5)  # x coordinate should be 5
        self.assertEqual(initial_pos[1], 5)  # y coordinate should be 5
        
        # Test moving right (should turn from North to East)
        car.move('R')
        current_pos = car.get_car_position()
        self.assertEqual(current_pos[0], 5)  # x should remain same
        self.assertEqual(current_pos[1], 5)  # y should remain same
        self.assertEqual(car.get_facing(), 'E')  # should now face East
        
        # Move forward after turning right (should move East, increasing x)
        car.move('F')
        final_pos = car.get_car_position()
        self.assertEqual(final_pos[0], 6)  # x should increase when moving East
        self.assertEqual(final_pos[1], 5)  # y should remain same
        
    def test_move_forward(self):
        """Test that the car moves forward correctly."""
        car = Car("ForwardCar", [0, 0], 'N')
        initial_pos = car.get_car_position()
        
        # Move forward (North direction should increase y)
        car.move('F')
        final_pos = car.get_car_position()
        
        self.assertEqual(final_pos[0], 0)  # x should remain same
        self.assertEqual(final_pos[1], 1)  # y should increase
        
    def test_valid_position(self):
        """Test that car can be created with valid positions."""
        valid_positions = [[0, 0], [5, 5], [-3, 2], [10, -5]]
        for pos in valid_positions:
            car = Car("TestCar", pos, 'N')
            car_pos = car.get_car_position()
            self.assertEqual(car_pos[0], pos[0])
            self.assertEqual(car_pos[1], pos[1])
            
    def test_invalid_position(self):
        """Test handling of edge cases for positions."""
        # Test with very large coordinates
        car = Car("TestCar", [1000, -1000], 'S')
        pos = car.get_car_position()
        self.assertEqual(pos[0], 1000)
        self.assertEqual(pos[1], -1000)
        
    def test_setup_field(self):
        """Test that car can be properly initialized on a field."""
        car = Car("FieldCar", [3, 7], 'E')
        self.assertEqual(car.get_car_name(), "FieldCar")
        self.assertEqual(car.get_car_position(), (3, 7))
        self.assertEqual(car.get_facing(), 'E')
        
    def test_invalid_field(self):
        """Test car behaviour with various field scenarios."""
        # Test car with different directions
        directions = ['N', 'S', 'E', 'W']
        for direction in directions:
            car = Car("TestCar", [0, 0], direction)
            self.assertEqual(car.get_facing(), direction)
                
    def test_check_collision(self):
        """Test collision detection functionality."""
        # Create two cars that will collide
        car1 = Car("A", [0, 0], 'N')
        car2 = Car("B", [0, 1], 'S')
        
        # Test initial positions are different
        initial_pos1 = car1.get_car_position()
        initial_pos2 = car2.get_car_position()
        self.assertNotEqual(initial_pos1, initial_pos2)
        
        # Move car1 forward (North) - should go to (0, 1)
        car1.move('F')
        # Move car2 forward (South) - should go to (0, 0)
        car2.move('F')
        
        # Check positions after first move
        pos1_after_move = car1.get_car_position()
        pos2_after_move = car2.get_car_position()
        self.assertEqual(pos1_after_move, (0, 1))
        self.assertEqual(pos2_after_move, (0, 0))
        
        # Now move them again - they should collide
        car1.move('F')  # car1 now at (0, 2)
        car2.move('F')  # car2 now at (0, -1)
        
        # Test that cars can be at same position/collision
        car3 = Car("C", [5, 5], 'N')
        car4 = Car("D", [5, 5], 'S')  # Same initial position
        
        pos3 = car3.get_car_position()
        pos4 = car4.get_car_position()
        self.assertEqual(pos3, pos4)  # This should be a collision
        
    def test_collision_detection_logic(self):
        """Test the collision detection logic specifically."""
        # Test positions for collision detection
        positions = {
            'A': (5, 4),
            'B': (5, 4),  # Same position as A - collision
            'C': (3, 2)   # Different position - no collision
        }
        
        collision_results = []
        
        # Manually check for collisions (simulating the check_collisions function logic)
        car_names = list(positions.keys())
        collisions_found = False
        new_collided_cars = set()
        
        for i in range(len(car_names)):
            for j in range(i + 1, len(car_names)):
                car1_name = car_names[i]
                car2_name = car_names[j]
                car1_pos = positions[car1_name]
                car2_pos = positions[car2_name]
                
                if car1_pos == car2_pos:
                    collisions_found = True
                    new_collided_cars.add(car1_name)
                    new_collided_cars.add(car2_name)
                    collision_results.append(f"{car1_name} collides with {car2_name} at {car1_pos}")
                    collision_results.append(f"{car2_name} collides with {car1_name} at {car2_pos}")
        
        # Should find collision between A and B
        self.assertTrue(collisions_found)
        self.assertTrue(any("A collides with B" in result for result in collision_results))
        self.assertTrue(any("B collides with A" in result for result in collision_results))
        self.assertIn('A', new_collided_cars)
        self.assertIn('B', new_collided_cars)
        self.assertNotIn('C', new_collided_cars)
        
    def test_collision_stops_cars(self):
        """Test that collided cars stop executing commands."""
        # Create three cars
        car1 = Car("A", [0, 0], 'N')
        car2 = Car("B", [0, 1], 'S') 
        car3 = Car("C", [5, 5], 'E')
            
        # Simulate collision detection
        collided_cars = set()
        
        # Move cars - A and B will collide, C continues
        car1.move('F')  # A moves to (0, 1)
        car2.move('F')  # B moves to (0, 0)
        car3.move('F')  # C moves to (6, 5)
            
        # Check positions after move
        positions = {
            'A': car1.get_car_position(),
            'B': car2.get_car_position(), 
            'C': car3.get_car_position()
        }
            
        # Simulate another step where A and B would collide if they move again
        initial_c_pos = car3.get_car_position()
            
        # Only move C (since A and B would be in collided_cars set)
        car3.move('F')  # C continues to (7, 5)
            
        final_c_pos = car3.get_car_position()
            
        # Verify C continued moving while A and B would be stopped
        self.assertNotEqual(initial_c_pos, final_c_pos)
        self.assertEqual(final_c_pos, (7, 5))    
        
    def test_boundary_checking_negative_coordinates(self):
        """Test that cars cannot move to negative coordinates."""
        # Create a car at edge position
        car = Car("BoundaryTest", [0, 0], 'S') 
        
        # move South (should fail)
        with self.assertRaises(ValueError) as context:
            car.move('F')
        
        self.assertIn("cannot move to negative coordinates", str(context.exception))
        self.assertIn("(0, -1)", str(context.exception))
        
        # Return car to origin
        self.assertEqual(car.get_car_position(), (0, 0))
        
        # move West from origin (should also fail)
        car_west = Car("BoundaryTestWest", [0, 0], 'W')
        with self.assertRaises(ValueError) as context:
            car_west.move('F')
        
        self.assertIn("cannot move to negative coordinates", str(context.exception))
        self.assertIn("(-1, 0)", str(context.exception))
        
    def test_boundary_checking_field_bounds(self):
        """Test that cars cannot move outside field bounds."""
        # Create a 5x5 field
        field_bounds = (5, 5)
        
        # move East
        car_east = Car("EdgeEast", [4, 2], 'E', field_bounds)
        with self.assertRaises(ValueError) as context:
            car_east.move('F')
        
        self.assertIn("cannot move outside field bounds", str(context.exception))
        self.assertIn("(5, 2)", str(context.exception))
        
        # Test car at top edge trying to move North
        car_north = Car("EdgeNorth", [2, 4], 'N', field_bounds)
        with self.assertRaises(ValueError) as context:
            car_north.move('F')
        
        self.assertIn("cannot move outside field bounds", str(context.exception))
        self.assertIn("(2, 5)", str(context.exception))
        
        # remain unchanged after failed moves
        self.assertEqual(car_east.get_car_position(), (4, 2))
        self.assertEqual(car_north.get_car_position(), (2, 4))
        
    def test_boundary_checking_valid_moves(self):
        """Test that valid moves within boundaries work correctly."""
        field_bounds = (10, 10)
        
        # Test car can move within bounds
        car = Car("ValidMoves", [5, 5], 'N', field_bounds)
        
        # Move North (should succeed)
        car.move('F')
        self.assertEqual(car.get_car_position(), (5, 6))
        
        # Move East
        car.move('R')
        car.move('F')
        self.assertEqual(car.get_car_position(), (6, 6))
        
        # Move South
        car.move('R')
        car.move('F')
        self.assertEqual(car.get_car_position(), (6, 5))
        
        # Move West
        car.move('R')
        car.move('F')
        self.assertEqual(car.get_car_position(), (5, 5))
        
    def test_boundary_edge_cases(self):
        """Test boundary checking edge cases."""
        field_bounds = (3, 3)  # Small 3x3 field
        
        # Test car at corner positions
        corners = [
            ([0, 0], 'S', "South from origin"),
            ([0, 0], 'W', "West from origin"),
            ([2, 2], 'N', "North from top-right"),
            ([2, 2], 'E', "East from top-right")
        ]
        
        for position, direction, description in corners:
            with self.subTest(case=description):
                car = Car("CornerTest", position, direction, field_bounds)
                
                with self.assertRaises(ValueError):
                    car.move('F')
                
                # Position should remain unchanged
                self.assertEqual(car.get_car_position(), tuple(position))
                
    def test_no_boundary_checking_when_disabled(self):
        """Test that cars can move to negative coordinates when boundary checking is disabled."""
        # Create car without field bounds
        car = Car("NoBounds", [1, 1], 'S') 
        
        # move to negative coordinates
        car.move('F')  # Move to (1, 0)
        self.assertEqual(car.get_car_position(), (1, 0))
        
        car.move('F')  
        self.assertEqual(car.get_car_position(), (1, -1))
            
if __name__ == '__main__':
   unittest.main()