# Env-KB
 A custom mechanical keyboard inspired by the CFTKB Mysterium

![Front](_docs/KBFront.png?raw=true "Front of PCB")

![PCB](_Pictures/PCB3.JPG?raw=true "A Rev0 PCB")

[Build Guide and Parts List](_docs/guide-and-parts.pdf)

### What is to do?
* For Rev#1 and onward I would like the option of a case, I think a sandwich type design would be best.
* I currently dont know how to use CAD software so the above point will either need to be done by someone else or Ill try to figure out some CAD software.

I would like to keep as much possible open source and compatible outside this keyboard because there is a serious lack of TKL things so for example a TKL plate is something I'd like to be open source and avaliable to others.
That said there is a lack of TKL things in the mechanical keyboard market so Im always happy to try and add more ISO and TKL things.


### Why a RPI Pico?
uh well why not, I think it would be a nice example for people to use as a example since python is surprizingly simple.
Ive made sure to leave GPIO 0 and 1 empty incase someone wants to add something like a I2C OLED or something of the sorts since we'll be using circuitpython.
And to add ive already tested everything needed so all I need to do is have a PCB made and see if all works as expected once I adjust the row and column pins on the MCU.

### ISO only?
As of recent commits this keyboard now supports ANSI layout! *yay!*
This keyboard should be compatible with any language layout that is physically the same as ISO UK (ISO-DE for example)

You should be able to use my keymap on a keyboard of your own design so long as its wiring setup is generally the same, Vertical aligned diodes and row incrementing keys.

### Misc bits!
Feel free to make your own PCBs of this keyboard, if you feel like supporting me you can "Buy me a coffee"
Paypal: Kel786@msn.com

(Ill publish some gerber files in the future)

### Things of handy dandy nature!
This keyboard makes use of KMKfw and CircuitPython
* https://github.com/KMKfw/kmk_firmware
* https://github.com/adafruit/circuitpython
