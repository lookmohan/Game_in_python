# Space Invaders Clone

Welcome to the **Space Invaders Clone**, a classic arcade-style game recreated using Python and Pygame. Engage in an intergalactic battle by controlling your spaceship, dodging enemy attacks, and shooting down waves of enemies to achieve the highest score!

## Features

- **Classic Gameplay:** Experience the nostalgia of the original Space Invaders with modern enhancements.
- **Multiple Enemies:** Face off against multiple enemies that increase in speed and number as your score rises.
- **Sound Effects:** Enjoy engaging sound effects for background music, shooting, and explosions.
- **Score Tracking:** Keep track of your score and aim for high scores.
- **Game Over Screen:** Receive a game over message when enemies breach your defenses.

## Getting Started

Follow these instructions to set up and run the game on your local machine.

### Prerequisites

- **Python 3.6+**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
- **Pygame Library**: This game uses Pygame for graphics and sound.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/space-invaders-clone.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd space-invaders-clone
   ```

3. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install the Required Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   *If you don't have a `requirements.txt`, you can install Pygame directly:*

   ```bash
   pip install pygame
   ```

5. **Ensure Assets Are in Place**

   Make sure the following assets are present in the project directory:

   - `bg.png`: Background image.
   - `monster.png`: Enemy and icon image.
   - `space-invaders (1).png`: Player spaceship image.
   - `bullet.png`: Bullet image.
   - `background.wav`: Background music.
   - `laser.wav`: Sound effect for shooting.
   - `explosion.wav`: Sound effect for explosions.
   - `Crashed Scoreboard.ttf`: Font file for score and game over text.

## How to Play

1. **Start the Game**

   Run the Python script to start the game:

   ```bash
   python space_invaders.py
   ```

2. **Gameplay**

   - Control your spaceship to move left and right across the bottom of the screen.
   - Press the **Spacebar** (or designated key) to shoot bullets at incoming enemies.
   - Prevent enemies from reaching the bottom of the screen.
   - Each enemy destroyed increases your score.
   - The game ends when an enemy breaches your defenses.

3. **Objective**

   Achieve the highest score possible by destroying as many enemies as you can before the game ends.

## Game Controls

- **Move Left:** Press the **Left Arrow** key or **'A'**.
- **Move Right:** Press the **Right Arrow** key or **'D'**.
- **Shoot Bullet:** Press the **Spacebar** or **'S'**.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. **Fork the Repository**

2. **Create a New Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add your feature"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

   Describe your changes and submit a pull request for review.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- **Pygame:** For providing the library that makes game development accessible in Python.
- **Original Space Invaders:** For inspiring this classic game remake.

