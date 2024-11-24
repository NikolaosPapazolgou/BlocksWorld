# Artificial Intelligence - Blocks World Problem

An AI that solves the Blocks World Problem with informed and uniformed searching algorithms.
## Searching Algorithms:
 1. Deep First (uniformed)
 2. Breadth First (uniformed)
 3. Best First (informed)
 4. A* (informed)

## Heuristic in the informed search algorithms:

The Best First and A* algorithm implement a heuristic function to choose states with the smallest heuristic value.

The heuristic function returns the number of blocks that are not to the correct position based on the given state and the goal state.

## How to run the program?
The program has 3 command line arguments:
1. The Search Algorithm: depth/breadth/best/astar
2. The name of the problem file: Choose a .txt file from the problems folder.
3. Solution file name: Optional. If not specified the solution will be saved in a folder called solutions.

For instance: 

`python main.py depth ./problems/probBLOCKS-6-0.txt`
