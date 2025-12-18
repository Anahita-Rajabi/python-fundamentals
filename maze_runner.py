class MazeRunner:

    """
    Handles player interactions through console input/output.

    This class serves as the user interface for the maze game, prompting for
    player decisions and displaying game updates.
    """

    def __init__(self):
        self.moves_remaining = 10
        self.explosives_remaining = 3
        self.room = 0
        self.total_room = 0
        self.side = None

    def get_move(self, msg):
        if self.room != 0 and self.total_room !=0:
            print(f'Beside you, you see "{self.room} of {self.total_room}" written in faded paint.')
        print(f"You have {self.moves_remaining} moves remaining.")
        print(f"You have {self.explosives_remaining} explosives remaining.")
        """
        Prompt the player to choose a direction to move.

        Args:
            msg (str): Message describing available directions

        Returns:
            str: The direction chosen by the player (should be 'N', 'E', 'S', or 'W')
        """
        print(msg)
        move = input("Which direction do you want to move? (N/E/S/W) ").strip().upper()
        while move not in ["N", "S", "W", "E"]:
            move = input("Which direction do you want to move? (N/E/S/W) ").strip().upper()

        return move

    def get_explosive_usage(self, msg):
        """
        Prompt the player to decide whether to use an explosive.

        Args:
            msg (str): Message explaining that an explosive is needed

        Returns:
            str: The player's response (should be 'Y' for yes or 'N' for no)
        """
        print(msg)



        if self.explosives_remaining == 0:
            return "N"

        reply = input("Y/N: ").strip().upper()
        while reply not in ["Y", "N"]:
            reply = input("Y/N: ").strip().upper()

        if reply == "Y" and self.explosives_remaining > 0:
            self.explosives_remaining = self.explosives_remaining - 1

        return reply

    def receive_update(self, msg):
        """
        Display a game update message to the player.

        Args:
            msg (str): The message to display
        """
        print(msg)
        #I split the "beside you..." to get "3 of 36". then split it again to get the numbers only. then I save the room number, and the total and the size of the maze.
        if "Beside you, you see" in msg:
            parts = msg.split('"')
            text = parts[-2]
            pieces = text.split(" of ")
            self.room = int(pieces[0])
            self.total_room = int(pieces[1])
            self.side = int(self.total_room ** 0.5)
            return

        move_msgs = ["You move North.", "You move South.", "You move East.", "You move West."]

        boom_msgs = [ "BOOM! The wall explodes into rubble and you tentatively step North.", "BOOM! The wall explodes into rubble and you tentatively step South.", "BOOM! The wall explodes into rubble and you tentatively step East.",  "BOOM! The wall explodes into rubble and you tentatively step West."]

        boundary_msg = "This wall seems different, like it's heavily reinforced. Maybe you've found a boundary of this place."

        no_explosive_msg = "You reach into your backpack and find no explosives left."

        if  msg in move_msgs  or msg in boom_msgs  or msg == "You decide not to use an explosive."  or msg == boundary_msg  or msg == no_explosive_msg:

            self.moves_remaining = self.moves_remaining - 1

        if self.side is None:
            return

        if msg == "You move North.":
            self.room =self.room+self.side
        elif msg == "You move South.":
            self.room =self.room- self.side
        elif msg == "You move East.":
            self.room =self.room- 1
        elif msg == "You move West.":
            self.room =self.room+ 1
        elif msg == "BOOM! The wall explodes into rubble and you tentatively step North.":
            self.room =self.room+ self.side
        elif msg == "BOOM! The wall explodes into rubble and you tentatively step South.":
            self.room =self.room- self.side
        elif msg == "BOOM! The wall explodes into rubble and you tentatively step East.":
            self.room =self.room- 1
        elif msg == "BOOM! The wall explodes into rubble and you tentatively step West.":
            self.room = self.room+ 1

        if "Partially hidden in the shadows, you spot another explosive." in msg:
            self.explosives_remaining = self.explosives_remaining+ 1
            return