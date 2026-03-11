# курсоры
image mouse default1 = Image("/MOUSE/default/frame_00_delay-0.08s.png")
image mouse default2 = Image("/MOUSE/default/frame_01_delay-0.08s.png")
image mouse default3 = Image("/MOUSE/default/frame_02_delay-0.08s.png")
image mouse default4 = Image("/MOUSE/default/frame_03_delay-0.08s.png")
image mouse default5 = Image("/MOUSE/default/frame_04_delay-0.08s.png")
image mouse default6 = Image("/MOUSE/default/frame_05_delay-0.08s.png")
image mouse default7 = Image("/MOUSE/default/frame_06_delay-0.08s.png")
image mouse default8 = Image("/MOUSE/default/frame_07_delay-0.08s.png")
image mouse default9 = Image("/MOUSE/default/frame_08_delay-0.08s.png")
image mouse default10 = Image("/MOUSE/default/frame_09_delay-0.08s.png")
image mouse default11 = Image("/MOUSE/default/frame_10_delay-0.08s.png")

image mouse_hand1 = Image("MOUSE/link/frame_00_delay-0.08s.png")
image mouse_hand2 = Image("MOUSE/link/frame_01_delay-0.08s.png")
image mouse_hand3 = Image("MOUSE/link/frame_02_delay-0.08s.png")
image mouse_hand4 = Image("MOUSE/link/frame_03_delay-0.08s.png")
image mouse_hand5 = Image("MOUSE/link/frame_04_delay-0.08s.png")
image mouse_hand6 = Image("MOUSE/link/frame_05_delay-0.08s.png")
image mouse_hand7 = Image("MOUSE/link/frame_06_delay-0.08s.png")
image mouse_hand8 = Image("MOUSE/link/frame_07_delay-0.08s.png")
image mouse_hand9 = Image("MOUSE/link/frame_08_delay-0.08s.png")
image mouse_hand10 = Image("MOUSE/link/frame_09_delay-0.08s.png")
image mouse_hand11 = Image("MOUSE/link/frame_10_delay-0.08s.png")
image mouse_hand12 = Image("MOUSE/link/frame_11_delay-0.08s.png")

image mouse_menu1 = Image("MOUSE/menu/frame_00_delay-0.08s.png")
image mouse_menu2 = Image("MOUSE/menu/frame_01_delay-0.08s.png")
image mouse_menu3 = Image("MOUSE/menu/frame_02_delay-0.08s.png")
image mouse_menu4 = Image("MOUSE/menu/frame_03_delay-0.08s.png")
image mouse_menu5 = Image("MOUSE/menu/frame_04_delay-0.08s.png")
image mouse_menu6 = Image("MOUSE/menu/frame_05_delay-0.08s.png")
image mouse_menu7 = Image("MOUSE/menu/frame_06_delay-0.08s.png")
image mouse_menu8 = Image("MOUSE/menu/frame_07_delay-0.08s.png")
image mouse_menu9 = Image("MOUSE/menu/frame_08_delay-0.08s.png")
image mouse_menu10 = Image("MOUSE/menu/frame_09_delay-0.08s.png")
image mouse_menu11 = Image("MOUSE/menu/frame_10_delay-0.08s.png")
image mouse_menu12 = Image("MOUSE/menu/frame_11_delay-0.08s.png")

image mouse default:
    "mouse default1" with Dissolve(.1)
    .1
    "mouse default2" with Dissolve(.1)
    .1
    "mouse default3" with Dissolve(.1)
    .1
    "mouse default4" with Dissolve(.1)
    .1
    "mouse default5" with Dissolve(.1)
    .1
    "mouse default6" with Dissolve(.1)
    .1
    "mouse default7" with Dissolve(.1)
    .1
    "mouse default8" with Dissolve(.1)
    .1
    "mouse default9" with Dissolve(.1)
    .1
    "mouse default10" with Dissolve(.1)
    .1
    "mouse default11" with Dissolve(.1)
    .1
    repeat


image mouse hand:
    "mouse_hand1" with Dissolve(.1)
    .1
    "mouse_hand2" with Dissolve(.1)
    .1
    "mouse_hand3" with Dissolve(.1)
    .1
    "mouse_hand2" with Dissolve(.1)
    .1
    "mouse_hand3" with Dissolve(.1)
    .1
    "mouse_hand4" with Dissolve(.1)
    .1
    "mouse_hand5" with Dissolve(.1)
    .1
    "mouse_hand6" with Dissolve(.1)
    .1
    "mouse_hand7" with Dissolve(.1)
    .1
    "mouse_hand8" with Dissolve(.1)
    .1
    "mouse_hand9" with Dissolve(.1)
    .1
    "mouse_hand10" with Dissolve(.1)
    .1
    "mouse_hand11" with Dissolve(.1)
    .1
    "mouse_hand12" with Dissolve(.1)
    .1
    repeat

image mouse menu:
    "mouse_menu1" with Dissolve(.1)
    .1
    "mouse_menu2" with Dissolve(.1)
    .1
    "mouse_menu3" with Dissolve(.1)
    .1
    "mouse_menu4" with Dissolve(.1)
    .1
    "mouse_menu5" with Dissolve(.1)
    .1
    "mouse_menu6" with Dissolve(.1)
    .1
    "mouse_menu7" with Dissolve(.1)
    .1
    "mouse_menu8" with Dissolve(.1)
    .1
    "mouse_menu9" with Dissolve(.1)
    .1
    "mouse_menu10" with Dissolve(.1)
    .1
    "mouse_menu11" with Dissolve(.1)
    .1
    "mouse_menu12" with Dissolve(.1)
    .1
    repeat


define config.mouse_displayable = MouseDisplayable(
    "mouse default", 40, 40
).add("button", "mouse hand", 40, 40
).add("menu", "mouse menu", 40, 40)
