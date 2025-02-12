'''
Treasure Island
Paul Ring
100 Days of Python
'''

def print_char_line(char_type, char_count):
    '''
    Prints a line of characters.
    
    :param char_type: The character to print.
    :param char_count: The number of times to print the character.
    '''
    print(char_type * char_count)

def print_char_pattern(char_type,*char_interval):
    '''
    Prints a pattern of characters.
    
    :param char_type: The character to print.
    :param char_interval: The interval at which to print the character.
    '''
    interval = 0
    for arg in [char_interval]:
        for i in range(len(arg)):
            if 0 == arg[i]:
                interval = -1
            else:
                interval = arg[i] -1
            print(" " * interval, char_type, end="")

    print(" ")
#            print(" " * interval, char_type)
#            

def banner():
    print_char_line("*", 80)
    print_char_pattern("|",9,19,19,19,9)
    print('''
        ____________________________________________________________________
        / \-----     ---------  -----------     -------------- ------    ----
        \_/__________________________________________________________________/
        |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
        |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
        | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
        |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
        |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
        |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
        |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
        |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
        | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
        |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
        |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
        | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
        |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
        | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
        |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
        | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
        |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
        | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
        |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
        |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
        / \----- ----- ------------  ------- ----- -------  --------  -------\
        \_/__________________________________________________________________/
        ''')
    
    print_char_pattern("|",9,19,19,19,9)
    print_char_line("*", 80)
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure and not be killed.")
    print("")

def decision_one():
    decision = False
    alive = True
    while decision == False:
        print("You are at a crossroad.  Where do you want to go?")
        instruction = input("   Type \"left\" or \"right\" ")
        if instruction == "right":
            print("Sorry, that leads to a cliff and your death :( ")
            decision = True
            alive = False
            exit
        elif instruction == "left":
            decision = True
        else:
            print("please type \"left\" or ri\"right\"....")
    return(alive)

def decision_two():
    decision = False
    while decision == False:
        print("You've come to a lake.  There is an island in the middle of the lake.")
        instruction = input("   Type \"wait\" to wait for a boat or \"swim\" if you want to swim across the lake.")
        if instruction == "swim":
            print("Sorry, you get too tired and drown :( ")
            decision = True
            exit
        elif instruction == "wait":
            decision = True
        else:
            print("please type \"wait\" or \"swim\"....")
    return

def decision_three():
    decision = False
    while decision == False:
        print("You arrive at the island unharmed.  There is a house with three doors.")
        instruction = input("   One red, one yellow and one blue.  Which color do you choose?")
        if instruction == "red":
            print("Sorry, you've been burned by fire, Game over... :( ")
            decision = True
            exit
        elif instruction == "blue":
            print("Sorry, you've been eathen by beasts!  Game over... :(")
            decision = True
        elif instruction == "yellow":
            print("Congratulations, you've found the treausre!  You win!")
            decision = True
            exit
        else:
            print("please type \"red\", \"yellow\" or \"blue\"....")
    return

def main():
    banner()
    if (decision_one() )== True:
        if (decision_two() )== True:
            decision_three()

if __name__ == "__main__":
    main()