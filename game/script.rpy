# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define oba = Character("おばあさん", color="#c8ffc8")
define mc = Character("私", color="#c8ffc8")
define obaSelf = Character(None, kind=oba, what_italic=True) 
define otouto = Character("弟", color="#3bff3b")
define chad = Character("チャド", color="#ff3bb460")
define prep = Character("プレップ", color="#e76eff")
define delin = Character("デリンキント", color="#ff9d1c")

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

    otouto 'おなかすいた！'

    pause 2.0 
    scene bg livingroom with character_fade

    show Brother Temp:
        zoom 0.5 xalign 0.0 yalign 1.0
    
    otouto 'おい！お兄ちゃん！歯ブラシがない、どうして？！'
    otouto 'どこに置いたの？！'

    show MainChar Temp:
        zoom 0.5 xalign 1.0 yalign 1.0 

    menu:
        "うそ！なんで私のせいにするの？":
            otouto 'だって、君が歯ブラシをいつもう越してるから'
        "あんまり覚えてないな。。。":
            otouto 'もっと考えてなんか思い出して！'
        "部屋にわすれちゃったかも。。。":
            otouto '…'
    
    otouto 'ああ、もう！お兄ちゃんはいつもそうだ！'
    otouto 'もう、いい！私が自分で探すから！'
    otouto 'ね、おばあちゃん、ごはんを作っておいた？'

    show Grandma Temp:
        zoom 0.5 xalign 1.0 yalign 1.0 

    oba '食べるだけではなく，テーブルで座ってくれませんか'
    otouto 'はい！'

    scene bg table with character_fade

    show Grandma Temp:
        zoom 0.5 xalign 1.0 yalign 1.0 

    oba 'さあ、食べましょう！'

    show Brother Temp:
        zoom 0.5 xalign 0.0 yalign 1.0

    otouto 'いただきます！'

    oba 'いただきます！'

    scene bg frontdoor with character_fade

    show Grandma Temp:
        zoom 0.5 xalign 1.0 yalign 1.0

    oba '今回は教科書を忘れてはいけなさい,それが大切だよ！'

    show Brother Temp:
        zoom 0.5 xalign 0.0 yalign 1.0

    otouto 'もう注意されたおばあちゃん！'
    oba 'まあ、いいでしょう。さあ、気を付けてね'
    otouto '行ってきます！'
    oba '行ってらっしゃい！'

    scene bg frontdoor with character_fade

    oba 'ところで、弟が世話してね'

    show MainChar Temp:
        zoom 0.5 xalign 1.0 yalign 1.0 

    menu:

        "うん、わかった！":
            obaSelf 'ニャンニャン'
        "もちろん":
            obaSelf 'ニャンニャン'
        "さあ。。":
            obaSelf 'ニャンニャン'

    scene bg road with character_fade

    show Brother Temp:
        zoom 0.5 xalign 0.0 yalign 1.0

    otouto 'お兄ちゃん、待って！'
    otouto 'あの、さっきはごめんね！'

    scene bg truckkun with character_fade

    show Brother Temp:
        zoom 0.5 xalign 0.0 yalign 1.0

    otouto '危ない！気を付けて！'

    show Love1 Temp:
        zoom 0.5 xalign 1.0 yalign 1.0

    chad 'おい！お兄ちゃん！'
    otouto 'チャド！'

    show Love2 Temp:
        zoom 0.5 xalign 0.5 yalign 1.0

    prep 'おい、プレップもいるぞ！'

    show Love4 Temp:
        zoom 0.5 xalign 1.0 yalign 1.0

    delin 'デリンキントもいるぞ！'
    
    return


