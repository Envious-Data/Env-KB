### What is this?

[EnvKB-FW.zip](http://github.com/Envious-Data/Env-KB/blob/main/_Firmware/EnvKB-FW.zip) is an optmized KMK firmware package, once you have flashed circuitpython to your raspberry pi pico you can drop the contents of this zip onto the "Circuitpy" drive.

be sure to remove code.py and if you need or want to make adjustment to the keymap then edit main.py.

CircuitPython-KMK, This is a Circuitpython fork that has some HID features disabled, this is a tempoary measure as some features which we could use are not implemented in circuitpython, in 7.0 we'll be able to override USB VID and which USB Descriptors within a config file on the MCU.


If you've designed your own keyboard and it happens to be similar in its schematic you can use my keymap (as an example), I couldnt find a iso or ansi TKL keymap for KMK so there is mine if needed. The keymap also contains a basic example for an aditional layer, the menu/option key has been replaced with a layer 1 modifier.

### LEDs!
as of when KMK was last (majorly) updated circuitpython didnt support HID out for LED status (like capslock, numlock, scroll lock). Circuitpython now supports these features but KMK hasnt been updated and I'm not very good at complex python coding so for now the keyboard wont have LEDs other than power and initilization.