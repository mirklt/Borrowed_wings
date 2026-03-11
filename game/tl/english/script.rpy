translate english splashscreen:
    python:
        music_vol = _preferences.volumes.get("music", 0.0)
        sfx_vol = _preferences.volumes.get("sfx", 0.0)
        voice_vol = _preferences.volumes.get("voice", 0.0)

        # Restore volume if all mixers were turned off.
        if music_vol <= 0.0 and sfx_vol <= 0.0 and voice_vol <= 0.0:
            _preferences.volumes["music"] = 0.7
            _preferences.volumes["sfx"] = 0.8
            _preferences.volumes["voice"] = 1.0

    scene black
    pause 0.5
    $ renpy.movie_cutscene("video/di.webm")
    return


translate english start:
    stop music fadeout 1.0
    play music mystic fadein 3.0 volume 0.35
    scene bg night
    $ persistent.cg_1 = True
    show gg backa:
        xalign 0.4
        yalign 0.1
    with eyes_blink

    gg backa "Um... Where am I? What is this place?"

    play sound wings
    scene bg black with eyes_blink
    n "Whoosh, whoosh"
    scene bg 1
    $ persistent.cg_2 = True
    gg scared baga "WHAT THE HELL?!"
    an "You have to make a choice, Liam."
    gg "Who are you?!"
    stop sound fadeout 2.0
    scene bg black with eyes_blink
    n "A jolt"

    scene bg falling
    $ persistent.cg_3 = True
    gg scared baga "AAAAAAAA!!!"

    scene bg black with eyes_blink
    play sound alarm
    n "Alarm clock sound"
    scene bg room with fade
    stop sound
    play audio click
    gg emberasseda "Phew... It was just a dream. But it felt so real..."
    stop music fadeout 2.0
    gg "I shouldn't have eaten noodles before bed."
    gg "Alright. Time to get up."

    scene bg room table

    call screen start_game_icon
    $ persistent.cg_4 = True
    $ persistent.cg_5 = True
    # call the minigame menu; when it returns the story continues below
    call nes_start

    gg "Time for school."
    play music normal fadein 3.0 volume 0.35
    jump street


translate english play_hiddenfolks:
    # setup (copy from HiddenFolks_test)
    $ hf_init("bg room table", 5,
        ("beer", 1013, 705, _("Мишка")),
        ("elf", 111, 560, _("Эльф")),
        ("flowers", 700, 615, _("Букет")),
        ("skull", 1813, 161, _("Череп")),
        ("sprite", 355, 240, _("Дотти-чан")),
        mouse=True,
        inventory=False,
        hint=True,
        hover=brightness(.05),
        w=200,
        h=200
    )

    # show background and game field
    $ hf_bg()
    with dissolve

    centered "{size=+24}Collect all items in 5 seconds.\nStart!"

    # start the minigame
    $ hf_start()

    # pause before showing results
    $ renpy.pause(1, hard=True)

    if hf_return == 0:
        centered "{size=+24}Hooray! All items collected!"
    else:
        centered "{size=+24}GAME OVER\nItems not collected: [hf_return]."

    $ hf_hide()
    with dissolve
    return


translate english nes_start:
    # don't show the menu again
    if have_played_nes:
        return

    $ run_hiddenfolks_after_nes = False

    menu:
        with dissolve

        "{size=22}!!!The game cannot be restarted. You can't load another game if one is already running."
        "{size=22}!!!You can't change the game. Q - exit."

        "{size=22}Z - jump/shoot"

        "Mario":
            call screen NES("Super Mario Bros 1 rus")
            $ run_hiddenfolks_after_nes = True

        "Tanks":
            call screen NES("Battle City")
            $ run_hiddenfolks_after_nes = True

        "Mario TV":
            call screen NES("Super Mario Bros 1 rus", False)
            $ run_hiddenfolks_after_nes = True

        "Exit":
            $ run_hiddenfolks_after_nes = True

    if run_hiddenfolks_after_nes:
        call play_hiddenfolks

    # remember the menu was used
    $ have_played_nes = True

    return


