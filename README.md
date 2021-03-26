# Env-KB
 A custom mechanical keyboard inspired by the CFTKB Mysterium

![Front](KBFront.png?raw=true "Front of PCB")

[Build Guide and Parts List](../blob/main/guide-and-parts.pdf)

### What is to do?
* Right now for the first 5 PCBs I have, ive ordered some wood to make a backing plate and im looking around for some cheap foam I can use for damping.
* For Rev 1 onward I have a decent idea with what I want to do and at some point they should all be generally forward compatible once major changes stop.

### Why a RPI Pico?
uh well why not, I think it would be a nice example for people to use as a example since python is surprizingly simple.
Ive made sure to leave GPIO 0 and 1 empty incase someone wants to add something like a I2C OLED or something of the sorts since we'll be using circuitpython.
And to add ive already tested everything needed so all I need to do is have a PCB made and see if all works as expected once I adjust the row and column pins on the MCU.

### ISO only?
Yep but eventually ill add support for different width and spacing bottom row, not sure if ill personally make a ansi version since im just learning this stuff and same goes for RGB, im not sure if I personally want to bother with that.

### Deviations!
Im not sure what to think about the base/backing place that the mysterium has though it does its job, For now I shall mimick its design though ive never been fond of philips head so if its easily possible to get my hands on robertson or allen head M2 screws (probably going to be allen).
