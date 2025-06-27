# KC.ESC are all place holders
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.handlers.sequences import simple_key_sequence
from kmk.modules.rgb import RGB

effects = ["rainbow", "breathing"]
num_layers = 2
current_layer = 0

keyboard = KMKKeyboard()
layers = Layers()
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
keyboard.modules.append(layers)

macros = Macros()
keyboard.modules.append(macros)

key_pins = [board.GP1, board.GP2, board.GP4, board.GP3, board.GP27, board.GP28, board.GP0]

rgb = RGB(
    pixel_pin=board.GP6,
    num_pixels=2,
    rgb_order=(1, 0, 2)
)
rgb.effect = effects[0]
keyboard.rgb = rgb
keyboard.modules.append(rgb)

encoder_handler.pins = (
    (board.GP7, board.GP29, board.GP26,),)

keyboard.matrix = KeysScanner(
    pins=key_pins,
    value_when_pressed=False,
)

@simple_key_sequence
def cycle_layer(key, keyboard):
    global current_layer
    current_layer += 1
    if current_layer > num_layers - 1:
        current_layer = 0
    keyboard.layers.set_layer(current_layer)
    current = getattr(keyboard.rgb, 'effect', 'off')
    index = effects.index(current) if current in effects else -1
    new_effect = effects[(index + 1) % len(effects)]
    keyboard.rgb.effect = new_effect

encoder_handler.map = [ (KC.VOLU, KC.VOLD, KC.MUTE),
                        (KC.LCTRL(KC.MINUS), KC.LCTRL(KC.PLUS), KC.LCTRL(KC.N0))
                        ]

keyboard.keymap = [
    [
    KC.ESC,
    KC.ESC,
    KC.ESC,
    KC.ESC,
    KC.ESC,
    KC.ESC,
    cycle_layer
    ],
    [
    KC.ESC,
    KC.ESC,
    KC.ESC,
    KC.ESC,
    KC.ESC,
    KC.ESC,
    cycle_layer
    ]
]

if __name__ == '__main__':
    keyboard.go()