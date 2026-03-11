init -2:
    image with_eye = "images/eye.webp"
    image with_eyes = "images/eyes.webp"

define eyes_blink = ImageDissolve("images/eyes.webp", 0.4, ramplen=128, reverse=True)
