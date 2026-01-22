# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define oba = Character("おばあさん", color="#c8ffc8")
define mc = Character("Main Character", color="#c8ffc8")

# The game starts here.

label start:

    pause 2.0 
    scene bg blackscreen with dissolve(4.0)

    mc '...'

    mc '...'

    mc '...'

    scene bg bedroom with Dissolve(4.0)
    pause 0.5
    show Grandma Temp:
        zoom 0.5 xalign 0.0 yalign 1.0

    oba 'まだ寝ている？、もうすぐご飯を作るよ、早く起きなさい！'

    pause 2.0
    scene bg kitchen with Dissolve(6.0)
    pause 0.5
    show Grandma Temp:
        zoom 0.5 xalign 0.0 yalign 1.0

    oba '聞いた?、どうやらVIUで今後二週間新しいお祭りを開催するって、知っていた?'

    show MainChar Temp:
        zoom 0.5 xalign 1.0 yalign 1.0  

    show Grandma Temp:
        zoom 0.5 xalign 0.0 yalign 1.0   

    return
