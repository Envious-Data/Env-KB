#PiPi-GHERKIN - Raspberry Pi PICO
#Rpi pico keyboard keymap, I used the gherkin keymap as a example :)
#print("Booting")
import board
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.hid import HIDModes

from kmk.keys import KC, make_key
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import time
import usb_hid

import board
import pwmio

from adafruit_hid.consumer_control_code import ConsumerControlCode

envkb = KMKKeyboard()
envkb.col_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP19, board.GP18, board.GP17, board.GP16)
envkb.row_pins = (board.GP20, board.GP21, board.GP22, board.GP26, board.GP27, board.GP28)
envkb.diode_orientation = DiodeOrientation.COLUMNS
envkb.debug_enabled = False
nokey = KC.NO

# The keyboard object!
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)


def examplefunc(*args, **kwargs):
    #A example function for if you want to print strings
    keyboard_layout.write('Shrek is love\n')
    #I basically lifted some code from a adafruit guide so there is likely a simpler solution here

def resetfunction(*args, **kwargs):
    led.frequency = 1
    led.duty_cycle = 5000
    #very anoying flashing
    time.sleep(0.5)
    import supervisor
    print("I've been asked to reboot")
    #print something for logging atleast
    supervisor.reload()


#couple custom keys made
EXAMPLE = make_key(on_press=examplefunc)
RESETME = make_key(on_press=resetfunction)

envkb.keymap = [
    [
    #Layer 0?
        KC.ESC, nokey, KC.F1, KC.F2, KC.F3, KC.F4, nokey, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.PSCREEN, KC.SCROLLLOCK, KC.PAUSE,
        KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, nokey, KC.BSPC, KC.INS, KC.HOME, KC.PGUP,
        KC.TAB, nokey, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.ENT, KC.DEL, KC.END, KC.PGDN,
        KC.CAPS, nokey, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.NUHS, nokey, nokey, nokey, nokey,
        KC.LSFT, KC.NONUS_BSLASH, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, nokey, KC.RSHIFT, nokey, nokey, KC.UP, nokey,
        KC.LCTL, KC.LGUI, nokey, KC.LALT, nokey, nokey, KC.SPC, nokey,nokey, nokey, KC.RALT, KC.RGUI, nokey, KC.MO(1), KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT,
    ],
    [
    #Layer 1
        KC.TRNS, nokey, KC.F13, KC.F14, KC.F15, KC.F16, nokey, KC.F17, KC.F18, KC.F19, KC.F20, KC.F21, KC.F22, KC.F23, KC.F24, KC.MUTE, KC.VOLD, KC.VOLU,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, nokey, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, nokey, KC.TRNS, KC.TRNS, KC.TRNS, RESETME, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, nokey, EXAMPLE, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, nokey, nokey, nokey, nokey,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, nokey, KC.TRNS, nokey, nokey, KC.TRNS, nokey,
        KC.TRNS, KC.TRNS, nokey, KC.TRNS, nokey, nokey, KC.TRNS, nokey, nokey, nokey, KC.TRNS, KC.TRNS, nokey, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    ],
]

#Simple thing to enable LED on pi once this script is executed
led = pwmio.PWMOut(board.GP25, frequency=1, duty_cycle=0, variable_frequency=True)
led.frequency = 60
led.duty_cycle = 500

#At this point once the LED is enabled the keyboard should be usable
#print("Booted")
#print("")
#print("       _                        ")
#print("       \`*-.                    ")
#print("        )  _`-.                 ")
#print("       .  : `. .                ")
#print("       : _   '  \               ")
#print("       ; *` _.   `*-._          ")
#print("       `-.-'          `-.       ")
#print("         ;       `       `.     ")
#print("         :.       .        \    ")
#print("         . \  .   :   .-'   .   ")
#print("         '  `+.;  ;  '      :   ")
#print("         :  '  |    ;       ;-. ")
#print("         ; '   : :`-:     _.`* ;")
#print("      .*' /  .*' ; .*`- +'  `*' ")
#print("      `*-*   `*-*  `*-*'        ")
#print("")

def usbfunc():
    if __name__ == '__main__':
        envkb.go(hid_type=HIDModes.USB) #Wired USB enable
        raise Exception('Something has caused an error.')
try:        
    usbfunc()
except Exception as e:
    import supervisor
    print(e)
    led.value = False
    supervisor.reload()

supervisor.reload()
#last ditch effor to reset the MCU, if this is being ran then something really is wrong lol