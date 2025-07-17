from dataclasses import replace

class Car(object):
    def __init__(self, name, position, direction):
        # Validate car name - only letters allowed
        if not name or not str(name).isalpha():
            raise ValueError(f"Car name must contain only letters. Invalid name: '{name}'")
        
        self.name = str(name)
        self.position = tuple(position) if isinstance(position, list) else position
        self.direction = str(direction)
        
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
             # Move forward using vector approach
            vector = vectors[compass.index(self.direction)]
            self.position = (self.position[0] + vector[0], self.position[1] + vector[1])
            
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