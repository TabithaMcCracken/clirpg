import requests

class Player:
    def __init__(self, name):
        self.name = name
        self.has_sword = False

    def pick_up_sword(self):
        if self.has_sword == False:
            response = input("You look around and find a large sword. Would you like to take it?").lower()
            if "yes" in response:
                self.has_sword = True
                print("You take it and head back out of the room.")

    def create_game_name(self):
        name_len = len(self.name)
        URL = f"https://uzby.com/api.php?min={name_len}&max={name_len}"
        response = requests.get(URL)
        game_name = response.text
        return game_name

class Room:
    def __init__(self, name, description, encounter):
        self.name = name
        self.description = description
        self.encounter = encounter

class Game:
    def __init__(self, player, rooms):
        self.player = player
        self.rooms = rooms
        self.game_over = False

    def game_engine(self):
        print(
        f"Welcome, {self.player.name}! \n"
        f"You're character name in this game is: {player.create_game_name()}! \n"
        f"Enjoy the game, we hope you make it out alive!\n"
        )
        while not self.game_over:
            room_choice = self.choose_a_door()
            self.go_into_room(room_choice)

    def choose_a_door(self):
        door_choice = input(
            "You are in a dark hallway, there are 2 doors in front of you. "
            "Would you like to go through the left door or the right door?\n"
        ).lower()
        return door_choice

    def go_into_room(self, room_choice):
        if room_choice in self.rooms:
            room = self.rooms[room_choice]
            print(room.description)
            if room.encounter == 'sword' and not self.player.has_sword:
                self.player.pick_up_sword()
            elif room.encounter == 'sword' and self.player.has_sword:
                print("You've already got the sword. There is nothing else of value in the room so you leave.")
            elif room.encounter == 'dragon':
                self.fight_dragon()
        else:
            print("Please answer with 'left' or 'right'")

    def fight_dragon(self):
        fight_dragon = input(
            "You have entered the room with the dragon. "
             "Would you like to fight the dragon?\n"
            ).lower()
        if fight_dragon == 'yes':
            self.game_over = True
            if self.player.has_sword:
                print("You had the sword, fought the dragon, and won! Congratulations!")
            else:
                print("I'm sorry! You didn't have any weapons and were eaten by the dragon! You lose!")
        else:
            print("You have left the room.")

if __name__ == "__main__":
    rooms = {
        'left': Room('left', 'The room appears to be empty.', 'sword'),
        'right': Room('right', 'There is a large dragon in the room.', 'dragon')
    }

    user_name = input("Please enter your name:\n")
    player = Player(user_name)
    game = Game(player, rooms)
    game.game_engine()
