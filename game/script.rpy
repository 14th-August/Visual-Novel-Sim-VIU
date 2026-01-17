# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("VIU MC Kun")
define p = Character("Penny")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    show Penny happy

    p "I can't wait to get hit by a bus today"

    show Penny blush

    p "Once you add a story, pictures, and music, you can release it to the world!"

    show Penny base

    e "meow meow"

    e "second text same image"
    


    return
