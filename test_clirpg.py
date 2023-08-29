import unittest
from io import StringIO
from unittest.mock import patch

from clirpg import Player, Room, Game 

class TestCLIRPGGame(unittest.TestCase):

    def test_player_name(self):
        player = Player("Test")
        self.assertEqual(player.name, "Test")

    def test_player_pick_up_sword(self):
        player = Player("Test")

        with patch("builtins.input", return_value = "yes"):
            player.pick_up_sword()
            self.assertEqual(player.has_sword, True)

    def test_player_create_game_name(self):
        player = Player("Test")
        game_name = player.create_game_name()
        self.assertEqual(len(player.name), len(game_name))

    def test_room_description(self):
        room = Room("left", "A room description.", "sword")
        self.assertEqual(room.name, "left")
        self.assertEqual(room.description, "A room description.")
        self.assertEqual(room.encounter, "sword")

    def test_game_choose_a_door(self):
        rooms = {
            "left": Room("left", "The room appears to be empty.", "sword"),
            "right": Room("right", "There is a large dragon in the room.", "dragon")
        }
        player = Player("Test")
        game = Game(player, rooms)

        with patch("builtins.input", return_value = "left"):
            door_choice = game.choose_a_door()
            self.assertEqual(door_choice, "left")

    def test_game_go_into_room(self): # Tests the left room and already has the sword
        rooms = {
            "left": Room("left", "The room appears to be empty.", "sword"),
            "right": Room("right", "There is a large dragon in the room.", "dragon")
        }
        player = Player("Test")
        player.has_sword = True
        game = Game(player, rooms)
    
        with patch("sys.stdout", new = StringIO()) as fake_out:
            game.go_into_room("left")
            self.assertEqual(fake_out.getvalue().strip(), "The room appears to be empty.\nYou've already got the sword. There is nothing else of value in the room so you leave.")

    def test_game_fight_dragon(self): # Tests yes to fight dragon with the sword
        rooms = {
        'left': Room('left', 'The room appears to be empty.', 'sword'),
        'right': Room('right', 'There is a large dragon in the room.', 'dragon')
        }
        player = Player("Test")
        player.has_sword = True
        game = Game(player, rooms)
        
        with patch("builtins.input", return_value = "yes"):
            with patch("sys.stdout", new = StringIO()) as fake_out:
                game.fight_dragon()
                self.assertEqual(fake_out.getvalue().strip(), "You had the sword, fought the dragon, and won! Congratulations!")

if __name__ == "__main__":
    unittest.main()
