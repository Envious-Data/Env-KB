#PiPi-GHERKIN - Raspberry Pi PICO
#Rpi pico keyboard keymap, I used the gherkin keymap as a example :)
import board
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.hid import HIDModes

envkb = KMKKeyboard()
envkb.col_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP19, board.GP18, board.GP17, board.GP16)
envkb.row_pins = (board.GP20, board.GP21, board.GP22, board.GP26, board.GP27, board.GP28)
envkb.diode_orientation = DiodeOrientation.COLUMNS
envkb.debug_enabled = False
nokey = KC.NO
envkb.keymap = [
    [
        KC.ESC, nokey, KC.F1, KC.F2, KC.F3, KC.F4, nokey, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.PSCREEN, KC.SCROLLLOCK, KC.PAUSE,
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, nokey, KC.BSPC, KC.INS, KC.HOME, KC.PGUP,
        KC.TAB, nokey, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.ENT, KC.DEL, KC.END, KC.PGDN,
        KC.CAPS, nokey, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.NUHS, nokey, nokey, nokey, nokey,
        KC.LSFT, KC.NONUS_BSLASH, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, nokey, KC.RSHIFT, nokey, nokey, KC.UP, nokey,
        KC.LCTL, KC.LGUI, nokey, KC.LALT, nokey, nokey, KC.SPC, nokey,nokey, nokey, KC.RALT, KC.RGUI, nokey, KC.APP, KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT,
    ],
]

#Simple thing to enable LED on pi once this script is executed
import board
import digitalio
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = True
#At this point once the LED is enabled the keyboard should be usable
if __name__ == '__main__':
    envkb.go(hid_type=HIDModes.USB) #Wired USB enables