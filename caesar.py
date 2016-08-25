from helpers import rotate_character
from sys import argv, exit
        
def encrypt(text, rot):
    newText = ""
    for ch in text:
        newCh = rotate_character(ch, rot)
        newText = newText + newCh
    return newText    

def user_input_is_valid(cl_args):
    if len(cl_args) == 2:
        if cl_args[1].isdigit() == True:
            return True    
    return False

#if user_input_is_valid(argv) == True:
#    t = input("Type a message:")
#    print(encrypt(t, argv[1]))
#else:
#    print("usage: python3 caesar.py n")
#    exit()