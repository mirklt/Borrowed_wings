

# Определение персонажей игры.
define gg = Character('Лиам', color="#9836e7",image="gg", callback=combined_callback, cb_name="gg", what_color="#c1b5e4", what_callback=typewriter_count_callback)
define ld = Character('Зефир', color="#eea4e4",image="ld", callback=combined_callback, cb_name="ld", what_color="#f8cfee", what_callback=typewriter_count_callback)
define x = Character('Эван', color="#ec9531",image="x", callback=combined_callback, cb_name="x",what_color="#ffffff", what_callback=typewriter_count_callback)
define d = Character('Майя', color="#ebde6a",image="d", callback=combined_callback, cb_name="d",what_color="#ffffff", what_callback=typewriter_count_callback)
define an = Character('Рафаэль', color="#6c9feb",image="an", callback=combined_callback, cb_name="an",what_color="#c0cdf0", what_callback=typewriter_count_callback)
define de = Character('Азазель', color="#fc5555", callback=combined_callback, cb_name="de", what_color="#ffffff", what_callback=typewriter_count_callback)

define un = Character('дядя', color="#726767", imagine="un", callback=combined_callback, cb_name="un", what_color="#b9b9b9", what_callback=typewriter_count_callback)

define n = Character(
    None,
    callback=combined_callback,
    cb_name=None,
    what_style="say_dialogue",
    what_italic=True,
    what_color="#b8b8b8"
)

define sc=Character(None, kind=nvl)

define audio.main_menu = "music/main_menu.mp3"
define audio.normal = "music/normal.mp3"
define audio.mystic = "music/waking_the_devil.mp3"

define audio.click = "sounds/click.mp3"
define audio.alarm = "sounds/alarm.mp3"
define audio.wings = "sounds/wings.wav"

default current_speaker = None

init python:

    def reset_speaker():
        # Auto-Highlight использует speaking_char, а не current_speaker.
        store.current_speaker = None
        if hasattr(store, "speaking_char"):
            store.speaking_char = None

    def _reset_highlight_on_scene(name, parsed=None):
        if name == "scene":
            reset_speaker()

    if hasattr(config, "statement_callbacks") and _reset_highlight_on_scene not in config.statement_callbacks:
        config.statement_callbacks.append(_reset_highlight_on_scene)

image gg shocked baga = At ("gg shocked bag", sprite_highlight ('gg'))
image gg backa = At ("gg back", sprite_highlight ('gg'))
image bag = At ("obj bag", sprite_highlight ('bag'))
image gg argue baga = At ("gg argue bag", sprite_highlight ('gg'))
image gg smirking fold baga = At ("gg smirking fold bag", sprite_highlight ('gg'))
image gg static baga = At ("gg static bag", sprite_highlight ('gg'))
image gg emberasseda = At ("gg emberassed gripping bag", sprite_highlight ('gg'))
image gg gripping baga = At ("gg static gripping bag", sprite_highlight ('gg'))
image gg opening baga = At ("gg opening bag", sprite_highlight ('gg'))
image gg scared baga = At ("gg scared bag", sprite_highlight ('gg'))
image gg hilla = At ("gg hill", sprite_highlight ('gg'))


# Side images for the dialogue panel.

image side gg shocked baga = "images/gg/side/side gg shocked bag.png"
image side gg static baga= "images/gg/side/side gg static bag.png"
image side gg backa = "images/gg/side/side gg static bag.png"
image side gg argue baga = "images/gg/side/side gg argue bag.png"
image side gg smirking fold baga = "images/gg/side/side gg smirking fold bag.png"
image side gg emberasseda = "images/gg/side/side gg emberassed gripping bag.png"
image side gg gripping baga = "images/gg/side/side gg static bag.png"
image side gg opening baga = "images/gg/side/side gg opening bag.png"
image side gg scared baga = "images/gg/side/side gg scared bag.png"

# angel
image an smilea = At ("an smile fold", sprite_highlight ('an'))
image an angrya = At ("an angry", sprite_highlight ('an'))
image an sidea = At ("an side", sprite_highlight ('an'))
image an sittinga = At ("an sitting", sprite_highlight ('an'))
image an roofa = At ("an roof", sprite_highlight ('an'))
image an smirka = At ("an smile pack", sprite_highlight ('an'))
image an hilla = At ("an hill", sprite_highlight ('an'))


image side an = "images/an/side/side an side.png"
image side an angrya = "images/an/side/side an angry.png"
image side an smilea = "images/an/side/side an smile fold.png"
image side an sidea = "images/an/side/side an side.png"
image side an roofa = "images/an/side/side an roof.png"
image side an smirka = "images/an/side/side an smile pack.png"


# ld
image ld coola = At ("ld cool", sprite_highlight ('ld'))
image ld oa = At ("ld o", sprite_highlight ('ld'))
image ld statica = At ("ld static", sprite_highlight ('ld'))
image ld scareda = At ("ld scared", sprite_highlight ('ld'))
image ld shya = At ("ld shy", sprite_highlight ('ld'))
image ld angrya = At ("ld angry", sprite_highlight ('ld'))
image ld happya = At ("ld happy", sprite_highlight ('ld'))
image ld crya = At ("ld cry", sprite_highlight ('ld'))

image side ld coola = "images/ld/side/side ld cool.png"
image side ld oa = "images/ld/side/side ld o.png"
image side ld statica = "images/ld/side/side ld static.png"
image side ld shya = "images/ld/side/side ld shy.png"
image side ld angrya = "images/ld/side/side ld angry.png"
image side ld happya = "images/ld/side/side ld happy.png"
image side ld crya = "images/ld/side/side ld cry.png"


image un statica = At ("un static", sprite_highlight ('un'))
image un angrya = At ("un angry", sprite_highlight ('un'))
