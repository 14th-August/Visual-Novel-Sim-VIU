# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define oba = Character("おばあさん", color="#c8ffc8")
define mc = Character("私", color="#c8ffc8")
define obaSelf = Character(None, kind=oba, what_italic=True) 
define imouto = Character("妹", color="#3bff3b")

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

    menu:

        "知らない、何の？":
            pass
        "ちょっと聞いていた、なんですか？":
            pass

    show Grandma Temp:
        zoom 0.5 xalign 0.0 yalign 1.0  

    oba 'じゃあ、いい機会だと思う、だって転校してから新しい友達をあんまり作っていなかった、行って方がいい！'

    show MainChar Temp:
        zoom 0.5 xalign 1.0 yalign 1.0  

    menu:

        "まあ。。。あんまり作りたくないな。。。":
            obaSelf 'なぜ、そんな返事が。。'
        "さあ、ちょっと楽しそう":
            obaSelf 'やった、すぐ結婚するからね。'
        "うん。行こう！":
            obaSelf 'やった、すぐ結婚するからね。'

    show Grandma Temp:
        zoom 0.5 xalign 0.0 yalign 1.0  


    oba 'さあ、学校はすぐ始まって、君のおじいちゃんもコンビニで会うつもりです。'
    oba '最近のことを彼に伝えます、興味がいつもあるような。'
    oba 'ところで、弟がもう起きた？おなかがすいたでしょ。 '

    imouto 'おなかすいた！'

    pause 2.0 
    scene bg livingroom with character_fade

    show Brother Temp:
        zoom 0.5 xalign 0.0 yalign 1.0
    
    imouto 'おい！お兄ちゃん！歯ブラシがない、どうして？！'

    return


