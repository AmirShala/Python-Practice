'''The following code will solve "The Maze" problem in Reeborg's World 
URL = (https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)'''

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if right_is_clear():
        if front_is_clear():
            move()
        else:
            turn_right()
            move()
    elif front_is_clear():
        move()
    else:
        turn_left()
