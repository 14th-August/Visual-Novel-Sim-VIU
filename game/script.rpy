# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define oba = Character("おばあさん", color="#c8ffc8")
define mc = Character("Main Character", color="#c8ffc8")

define character_fade = Dissolve(4.0)

# The game starts here.

label start:

    pause 2.0 
    scene bg blackscreen with character_fade

    mc '...'

    mc '...'

    mc '...'

    pause 2.0
    scene bg bedroom with character_fade
    pause 2.0
    show Grandma Temp:
        zoom 0.5 xalign 0.0 yalign 1.0

    oba 'まだ寝ている？、もうすぐご飯を作るよ、早く起きなさい！'

    pause 2.0
    scene bg kitchen with character_fade
    pause 2.0
    show Grandma Temp:
        zoom 0.5 
        xalign 0.0 
        yalign 1.0
    with character_fade

    oba '聞いた?、どうやらVIUで今後二週間新しいお祭りを開催するって、知っていた?'

    show MainChar Temp:
        zoom 0.5 xalign 1.0 yalign 1.0  

    show Grandma Temp:
        zoom 0.5 xalign 0.0 yalign 1.0  

    menu:
        "":

        "":

    return
