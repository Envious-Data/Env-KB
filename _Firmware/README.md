### What is this?

[EnvKB-FW.zip](http://github.com/Envious-Data/Env-KB/blob/main/_Firmware/EnvKB-FW.zip) is an optmized KMK firmware package, once you have flashed circuitpython to your raspberry pi pico you can drop the contents of this zip onto the "Circuitpy" drive.

be sure to remove code.py and if you need or want to make adjustment to the keymap then edit main.py.

[Custom Circuitpython UF2](https://github.com/Envious-Data/Env-KB/blob/main/_Firmware/Adafruit%CircuitPython%7.0.0-alpha.1-55-gebfe36c9a.uf2) this is a custom circuitpython firmware that has some HID stuff disabled and some things renamed so your raspberry pi pico shows up more like a keyboard and less a Raspberry pi, Do note that Storage mounting is disabled so either flash this after you've uploaded your files or upload them via something like thonny. (The code used to compile this UF2 is unmodified I just used some extra flags to optmize and disable certain features.)

In circuitpython 7.0 we should be able to disable extra HID descriptors via a config file but for now as said Ive just compiled a version with these extra HID devices disabled.

If you've designed your own keyboard and it happens to be similar in its schematic you can use my keymap (as an example), I couldnt find a iso or ansi TKL keymap for KMK so there is mine if needed. The keymap also contains a basic example for an aditional layer, the menu/option key has been replaced with a layer 1 modifier.

### LEDs!
as of when KMK was last (majorly) updated circuitpython didnt support HID out for LED status (like capslock, numlock, scroll lock). Circuitpython now supports these features but KMK hasnt been updated and I'm not very good at complex python coding so for now the keyboard wont have LEDs other than power and initilization.