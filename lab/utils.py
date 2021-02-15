from threading import Thread
import random
import os
import re
import sys


def help_player():
    print('Use the keys: H, J, K and L to move the robot')
    print('a) H to move left')
    print('b) J to move down')
    print('c) K to move up')
    print('d) L to move right')
    print('e) "keyN" will move it N time(s) to the "key" direction \n eg: h3 will move it 3 times to the left\n')


def question(quest: str, resp: tuple):
    while True:
        answer = input(quest)[0]
        if answer in resp:
            return answer


def files_in(dir_: str):
    """List all files with the extension .txt/.stat in the given directory.

    Arguments:
        dir_ {str} -- The directory to list over.

    Returns:
        [tuple] -- 0: Dict containing keys and values,
                      which are position of the file
                      in the directory.
                   1: The complete path to all these file.
    """

    pattern_path = r'/*(?P<name>\w*)(?P<extension>\.txt|\.stat)$'
    list_dir = []
    path_to = []
    for k, v in enumerate(os.listdir(dir_)):
        if v.endswith(re.search(pattern_path, v).group('extension')):
            path = os.path.join(dir_, v)
            list_dir.append((k, re.search(pattern_path, path).group('name')))
            path_to.append((k, path))
    sorted(list_dir)
    files = {}
    path_to_ = {}
    i = 0
    while i < len(path_to):
        files[list_dir[i][0]] = list_dir[i][1]
        path_to_[path_to[i][0]] = path_to[i][1]
        i += 1

    return files, path_to_


# Card information
path_to_cards = '/cards'
full_path = sys.path[0] + path_to_cards


def playground_menu():

    menu = "PLAYGROUNDS LIST"
    sep = "-" * (len(menu) + 4)
    print(sep)
    print(f"| {menu} |")
    print(sep)
    playground_list, path_to_playground = files_in(full_path)
    for number, value in playground_list.items():
        text = f"| {number} | {value}".title()
        text += " " * (len(menu) - len(value) - 3)
        text += "|"
        print(text)
    print(sep)


def playground_choice():
    """Select a playground to play on.

    Returns:
        [tuple] -- 0: Represent the playground's name.
                   1: Represent a set of lines representing the road
    """

    extension = '.txt'
    playground_list, path_to_playground = files_in(full_path)
    selected_name = \
        playground_list[random.randint(0, len(playground_list) - 1)]
    playground = []
    file_ = full_path + '/{}{}'.format(selected_name, extension)
    with open(file_) as playground_:
        playground = playground_.readlines()
        selected_name += '\n'
    return selected_name, playground


class InitPosition(Thread):
    """Initialize robot's position."""

    def __init__(self, lines, to_replace, symbole_in, obs):
        """Initialize elements to working with.

        Arguments:
            lines {list} -- List containing the lines in Card object.
            to_replace {str} -- Symbole representing the robot.
            obs {list} -- Symbole representing a list's obstacle
                          in an Obstacle object.
        """

        self.lines = lines
        self.to_replace = to_replace
        self.symbole_in = symbole_in
        self.obs = obs

    def run(self):
        index_in_liste = random.randrange(1, 3)
        # get the line to working on
        line = self.lines[index_in_liste]
        line = [x for x in line]
        while self.to_replace not in line:
            i = random.randrange(2, len(line))
            old_value = line[i]
            # replace a space with the robot symbole
            line[i] = self.to_replace if \
                line[i] not in self.obs and \
                line[i] != self.symbole_in else old_value
        line = ''.join(line)
        self.lines[index_in_liste] = line


def msg_decor(text, sep):
    len_ = len(text) + 2
    sep = sep * len_ + '\n'
    chosed = sep
    chosed += "|" + text + "|\n"
    chosed += sep
    chosed = chosed.encode()
    return chosed


if __name__ == '__main__':
    selected_name, playground = playground_choice()
    msg = ''
    for line in playground:
        msg += line

    le = len(msg)
    print(le)
    msg = msg.encode()
    le = len(msg)
    print(le)
    print(msg)
