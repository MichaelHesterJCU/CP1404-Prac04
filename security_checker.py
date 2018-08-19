"""
A very good tool to make sure only your selected usernames can log in. Unbreakable.
"""

def main():
    count = 4
    while count in range(4,0,-1):
        user_entered_name = str(input("Please enter your username:  "))
        if username_checker(user_entered_name,count) == True:
            print("Access granted!")
            count = 0
        else:
            print("Access denied! {} attempts remaining".format(count - 1))
            count = count -1


def username_checker(name_comparison,attempts):
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    if name_comparison in usernames:
        return True

main()