import os
import utils
import time
import sys
from node import TreeNode


def search(queue, method, initial, goal):
    """Searches the tree for a solution based on a search algorithm."""
    root = TreeNode(initial, None, None, 0, 0, 0)
    if method == 'astar' or method == 'best':
        queue.put((0, root))
    else:
        queue.put(root)

    explored_set = set()  #Set of explored states.
    start = time.time()
    while (not queue.empty()) and (time.time() - start <= 60):
        #While the queue is not empty and the time limit hasn't expired.

        if method == "astar" or method == "best":
            #PriorityQueue .get() method returns the priority number and the element
            curr_f, current = queue.get()
        else:
            current = queue.get()

        if current.is_goal(goal):
            return current

        if str(current.state) in explored_set:
            continue

        current.find_children(method, goal)
        explored_set.add(str(current.state))

        for child in current.children:
            if method == "depth" or method == "breadth":
                queue.put(child)
            elif method == "astar" or method == "best":
                queue.put((child.f, child))

    return None


def main():
    start = time.time()  # Start time.
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal

    #Handles the arguments.
    if len(sys.argv) == 3:
        # If the arguments are 3 output file name wasn't specified
        method = sys.argv[1]
        input_file = sys.argv[2]
    elif len(sys.argv) == 4:
        # If the arguments are 4 THE output file name was specified
        method = sys.argv[1]
        input_file = sys.argv[2]
        output_file = sys.argv[3]
    else:
        print(
            f'How to use: {sys.argv[0]} <search algorithm> <problem file name> <solution file name>'
        )
        print('- search algorithms: depth (Depth First), breadth (Breadth First), best (Best First), astar (A*)')
        sys.exit()

        #Initiliazes the data structure of the que base on the search method.
    search_queue = utils.METHODS[method]

    #Parse the input file and get the blocks, initial state, goal state.
    data = utils.load_problem_file(input_file)
    blocks = utils.get_blocks_from_file(data)
    initial_state = utils.get_initial_state(data)
    goal_state = utils.get_goal_state(data)

    print('BLOCKS:', blocks)

    print('\n################## INITIAL STATE ##################\n')
    print(initial_state)
    i_blocks = utils.initialize_blocks(blocks, initial_state)

    print('\n################## GOAL STATE ##################\n')
    print(goal_state)
    g_blocks = utils.initialize_blocks(blocks, goal_state)

    solution_node = search(search_queue, method, i_blocks, g_blocks)

    if solution_node is not None:
        # If a solution is found.
        print('\n################## SOLUTION ##################\n')
        solution_node.print_state()
        print(f'Number of moves: {solution_node.g}')

        # Calculates the time it took to find the solution.
        print('Took: ', time.time() - start)

        solution_path = solution_node.get_moves_to_solution()

        if len(sys.argv) == 3:
            # If the output file name was not specified.
            try:
                # Handling the paths with forward-slashes and back-slashes.
                file_name = input_file.split('\\')[-1]
                output_file = './solutions/' + method + '-' + file_name
                utils.write_solution(output_file, solution_path)
            except FileNotFoundError:
                file_name = input_file.split('/')[-1]
                output_file = './solutions/' + method + '-' + file_name
                utils.write_solution(output_file, solution_path)
        else:
            # If the output file name is specified.
            utils.write_solution(output_file, solution_path)

    else:
        print('Time taken: ', time.time() - start)
        print('############ ONE MINUTE PASSED AND NO SOLUTION WAS FOUND ############')
        sys.exit()


if __name__ == '__main__':
    main()
