from maze_runner import MazeRunner

class MazeRunnerBot(MazeRunner):

    def __init__(self):
        super().__init__()
        self.last_direction = None

    def receive_update(self, msg):
        super().receive_update(msg)

        if msg == "You move North.":
            self.last_direction = "N"
        elif msg == "You move South.":
            self.last_direction = "S"
        elif msg == "You move East.":
            self.last_direction = "E"
        elif msg == "You move West.":
            self.last_direction = "W"
        elif msg == "BOOM! The wall explodes into rubble and you tentatively step North.":
            self.last_direction = "N"
        elif msg == "BOOM! The wall explodes into rubble and you tentatively step South.":
            self.last_direction = "S"
        elif msg == "BOOM! The wall explodes into rubble and you tentatively step East.":
            self.last_direction = "E"
        elif msg == "BOOM! The wall explodes into rubble and you tentatively step West.":
            self.last_direction = "W"

    def get_move(self, msg):
        if self.room != 0 and self.total_room !=0:
            print(f'Beside you, you see "{self.room} of {self.total_room}" written in faded paint.')
        print(f"You have {self.moves_remaining} moves remaining.")
        print(f"You have {self.explosives_remaining} explosives remaining.")
        print(msg)

        directions = []
        if "North" in msg:
            directions.append("N")
        if "South" in msg:
            directions.append("S")
        if "East" in msg:
            directions.append("E")
        if "West" in msg:
            directions.append("W")

        if len(directions)==0:
            move = "N"
        else:
            #my bot used to choose north-south-north-south for the whole game, so to prevent it from repeatedly running into the same wall, I wrote these lines to stop it from going back to the previous room.
            if self.last_direction == "N":
                if "S" in directions and len(directions) > 1:
                    directions.remove("S")
            elif self.last_direction == "S":
                if "N" in directions and len(directions) > 1:
                    directions.remove("N")
            elif self.last_direction == "E":
                if "W" in directions and len(directions) > 1:
                    directions.remove("W")
            elif self.last_direction == "W":
                if "E" in directions and len(directions) > 1:
                    directions.remove("E")

            move = directions[0]


        self.last_direction = move
        return move

    def get_explosive_usage(self, msg):
        print(msg)

        if self.explosives_remaining == 0:
            return "N"

        return "N"

#I tried to make the bot use unsafe directions to make it use Y, but it didn’t work perfectly and I got negative values for self.room, so since the project says the bot will NOT lose marks if it never uses explosives, I kept it like this
