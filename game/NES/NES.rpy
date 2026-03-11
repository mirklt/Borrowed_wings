# NGES is really the ANESE emulator, by Daniel Prilik, slimmed down and plugged into Ren'Py by PyTom.

init:
    transform nes_tv_at():
        nearest True
        # высота экрана макета телевизора
        zoom 480 / 240
        pos(614, 165)

    transform nes_fullscreen_at():
        nearest True
        # высота экрана игры
        zoom config.screen_height / 240
        align (.5, .5)

    transform pad_at():
        rotate_pad False
        rotate -90
        align(1., .5)

    transform show_hide(t=.5):
        on show:
            alpha 0
            linear t alpha 1

        on hide:
            linear t alpha 0

screen NES(game="Battle City", fullscreen=True):
    key "K_q" action Return()

    if not nges.nges_available:
        modal True

        frame style "empty":
            xfill True
            yfill True
            at show_hide

            text "NES-эмулятор недоступен на этом устройстве.":
                xalign 0.5
                yalign 0.45
                text_align 0.5
                color "#ffffff"
                outlines [(2, "#000000", 0, 0)]

            textbutton "Назад":
                xalign 0.5
                yalign 0.58
                action Return()

    else:
        # recreate the emulator object each time the screen is shown.
        $ d = nges.NGES("NES/ROM/" + game + ".nes")

        frame style "empty":
            xfill True
            yfill True

            if not fullscreen:
                background "NES/images/bg.webp"
                foreground "NES/images/tv.webp"

            at show_hide

            add d:
                if fullscreen:
                    at nes_fullscreen_at

                else:
                    at nes_tv_at

        add "NES/images/gamepad.webp":
            if fullscreen:
                at show_hide, pad_at

            else:
                at show_hide
                align(.5, 1.)