translate english street:
    scene bg street with moveinright

    show gg static baga:
        xalign 0.1
        yalign 0.1
    with fade
    with Pause(0.5)
    gg "I should probably prepare for the exam."
    gg opening baga "Let's see."

    scene bg fe
    play sound wings
    gg shocked baga "...what? Feathers?"
    scene bg black with eyes_blink
    scene bg first meet
    $ persistent.cg_meet = True
    with eyes_blink
    pause 1.0
    scene bg black with eyes_blink
    scene bg roof
    $ persistent.cg_6 = True
    pause 1.0
    show an roofa:
        xpos 0.65
        ypos 0.3
    with fade
    stop sound fadeout 1.0
    pause 0.5
    gg scared baga "What the hell..."
    an "Not a devil, an Angel."
    n "The angel rose smoothly."
    show an roof:
        xalign 0.9
        yalign 0.001
    an angrya "You look disappointing."

    show gg emberasseda:
        xpos 0.1
        ypos 1
    gg """Um...

    I guess I'm happy to meet you too?"""

    n "..."

    gg """So... um...

    Is this some kind of cosplay meetup?"""

    an """No. I am an angel. I don't like repeating myself."""
    gg """Yeah, sure. Listen, dude, I take it this is some kind of prank or something?"""
    n "He sighs. Opens his clothes. Wings appear."
    scene bg angel with dissolve
    $ persistent.cg_angel = True
    pause 1.0
    gg shocked baga "..."
    pause 1.0
    gg """You... you weren't making it up..."""
    pause 1.0

    scene bg roof with fade

    show an angrya:
        xalign 0.9
        yalign 0.001

    show gg emberasseda:
        xpos 0.1
        ypos 1

    an """I'll say it one last time. I'm an angel. My name is Raphael.
    """
    gg "Yeah... and I'm... I'm Liam."
    an smirka "I know."
    gg "What?"
    an "You're the only one who can see me."
    an smilea "It's not a coincidence. You're chosen, congratulations."
    gg "Wow. Cool. And the prize is at least a free cafeteria lunch?"
    an angrya "..."
    play sound meme_spiderman volume 0.5
    an angrya "You will decide people's fates."
    gg argue baga """W-what?!
    And I can't refuse right away?"""
    stop sound fadeout 1.0
    an "No."
    jump school


translate english school:
    window hide
    nvl clear
    scene school tree
    with fade
    pause 0.5
    with dissolve
    sc "He goes to classes with him."
    scene bg classroom with dissolve
    pause 1.0
    $ persistent.cg_7 = True
    sc "During lessons, Raphael sits by the window, on the floor—basically on any flat surface—and watches."
    scene school pink with Pause(0.5)

    sc "In the locker room, he shamelessly checks out the guys."
    scene bg f fire with dissolve
    $ persistent.cg_8 = True
    pause 1.0
    nvl clear
    sc "Outside, Liam had to 'gently' explain the concept of personal space to him."
    nvl hide
    pause 1.0

    scene bg hill with fade
    show an hilla:
        xpos 1470
        ypos 350
    $ persistent.cg_hill = True

    show gg hilla:
        xpos 1595
        ypos 690

    pause 1.5
    gg "Listen, how does all this work? What are these fates?"
    an """Everyone has their own fate. Their own path.

    But little by little, darkness consumes a person, and that fate simply breaks.

    Angels always try to support that soul, but there are moments when it's impossible.

    That's why I'm here. I can't interfere in their lives, but you can.

    You must help, Liam."""

    jump zephir


