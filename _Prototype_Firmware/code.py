#PiPi-GHERKIN - Raspberry Pi PICO
#Rpi pico keyboard keymap, I used the gherkin keymap as a example :)
print("Starting")

#run the led
import board
import pwmio
import time
import supervisor

led = pwmio.PWMOut(board.GP25, frequency=1, duty_cycle=1024, variable_frequency=True)

exec(open('oled.py').read())



import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.keys import KC, make_key
envkb = KMKKeyboard()

envkb.col_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP19, board.GP18, board.GP17, board.GP16)
envkb.row_pins = (board.GP20, board.GP21, board.GP22, board.GP26, board.GP27, board.GP28)
envkb.diode_orientation = DiodeOrientation.COLUMNS

rollover_cols_every_rows = 4
envkb.diode_orientation = DiodeOrientation.COLUMNS
envkb.debug_enabled = False

layers = Layers()
envkb.modules = [layers]

nokey = KC.NO
envkb.keymap = [
    [
    #Layer 0?
        KC.ESC, nokey, KC.F1, KC.F2, KC.F3, KC.F4, nokey, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.PSCREEN, KC.SCROLLLOCK, KC.PAUSE,
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, nokey, KC.BSPC, KC.INS, KC.HOME, KC.PGUP,
        KC.TAB, nokey, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.DEL, KC.END, KC.PGDN,
        KC.CAPS, nokey, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.NUHS, KC.ENT, nokey, nokey, nokey,
        KC.LSFT, KC.NONUS_BSLASH, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, nokey, KC.RSHIFT, nokey, nokey, KC.UP, nokey,
        KC.LCTL, KC.LGUI, nokey, KC.LALT, nokey, nokey, KC.SPC, nokey,nokey, nokey, KC.RALT, KC.RGUI, nokey, KC.MO(1), KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT,
    ],
    [
    #Layer 1
        KC.TRNS, nokey, KC.F13, KC.F14, KC.F15, KC.F16, nokey, KC.F17, KC.F18, KC.F19, KC.F20, KC.F21, KC.F22, KC.F23, KC.F24, KC.MUTE, KC.VOLD, KC.VOLU,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, nokey, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, nokey, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, nokey, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, nokey, nokey, nokey, nokey,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, nokey, KC.TRNS, nokey, nokey, KC.TRNS, nokey,
        KC.TRNS, KC.TRNS, nokey, KC.TRNS, nokey, nokey, KC.TRNS, nokey, nokey, nokey, KC.TRNS, KC.TRNS, nokey, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    ],
]

def usbfunc():
    
    if __name__ == '__main__':
        led.duty_cycle=16384
        led.frequency=144
        print("Started")
        envkb.go()
        raise Exception('Something has caused an error.')
        
try:
    usbfunc()
except KeyboardInterrupt:
    led.duty_cycle=0
    print("Keyboard Interrupt")
except Exception as e:
    print(e)
    led.duty_cycle=0
    supervisor.reload()


supervisor.reload()