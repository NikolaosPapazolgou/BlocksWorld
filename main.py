#NOTE: POSSIBLE POSITIONS OF EACH BLOCK
# We have a table and a number of blocks.A block can be ontop of the table (ontable A)
# OR it can be ontop of another block (on A B).
#NOTE: Blocks form a STACK of N blocks, where N is the number of blocks given in the problem.
# When a BLOCK has no block ontop of it we declare its clear property true otherwise false.
# NOTE: POSSIBLE MOVING OF BLOCKS.
#  RESTRICTIONS (1) we can move one block at a time, (2) The moving block should have a clear property value of true.
#  (3) The destination of the moving block should either be (A) the table OR (B) a block with a clear property of true.
#NOTE: Moves function-method description
# The moving procedure is a method that takes 3 arguments (1) The moving block, (2) The original position
# (3) The new position of the moving block
#NOTE: INSTANCE OF THE INPUT.TXT FILE:
# (define (problem BLOCKS-4-0)
# (:domain BLOCKS)
# (:objects D B A C )
# (:INIT (CLEAR C) (CLEAR A) (CLEAR B) (CLEAR D) (ONTABLE C) (ONTABLE A) (ONTABLE
# B) (ONTABLE D) (HANDEMPTY))
# (:goal (AND (ON D C) (ON C B) (ON B A))) )
#NOTE: OUTPUT FORM: Restrain the time of execution to 60 secs, display the time of execution and the moves made.


#TODO:Write a program that finds the best route to reach the given solution state.
# Read the input file and Write the solution to the output file
#TODO GENERAL
#TODO Read the INPUT.TXT File
alphabet = [chr(i) for i in range(65, 91)]
print(alphabet)

with open('input.txt', "r") as inputFile:
    line_2 = inputFile.read()
    lines = inputFile.readlines()


print(line_2.strip()[1:-1].split(') ('), "DSASDDSAASD")
useful_lines = lines[2:5]
print(useful_lines)

chunk_size = 10
block_properties_list = []

for line in useful_lines:
    if "objects" in line:
        for character in line:
            if character in alphabet:
                print(character)

    if "INIT" in line:
        for line_chunk in range(7, len(line), chunk_size):
            if "ONTABLE" in line[line_chunk: line_chunk + chunk_size]:
                chunk_size = 12
            print(line[line_chunk: line_chunk + chunk_size])


#TODO Process The INPUT.TXT File content
#TODO Store The Initial state
#TODO Store The Goal State - Solution


#TODO Create Classes Describing the objects
#TODO Create a class of BLOCKS
#TODO Add the corresponding properties and methods
#TODO Create a class of Table
#TODO Add the corresponding properties and methods


#TODO Create global used functions
#TODO Create Constants implying rigid values
