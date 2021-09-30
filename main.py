def on_button_pressed_a():
    playerSprite.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

playerSprite: game.LedSprite = None
playerSprite = game.create_sprite(2, 4)

def on_forever():
    pass
basic.forever(on_forever)
