import re

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
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open('input.txt', "r") as inputFile:
    lines = inputFile.readlines()

#The lines of the file from 2 to 5
useful_lines = lines[2:5]
print(useful_lines)

# Processing the file input,while creating a dictionary that includes
# 3 keys : 1) blocks 2) clear 3) ontable 4) on 5) goal
#The 1. Indicates how many blocks are being used and what's their name
#The 2. Indicates how many of them will have a property of clear true
#The 3. Indicates how many of the blocks will have a property of ontable true
#The 4. Indicates which blocks are on top of each other for instance: on A B means that A is on top of B
#The 5. Indicates which is the end state goal, it contains on pairs
dictionary_formatted_input = {}

for line in useful_lines:
    if "objects" in line:
        current_list = [char for char in line if char in alphabet]
        dictionary_formatted_input["blocks"] = current_list
    if "INIT" in line:
        clear_letters = re.findall(r'\(CLEAR (\w)\)', line)
        ontable_letters = re.findall(r'\(ONTABLE (\w)\)', line)
        on_letters = re.findall(r'\(ON (\w) (\w)\)', line)
        dictionary_formatted_input["clear"] = clear_letters
        dictionary_formatted_input["ontable"] = ontable_letters
        dictionary_formatted_input["on"] = on_letters
    if "goal" in line:
        on_letters = re.findall(r'\(ON (\w) (\w)\)', line)
        dictionary_formatted_input["goal"] = on_letters

for block in dictionary_formatted_input["blocks"]:
    print("BLOCKS :", block)
for clear_block in dictionary_formatted_input["clear"]:
    print("CLEAR BLOCKS:", clear_block)
for ontable_block in dictionary_formatted_input["ontable"]:
    print("ONTABLE BLOCKS:", ontable_block)
for on_block in dictionary_formatted_input["on"]:
    print("ON BLOCKS:", on_block, type(on_block))
for goal_block in dictionary_formatted_input["goal"]:
    print("GOAL BLOCKS:", goal_block, type(goal_block))

#TODO: INITIAL STATE CONTAINS THE ENVIROMENT IN THIS OCCASION IS THE TABLE WHICH IS A SET OF STACKS
#I will create a list of lists to represent the set of stacks (TABLE)
table = []


def create_initial_state(table, dictionary_formatted_input):
    for ontable_block in dictionary_formatted_input["ontable"]:
        list = [ontable_block]
        table.append(list)
    for on_block in reversed(dictionary_formatted_input["on"]):
        first_letter = on_block[0]
        second_letter = on_block[1]
        print(f"FIRST LETTER: {first_letter}", f"SECOND LETTER: {second_letter}")
        for stack in table:
            print(f"STACK : {stack}")
            if second_letter in stack:
                print("INSIDE THE IF THE STACK")
                stack.append(first_letter)


create_initial_state(table, dictionary_formatted_input)

print(f"TABLE {table}")

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
