import re
from queue import Queue, LifoQueue, PriorityQueue

METHODS = {
    "breadth": Queue(),  #First in First out for BFS.
    "depth": LifoQueue(),  #Last in first out for DFS.
    "best": PriorityQueue(),  #PriorityQueue for Best First.
    "astar": PriorityQueue(),  #PriorityQueue for A*.
}



def load_problem_file(input):
    """Loads the problem from the input file and reforms it replacing spaces with a hyphen"""

    data = []
    with open(input, "r") as file:
        raw_data = file.readlines()

        for line in raw_data:
            data.append(line.strip('\n').replace(' ', '-'))
    return data



def get_initial_state(data):
    """Extracts the initial state from the data."""

    flag = False
    initial_state = []

    for line in data:
        if re.findall(r'\A\(:INIT', line, re.I) or flag:
            flag = True
            if re.match(r'\A\(:goal', line, re.I):
                break

            pattern = r'CLEAR-\w{1}\d?|ONTABLE-\w{1}\d?|ON-\w{1}\d?-\w{1}\d?'
            initial_state.extend(re.findall(pattern, line))

    return initial_state


def get_goal_state(data):
    """Extracts the goal state from the data."""

    flag = False
    goal_state = []
    for line in data:
        if re.match(r'\A\(:goal', line, re.I) or flag:
            flag = True
            pattern = r'CLEAR-\w{1}\d?|ONTABLE-\w{1}\d?|ON-\w{1}\d?-\w{1}\d?'
            goal_state.extend(re.findall(pattern, line))

    return goal_state

def get_blocks_from_file(data):
    """Extracts the number of block objects and their string values."""
    flag = False
    blocks = []
    for line in data:
        if re.match(r'\A\(:object', line, re.I) or flag:
            flag = True
            if re.match(r'\A\(:INIT', line, re.I):
                break
            blocks.extend(re.findall(r'\w{1}\d?', line))

    return blocks[7:]

def initialize_blocks(objects, state):
    """Initializes a dictionary that its id key represents a block with 4 properties."""

    global id
    blocks = {id: {'CLEAR': True, 'ON': -1, 'UNDER': -1, 'ONTABLE': True} for id in objects}

    for state in state:
        if len(state.split('-')) < 3:
            position, block = state.split('-')
        else:
            position, block, on = state.split('-')

        if position == "CLEAR":
            blocks[block][position] = True
        elif position == "ONTABLE":
            blocks[block][position] = True
        else:
            blocks[on]["UNDER"] = block
            blocks[block]["ONTABLE"] = False
            blocks[block][position] = on
            if blocks[on]["CLEAR"]:
                blocks[on]["CLEAR"] = False

    return blocks


def write_solution(file, solution_path):
    """Writes the solution to a file."""

    solution_path.reverse()
    with open(file, 'w') as file:
        for i, move in enumerate(solution_path):
            file.write(f'{i+1}. move {move}\n')


if __name__ == "__main__":
    pass
