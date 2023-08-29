
# Basic CLI RPG Game

A simple command-line role-playing game (RPG) where a player navigates through rooms, finds a sword, and potentially battles a dragon.

## Features

- **Character Name Generation**: Create a custom character name using the length of the user's name.
- **Dynamic Navigation**: Navigate through two rooms.
- **Game Decisions**: Pick up a sword and potentially fight a dragon. Your decisions impact the game's outcomes.

## Installation & Running the Game

### Prerequisites

Ensure you have Python and the `requests` library installed.

```bash
pip install requests
```

#### Running the game
After ensuring you have the prerequisites installed, you can simply run the script:

```bash
python rpg_game.py
```

## How to Play
1. Start the game and enter your name.
2. Your character's name in the game will be generated based on the length of the name you entered.
3. You will be presented with two doors: left and right. Choose one.
4. Depending on the room you enter, you may find a sword or face a dragon.
5. The decisions you make will determine the outcome of the game. Good luck!

## Game Design
Player class: Represents the player with attributes like the player's name and whether they have a sword. It also contains methods for the player to pick up a sword and create a game name.

Room class: Represents a room in the game with attributes like name, description, and what the player might encounter in that room.

Game class: This class drives the game. It contains methods for navigating the game, choosing rooms, going into rooms, and handling the dragon encounter.

## Future Improvements
This is a basic CLI RPG game. In the future, there might be additions of more rooms, encounters, and a more intricate storyline.

## Acknowledgements
The create_game_name method uses the Uzby API to generate names based on the length of the player's name.