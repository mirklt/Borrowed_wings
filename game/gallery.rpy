default persistent.cg_1 = False
default persistent.cg_2 = False
default persistent.cg_3 = False

init python:
    g = Gallery()

    g.button("cg1")
    g.condition("persistent.cg_1")
    g.image("images/bg/bg night.png")

    g.button("cg2")
    g.condition("persistent.cg_2")
    g.image("images/bg/bg 1.png")

    g.button("cg3")
    g.condition("persistent.cg_3")
    g.image("images/bg/bg falling.jpg")

    g.transition = Dissolve(0.3)

    def auto_thumb(img_path):
        return AlphaMask(
            Transform(img_path, size=(320, 180)),
            Transform("gallery/mask_thumb.png", size=(320, 180))
        )

transform thumb_idle_fx:
    matrixcolor SaturationMatrix(0.55) * BrightnessMatrix(-0.18)

transform thumb_hover_fx:
    matrixcolor SaturationMatrix(1.0) * BrightnessMatrix(0.08)

screen gallery_menu():

    tag menu

    add "gui/main_menu.png"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        text "Галерея" xalign 0.5

        grid 3 1:
            spacing 60

            if persistent.cg_1:
                imagebutton:
                    idle At(auto_thumb("gallery/bg night.png"), thumb_idle_fx)
                    hover At(auto_thumb("gallery/bg night.png"), thumb_hover_fx)
                    action g.Action("cg1")
            else:
                imagebutton:
                    idle At(auto_thumb("gallery/locked.jpg"), thumb_idle_fx)
                    hover At(auto_thumb("gallery/locked.jpg"), thumb_hover_fx)
                    action NullAction()

            if persistent.cg_2:
                imagebutton:
                    idle At(auto_thumb("gallery/bg 1.png"), thumb_idle_fx)
                    hover At(auto_thumb("gallery/bg 1.png"), thumb_hover_fx)
                    action g.Action("cg2")
            else:
                imagebutton:
                    idle At(auto_thumb("gallery/locked.jpg"), thumb_idle_fx)
                    hover At(auto_thumb("gallery/locked.jpg"), thumb_hover_fx)
                    action NullAction()

            if persistent.cg_3:
                imagebutton:
                    idle At(auto_thumb("gallery/bg falling.jpg"), thumb_idle_fx)
                    hover At(auto_thumb("gallery/bg falling.jpg"), thumb_hover_fx)
                    action g.Action("cg3")
            else:
                imagebutton:
                    idle At(auto_thumb("gallery/locked.jpg"), thumb_idle_fx)
                    hover At(auto_thumb("gallery/locked.jpg"), thumb_hover_fx)
                    action NullAction()

        textbutton "Назад" action Return() xalign 0.5
