### What is this?

"EnvKB-FW.zip" is an optmized KMK firmware package, once you have flashed circuitpython to your raspberry pi pico you can drop the contents of this zip onto the "Circuitpy" drive.

Be sure to make sure the contents of my zip files are the only thing on your raspberry pi pico otherwise it may try to run another file and not my keyboard code.

also there are two zips here, If you happen to have a Green PCB prototype from me then use the zip labled "prototype" otherwise use a zip matching your revision number which you can find a small triangle by the diode number to indicate revision.

![What your Raspberry Pi Drive Should Look Like](example.jpg)

CircuitPython-KMK, This is a Circuitpython fork that has some HID features disabled, this is a tempoary measure as some features which we could use are not implemented in circuitpython, in 7.0 we'll be able to override USB VID and which USB Descriptors within a config file on the MCU.


If you've designed your own keyboard and it happens to be similar in its schematic you can use my keymap (as an example), I couldnt find a iso or ansi TKL keymap for KMK so there is mine if needed. The keymap also contains a basic example for an aditional layer, the menu/option key has been replaced with a layer 1 modifier.

### LEDs!
as of when KMK was last (majorly) updated circuitpython didnt support HID out for LED status (like capslock, numlock, scroll lock). Circuitpython now supports these features but KMK hasnt been updated and I'm not very good at complex python coding so for now the keyboard wont have LEDs other than power and initilization.


## SETUP INSTRUCTIONS
The setup for any of my keyboards using a Raspberry Pi Pico should generally be the same

- Install [Circuitpython](https://circuitpython.org/board/raspberry_pi_pico/) To your Raspberry Pi Pico
- Once installed Extract "EnvKB-FW.zip" to your raspberry pi pico 
- Remove any extra files that may exist on your pico, sometimes circuitpython will have add a py file extra upon flashing.
- replace main.py with the respective keymap file for your keyboard, in this case for EnvKB it would be [This file](https://github.com/Envious-Data/Env-KB/blob/main/_Firmware/KMK-KEYMAP.py)
- there is a screenshot above on what the files on your Raspberry Pi Pico should look like


## POSSIBLE ISSUES
Circuitpython may have some driver issues with windows 7 so keep that in mind if thonny doesnt work and you are trying to debug.
https://learn.adafruit.com/circuit-playground-express-circuitpython-5-minute-guide/connect

