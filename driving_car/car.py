from dataclasses import replace

class Car(object):
    def __init__(self, name, position, direction, field_bounds=None):
        # Validate car name - only letters allowed
        if not name or not str(name).isalpha():
            raise ValueError(f"Car name must contain only letters. Invalid name: '{name}'")
        
        self.name = str(name)
        self.position = tuple(position) if isinstance(position, list) else position
        self.direction = str(direction)
        self.field_bounds = field_bounds
        
    def get_car_name(self) -> str:
        return str(self.name)
    
    def get_facing(self) -> str:
        return str(self.direction)
    
    def get_car_position(self) -> tuple:
        """
        Get the current position of the car in the grid.
        
        Returns:
            tuple: A tuple containing the x and y coordinates
                   Format: (x_coordinate, y_coordinate)
        """
        if hasattr(self, 'position') and len(self.position) >= 2:
            return (self.position[0], self.position[1])
        else:
            # Return default position if position is not properly set
            return (0, 0)
        
    def _is_valid_position(self, new_position):
        """Check if a position is valid."""
        x, y = new_position
        
        # Check for negative coordinates
        if x < 0 or y < 0:
            return False
            
        # Check field bounds if set
        if self.field_bounds:
            width, height = self.field_bounds
            if x >= width or y >= height:
                return False
                
        return True

    def move(self, commands):
        compass = ['N', 'E', 'S', 'W']
        vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # N, E, S, W movement vectors
        current = compass.index(self.direction)
        
        if commands == 'R':
            # Turn right: move clockwise in compass
            self.direction = compass[(current + 1) % 4]
        elif commands == 'L':
            # Turn left: move counter-clockwise in compass
            self.direction = compass[(current - 1) % 4]
        elif commands == 'F':
            # Move forward in current direction
            dx, dy = vectors[current]
            new_x = self.position[0] + dx
            new_y = self.position[1] + dy
            new_position = (new_x, new_y)
            
            # Check if the new position is valid
            if self._is_valid_position(new_position):
                self.position = new_position
            else:
                if new_x < 0 or new_y < 0:
                    raise ValueError(f"Car {self.name} cannot move to negative coordinates: ({new_x}, {new_y})")
                elif self.field_bounds:
                    width, height = self.field_bounds
                    raise ValueError(f"Car {self.name} cannot move outside field bounds: ({new_x}, {new_y}) exceeds ({width-1}, {height-1})")
                else:
                    raise ValueError(f"Car {self.name} cannot move to invalid position: ({new_x}, {new_y})")
        else:
            raise ValueError(f"Invalid command: {commands}. Use 'F' for forward, 'L' for left, 'R' for right.")
            
        # elif commands == 'F':
        #     # Move forward: update position based on current direction
        #     x, y = self.position
        #     if self.direction == 'N':
        #         y += 1
        #     elif self.direction == 'S':
        #         y -= 1
        #     elif self.direction == 'E':
        #         x += 1
        #     elif self.direction == 'W':
        #         x -= 1
        #     self.position = (x, y)