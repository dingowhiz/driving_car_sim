# Driving Car Simulation

A Python-based simulation program that demonstrates autonomous car movement on a 2D grid with collision detection and real-time tracking.

## 🚗 Overview

This simulation allows you to:
- Create multiple cars on a grid field
- Program movement sequences for each car
- Execute simultaneous car movements step-by-step
- Detect and handle collisions between cars
- Track car positions and orientations in real-time

## 📁 Project Structure

```
driving_car_sim/
├── driving_car/
│   ├── main.py              # Main program entry point
│   ├── car.py               # Car class implementation
│   ├── test_sequences.py    # Development testing script
│   └── tests/
│       └── test_drive.py    # Unit tests
└── README.md               # This file
```

## 🛠️ Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## 🚀 Quick Start

### Installation

1. Clone or download the project:
```bash
git clone <repository-url>
cd driving_car_sim
```

2. Navigate to the driving_car directory:
```bash
cd driving_car
```

### Running the Simulation

```bash
python main.py
```

## 📖 Usage Guide

### 1. Field Setup
When you start the program, you'll be prompted to create a simulation field:
```
Please enter the width and height (e.g., '10 10'): 15 15
```

### 2. Adding Cars
Choose option `1` to add a car:
- **Car Name**: Enter letters only (e.g., "Tesla", "BMW", "A")
- **Position**: Enter `x y Direction` format (e.g., "5 3 N")
- **Commands**: Enter movement sequence (e.g., "FFRFFLF")

#### Valid Directions:
- `N` - North (↑)
- `S` - South (↓)
- `E` - East (→)
- `W` - West (←)

#### Valid Commands:
- `F` - Move Forward
- `L` - Turn Left
- `R` - Turn Right

### 3. Running Simulation
Choose option `2` to execute all car movements simultaneously.

## 🎮 Example Session

```
Welcome to Auto Driving Car Simulation!
Please enter the width and height (e.g., '10 10'): 10 10

Enter car name (letters only): A
Please enter initial position of car A in x y Direction format (e.g.'2 3 N'): 1 2 N
Please enter the commands in sequence for car A (e.g., F, LLF, FFRFFLF): FFRFF

Enter car name (letters only): B
Please enter initial position of car B in x y Direction format (e.g.'2 3 N'): 7 8 E
Please enter the commands in sequence for car B (e.g., F, LLF, FFRFFLF): FLF

Current Cars:
- A, (1,2) N, FFRFF
- B, (7,8) E, FLF

Choose option 2 to run simulation...

RUNNING SIMULATION
Step 1: A - F - moved forward. Position: (1, 3), Facing: N
Step 1: B - F - moved forward. Position: (8, 8), Facing: E
Step 2: A - F - moved forward. Position: (1, 4), Facing: N
Step 2: B - L - turned left. Position: (8, 8), Facing: N
...
```

## ⚠️ Collision Detection

The simulation includes comprehensive collision detection:
- **Real-time Detection**: Checks for collisions after each movement step
- **Automatic Stop**: Collided cars stop executing further commands
- **Collision Report**: Shows detailed collision information

Example collision output:
```
*** COLLISION DETECTED at step 5 ***
Cars A and B collided at position (4,4)

After simulation, the result is:
- A, collides with B at (4,4) at step 5
- B, collides with A at (4,4) at step 5
```

## 🧪 Testing

### Running Unit Tests
```bash
cd driving_car/tests
python test_drive.py
```

### Running Development Tests
```bash
cd driving_car
python test_sequences.py
```

### Test Coverage
The test suite covers:
- Car creation and validation
- Movement mechanics (forward, left, right)
- Position tracking
- Collision detection logic
- Error handling

## 🏗️ Architecture

### Core Classes

#### `Car` Class (`car.py`)
- **Purpose**: Represents a single car with position and orientation
- **Key Methods**:
  - `get_car_name()`: Returns car identifier
  - `get_car_position()`: Returns (x, y) coordinates
  - `get_facing()`: Returns current direction (N/S/E/W)
  - `move(command)`: Executes a single movement command

#### Main Functions (`main.py`)
- **`main()`**: Program entry point and main loop
- **`run_simulation()`**: Executes simultaneous car movements
- **`check_collisions()`**: Detects car collisions
- **`get_car_input()`**: Handles car creation with validation
- **`process_command()`**: Processes and validates movement commands

### Data Flow
1. User creates field dimensions
2. Cars are added with initial positions and command sequences
3. Simulation executes commands step-by-step for all cars simultaneously
4. Collision detection runs after each step
5. Results are displayed with final positions and collision reports

## 🎯 Features

### ✅ Implemented
- [x] Multi-car simulation
- [x] Simultaneous movement execution
- [x] Real-time collision detection
- [x] Command sequence validation
- [x] Comprehensive error handling
- [x] Unit test coverage
- [x] User-friendly interface

### 🔄 Movement System
- **Grid-based**: Cars move on discrete integer coordinates
- **Direction tracking**: Cars maintain orientation (N/S/E/W)
- **Command sequences**: Support for complex movement patterns
- **Step-by-step execution**: All cars move simultaneously

### 🛡️ Error Handling
- Input validation for car names, positions, and commands
- Graceful handling of invalid movement sequences
- Collision detection and automatic car stopping
- Exception handling with user-friendly error messages

## 🐛 Known Limitations

- No visualization of the grid or car positions
- Commands are executed immediately without time delays
- No save/load functionality for simulation states

## 🔧 Development

### Adding New Features
1. ...

### Code Style
- Follow PEP 8 Python style guidelines
- Use descriptive variable and function names
- Include docstrings for all public methods
- Add type hints where appropriate

## 📝 License

This project is provided as-is for educational and demonstration purposes.
