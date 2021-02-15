import utils
import re

users = {}


class Obstacle:
    obstacles = {'wall': 'O', 'door': '.', 'd_wall': '0'}

    def __init__(self):
        self.obstacle = None

    def set_obstacle(self):

        pass

    def subtituate(self, to_subtituate):
        """Subtituate the given element.

        Arguments:
            to_subtituate {str} -- Element to replace

        Returns:
            [str] -- Element to replace with
        """

        if to_subtituate in self.obstacles:
            if to_subtituate == self.obstacles['door']:
                self.obstacle = self.obstacles['wall']
            else:
                print(">>> Can't subtituate")
        else:
            print(">>> Can't subtituate")

    def break_(self, to_break):
        """Create a road

        Arguments:
            to_break {str} -- Element to break

        Returns:
            [str] -- Element to replace with
        """

        if to_break in self.obstacles:
            if to_break == self.obstacles['d_wall']:
                self.obstacle = self.obstacles['door']
            else:
                print(">>> Can't break")
        else:
            print(">>> Can't subtituate")


class Position:
    def __init__(self, x=0, y=0):
        """Initialize the positions.
        """
        self.x = x
        self.y = y


class User:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def set_score(self, new_score):
        self.score = new_score


def winner(user_1, user_2):
    if user_1.score > user_2:
        return user_1
    else:
        return user_2


class Card:
    def __init__(self):
        self.data = utils.playground_choice()
        self.lines = self.data[1]

    def __repr__(self):
        card = ''
        for line in self.lines:
            card += line
        return card

    def update(self, lines):
        self.lines = lines


class Robot:
    """Manage the Robot
    """

    def __init__(self, symbole: str, owner: User, card: Card):
        self.symbole = symbole  # Symbole representing the robot
        self.owner = owner  # The owner of the current robot
        self.pos = Position()  # position x and y on the map
        self.obstacles = Obstacle()

    def move_up(self, to=1):
        self.pos.x -= to

    def move_down(self, to=1):
        self.pos.y += to

    def move_forward(self, to=1):
        self.pos.x -= to

    def move_backward(self, to=1):
        self.pos.x += to

    def brik_up(self, to_brik):
        self.obstacles.subtituate(to_brik)

    def break_(self, to_break):
        self.obstacles.break_(to_break)

    def is_end(self):
        """To verify if the robot is at the exit zone of the road"""
        # the end is reprented by this pattern
        pattern = rf"(?P<end>{self.symbole}U)"
        # get the actual y position of the robot
        actual_y_pos = self.pos.y
        # get this line in the end_line variable
        end_line = self.lines[actual_y_pos]
        # verify if we have a match
        match = re.search(pattern, end_line)
        # if True, we print the win message
        if match:
            print('\nYou Win!!!\n'.title())
            return True
        else:
            return False
    cmds = {
        'h': move_forward,
        'j': move_down,
        'k': move_up,
        'l': move_backward,
        'm': brik_up,
        'p': break_
    }


if __name__ == '__main__':
    card = Card()
    print(card)
    utils.help_player()
    utils.playground_menu()