translate english zephir:
    pause 0.5
    scene school tree with fade
    pause 0.5

    show an smilea:
        xpos 1200
        ypos 1
    with dissolve

    show gg gripping baga:
        xpos -100
        ypos 1
    with dissolve

    n """A new day

    Liam was walking through school, talking with Raphael, when suddenly a voice called out."""

    ld "Liam?"

    n "They turn around and see Zephyr—Liam's best friend. A boy with a soft, pleasant look and a smile."

    show ld happya:
        xpos 500
        ypos 1
    with moveinleft
    pause 0.5
    gg smirking fold baga "Zeephiiir. Hey, bro."
    ld "Heeey~"
    n "Raphael looks at him with suspicion."
    window hide
    nvl clear
    sc """
    Liam decided to spend the day with Zephyr, and it actually goes really well.
    They talk, laugh, and hang out after school."""
    nvl clear
    scene bg room night
    sc "Tired, Liam returns home and falls asleep almost immediately."
    sc "But at night he has a dream."
    scene bg black with eyes_blink
    pause 1.0
    n "Darkness. Stuffy."
    pause 0.5
    scene bg zephir cry 1 with eyes_blink
    $ persistent.cg_9 = True
    gg shocked baga "Zephyr?"
    scene bg zephir cry 2 with dissolve
    pause
    ld scareda "Help me. I... I'm scared.."
    scene bg zephir cry 3 with dissolve
    $ persistent.cg_10 = True
    pause 1.0
    scene bg room night with fade
    $ persistent.cg_roomnight = True
    n "Liam jolts awake, breathing heavily."
    show gg static baga:
        xpos 100
        ypos 1
    with dissolve

    n "Raphael is sitting nearby."
    show an sittinga:
        xpos 1000
        ypos 1
    with dissolve

    an "I see your morning started with quite a jolt."
    gg "Yeah. Sure."
    an "Saw Zephyr?"
    gg shocked baga "How do you...?"
    an "Here we go..."
    gg argue baga """Stop talking in riddles like some mysterious puppet master.

    What does Zephyr have to do with this? I don't understand anything."""
    an "He's the first victim."
    gg shocked baga """...

    Zephyr? How? No... but..."""
    an "You'll learn everything in time."
    scene school tree with dissolve
    window hide
    nvl clear
    sc """At school.

    That day Liam starts watching Zephyr more closely.

    Every smile.

    Every flinch.

    Every whisper.

    Every tremble in his voice.
    """
    nvl clear
    sc """He notices a strange pattern.

    Zephyr grows quieter whenever his uncle is nearby.
    From the outside it doesn't look unusual for family relations...
    but it still feels like—

    something is wrong.
    """
    n "After class."
    show gg static baga:
        xpos 900
        ypos 1
    with dissolve

    show ld statica:
        xpos 200
        ypos 1
    with dissolve
    gg emberasseda "Zephyr"
    ld "Yeah?"
    gg "I... I'm not great with words, but..."
    gg "You know I'm your friend. And you can always tell me anything."
    ld oa "Why all of a sudden?"
    gg "Just because. I want you to know you can trust me."
    n "Zephyr hesitates."
    ld shya "Li... Liam... I..."
    n """But then a hand lands on his shoulder.

    It's his uncle."""
    show un statica:
        xpos -200
        ypos 1
    with fade
    n "Zephyr tenses up immediately and lowers his head."
    show ld cry
    un "So, boys? What are you chatting about?"
    ld statica "Nothing, uncle."
    n "His uncle fixes an unreadable look on him for a second, then smiles again."
    un "Then let's go home."
    un "Thanks for looking out for my boy, Liam."
    un "Say hello to your family."
    jump home_1


translate english home_1:
    scene bg room1
    n "At home."
    show gg argue baga:
        xpos 200
        ypos 1
    with dissolve

    show an sidea:
        xpos 1000
        ypos 1
    with dissolve
    gg "What was that??"
    an "You're finally starting to notice."
    gg "Notice what exactly? Let's skip the riddles again."
    an "Well, if you don't want my 'riddles', you'll understand in time."
    gg "Are you, like, offended?"
    pause 1.0
    gg emberasseda "...."
    gg emberasseda "Well, sorry."
    n "Raphael chuckles softly."
    an smirka "Heh, you're so naive."
    n "Raphael didn't say anything else that day."

    scene bg room night with fade
    n "Night."
    window hide
    nvl clear
    sc """Liam can't fall asleep for a long time.
    Eventually, in the middle of the night, he takes a sleeping pill and goes to bed.
    Raphael watches him the whole time.
    He slightly waves his hand.
    Quiet sparks of light appear in the air.
    After that, he simply waits."""

    scene bg black with fade
    n """Liam's dream

    Stuffy again.

    But this time, light slowly appears in the darkness...
    """

