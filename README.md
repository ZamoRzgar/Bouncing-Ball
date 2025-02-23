# Ball Bouncing Inside Rotating Hexagon Created With Grok 3

A simple yet visually engaging physics-based game built with Python and Pygame. Watch a ball bounce realistically inside a rotating hexagon, complete with dynamic visual effects like a pulsing hexagon, a fading ball trail, and natural color tones.

## Description

In this game, a forest-green hexagon rotates slowly while an earthy-orange ball bounces inside it, influenced by gravity and realistic collision physics. The hexagon pulses subtly, and the ball leaves a fading trail, creating a dynamic and organic feel. The project demonstrates basic game physics, collision detection, and graphical enhancements using Pygame.

## Features

- **Realistic Physics**: The ball bounces off the hexagon's walls with near-perfect elasticity (0.999 bounce factor) and responds to gravity.
- **Dynamic Hexagon**: The hexagon rotates at 0.5 degrees per frame and pulses in size for visual flair.
- **Natural Aesthetics**: Uses a warm cream background, forest green hexagon with a shadow, and an earthy orange ball with a fading trail.
- **Smooth Animation**: Runs at 60 FPS for a fluid experience.

## Prerequisites

- **Python 3.x**: Ensure Python is installed on your system ([Download Python](https://www.python.org/downloads/))
- **Pygame**: A Python library for game development

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Bouncing-ball.git
   cd ball-bouncing-hexagon
   ```

2. **Install Pygame**:
   ```bash
   pip install pygame
   ```

3. **Run the Game**:
   ```bash
   python dynamic_hexagon.py
   ```

## How to Play

- The game starts automatically when you run the script
- Watch the ball bounce inside the rotating hexagon
- Close the window (click the "X") to exit

## Controls

No user input is required; the simulation runs autonomously.

## Code Structure

The main game file `dynamic_hexagon.py` contains all logic, physics, and rendering.

### Key Components:
- Collision detection with line intersection and reflection
- Hexagon pulsing and rotation
- Ball trail effect using deque

## Screenshot

![Game Screenshot](screenshot.png)
*The ball bouncing inside the pulsing, rotating hexagon with a trail effect*

## Customization

Feel free to tweak the following variables in `dynamic_hexagon.py`:
- `rotation_speed`: Adjust hexagon rotation speed (default: 0.5)
- `gravity`: Change the strength of gravity (default: 0.3)
- `bounce_factor`: Modify elasticity (0 to 1, default: 0.999)
- `pulse_amplitude`: Control hexagon pulsing size (default: 5)
- Colors: Edit `CREAM`, `FOREST_GREEN`, `EARTH_ORANGE`, etc., for different aesthetics

## Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit (`git commit -m "Add feature"`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

## License

This project is unlicensed — feel free to use, modify, and distribute it as you wish.

## Acknowledgments

- Built with Pygame, a fantastic library for Python game development
- Inspired by physics simulations and dynamic visual effects