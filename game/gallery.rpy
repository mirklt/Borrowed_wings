default persistent.cg_1 = False
default persistent.cg_2 = False
default persistent.cg_3 = False
default persistent.cg_4 = False
default persistent.cg_5 = False
default persistent.cg_6 = False
default persistent.cg_7 = False
default persistent.cg_8 = False
default persistent.cg_9 = False
default persistent.cg_10 = False
default persistent.cg_meet = False
default persistent.cg_angel = False
default persistent.cg_hill = False
default persistent.cg_roomnight = False

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

    g.button("cg4")
    g.condition("persistent.cg_4")
    g.image("images/bg/bg room1.png")

    g.button("cg5")
    g.condition("persistent.cg_5")
    g.image("images/bg/bg room table.png")

    g.button("cg6")
    g.condition("persistent.cg_6")
    g.image("images/bg/6.jpg")

    g.button("cg7")
    g.condition("persistent.cg_7")
    g.image("images/bg/bg classroom.png")

    g.button("cg8")
    g.condition("persistent.cg_8")
    g.image("images/bg/bg f fire.png")


    g.button("cg9")
    g.condition("persistent.cg_9")
    g.image("images/bg/bg zephir cry 1.png")


    g.button("cg10")
    g.condition("persistent.cg_10")
    g.image("images/bg/bg zephir cry 3.png")

    g.button("cgmeet")
    g.condition("persistent.cg_meet")
    g.image("images/bg/bg first meet.png")

    g.button("cgangel")
    g.condition("persistent.cg_angel")
    g.image("images/bg/bg angel.jpg")

    g.button("cghill")
    g.condition("persistent.cg_hill")
    g.image("images/bg/hill.png")

    g.button("cgroomnight")
    g.condition("persistent.cg_roomnight")
    g.image("images/bg/bg room night.png")



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

    style_prefix "gallery"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        text _("Галерея") xalign 0.5

        viewport:
            xalign 0.5
            xsize (1080 + gui.scrollbar_size + 20)
            ysize 720
            scrollbars "vertical"
            mousewheel True
            draggable True
            side_yfill True

            vpgrid:
                cols 3
                spacing 60
                xalign 0.5

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

                if persistent.cg_4:
                    imagebutton:
                        idle At(auto_thumb("gallery/bg room1.png"), thumb_idle_fx)
                        hover At(auto_thumb("gallery/bg room1.png"), thumb_hover_fx)
                        action g.Action("cg4")
                else:
                    imagebutton:
                        idle At(auto_thumb("gallery/locked.jpg"), thumb_idle_fx)
                        hover At(auto_thumb("gallery/locked.jpg"), thumb_hover_fx)
                        action NullAction()

                if persistent.cg_5:
                    imagebutton:
                        idle At(auto_thumb("gallery/bg room table.png"), thumb_idle_fx)
                        hover At(auto_thumb("gallery/bg room table.png"), thumb_hover_fx)
                        action g.Action("cg5")
                else:
                    imagebutton:
                        idle At(auto_thumb("gallery/locked.jpg"), thumb_idle_fx)
                        hover At(auto_thumb("gallery/locked.jpg"), thumb_hover_fx)
                        action NullAction()

                if persistent.cg_6:
                    imagebutton:
                        idle At(auto_thumb("gallery/6.jpg"), thumb_idle_fx)
                        hover At(auto_thumb("gallery/6.jpg"), thumb_hover_fx)
                        action g.Action("cg6")
                else:
                    imagebutton:
                        idle At(auto_thumb("gallery/locked.jpg"), thumb_idle_fx)
                        hover At(auto_thumb("gallery/locked.jpg"), thumb_hover_fx)
                        action NullAction()

                if persistent.cg_7:
                    imagebutton:
                        idle At(auto_thumb("gallery/bg classroom.png"), thumb_idle_fx)
                        hover At(auto_thumb("gallery/bg classroom.png"), thumb_hover_fx)
                        action g.Action("cg7")
                else:
                    imagebutton:
                        idle At(auto_thumb("gallery/locked.jpg"), thumb_idle_fx)
                        hover At(auto_thumb("gallery/locked.jpg"), thumb_hover_fx)
                        action NullAction()

                if persistent.cg_8:
                    imagebutton:
                        idle At(auto_thumb("gallery/bg f fire.png"), thumb_idle_fx)
                        hover At(auto_thumb("gallery/bg f fire.png"), thumb_hover_fx)
                        action g.Action("cg8")
                else:
                    imagebutton:
                        idle At(auto_thumb("gallery/locked.jpg"), thumb_idle_fx)
                        hover At(auto_thumb("gallery/locked.jpg"), thumb_hover_fx)
                        action NullAction()

                if persistent.cg_9:
                    imagebutton:
                        idle At(auto_thumb("gallery/bg zephir cry 1.png"), thumb_idle_fx)
                        hover At(auto_thumb("gallery/bg zephir cry 1.png"), thumb_hover_fx)
                        action g.Action("cg9")
                else:
                    imagebutton:
                        idle At(auto_thumb("gallery/locked.jpg"), thumb_idle_fx)
                        hover At(auto_thumb("gallery/locked.jpg"), thumb_hover_fx)
                        action NullAction()

                if persistent.cg_10:
                    imagebutton:
                        idle At(auto_thumb("gallery/bg zephir cry 3.png"), thumb_idle_fx)
                        hover At(auto_thumb("gallery/bg zephir cry 3.png"), thumb_hover_fx)
                        action g.Action("cg4")
                else:
                    imagebutton:
                        idle At(auto_thumb("gallery/locked.jpg"), thumb_idle_fx)
                        hover At(auto_thumb("gallery/locked.jpg"), thumb_hover_fx)
                        action NullAction()

                if persistent.cg_meet:
                    imagebutton:
                        idle At(auto_thumb("gallery/bg first meet.png"), thumb_idle_fx)
                        hover At(auto_thumb("gallery/bg first meet.png"), thumb_hover_fx)
                        action g.Action("cgmeet")
                else:
                    imagebutton:
                        idle At(auto_thumb("gallery/locked.jpg"), thumb_idle_fx)
                        hover At(auto_thumb("gallery/locked.jpg"), thumb_hover_fx)
                        action NullAction()

                if persistent.cg_angel:
                    imagebutton:
                        idle At(auto_thumb("gallery/bg angel.jpg"), thumb_idle_fx)
                        hover At(auto_thumb("gallery/bg angel.jpg"), thumb_hover_fx)
                        action g.Action("cgangel")
                else:
                    imagebutton:
                        idle At(auto_thumb("gallery/locked.jpg"), thumb_idle_fx)
                        hover At(auto_thumb("gallery/locked.jpg"), thumb_hover_fx)
                        action NullAction()

                if persistent.cg_hill:
                    imagebutton:
                        idle At(auto_thumb("gallery/hill.png"), thumb_idle_fx)
                        hover At(auto_thumb("gallery/hill.png"), thumb_hover_fx)
                        action g.Action("cghill")
                else:
                    imagebutton:
                        idle At(auto_thumb("gallery/locked.jpg"), thumb_idle_fx)
                        hover At(auto_thumb("gallery/locked.jpg"), thumb_hover_fx)
                        action NullAction()

                if persistent.cg_roomnight:
                    imagebutton:
                        idle At(auto_thumb("gallery/bg room night.png"), thumb_idle_fx)
                        hover At(auto_thumb("gallery/bg room night.png"), thumb_hover_fx)
                        action g.Action("cgroomnight")
                else:
                    imagebutton:
                        idle At(auto_thumb("gallery/locked.jpg"), thumb_idle_fx)
                        hover At(auto_thumb("gallery/locked.jpg"), thumb_hover_fx)
                        action NullAction()

            # if persistent.cg_4:
            #     imagebutton:
            #         idle At(auto_thumb("gallery"), thumb_idle_fx)
            #         hover At(auto_thumb("gallery"), thumb_hover_fx)
            #         action g.Action("cg4")
            # else:
            #     imagebutton:
            #         idle At(auto_thumb("gallery/locked.jpg"), thumb_idle_fx)
            #         hover At(auto_thumb("gallery/locked.jpg"), thumb_hover_fx)
            #         action NullAction()

        textbutton _("Назад") action Return() xalign 0.5

style gallery_vscrollbar is vscrollbar
style gallery_vscrollbar:
    xoffset 60

style gallery_button is button
style gallery_button_text is button_text

style gallery_button:
    xpadding 30
    ypadding 16

style gallery_button_text:
    size 60
