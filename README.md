# Env-KB
 A custom mechanical keyboard inspired by the CFTKB Mysterium.
 
- Project Name: EnvKB80
- Nickname: Delirium

![Updated PCB](https://raw.githubusercontent.com/Envious-Data/Env-KB/main/_pictures/KBFront.png)

![Rev0 Build](https://raw.githubusercontent.com/Envious-Data/Env-KB/main/_pictures/Rev.0/Built/DSC_0826.JPG)


### About:
This is a raspberry pi pico powered keyboard I designed as I wanted something similar to a CFTKB Mysterium but easier to solder and a bit more robustly designed.

### Firmware
Pre-compiled firmwares can be found [here](https://github.com/Envious-Data/EnvKB-QMK/tree/main/_PREBUILTFIRMWARES)
- to flash a raspberry pi pico or any RP2040 board you need to hold the bootsel button while plugging in the USB, it'll show up as a USB drive called RP2-boot, you can then drag and drop a UF2 firmware file onto the pico, it will reboot its self.

### Parts
- 1x Type-C-31-M-14
- 90x 1n4148 DO-35
- 90x MX keyboard switches (5 pin advised if without switch plate)
- 3x 5.1K 1/4W resistors
- 1x 3mm LED
- 1x 1x04 2.54mm pin socket (optional oled)
- 1x Panasonic EVQPU SMD switch (optional reset)
- raspberry pi pico

- 10x m2 female standoffs 10mm 
- 20x m2 screws <5mm

### Building
Most part orientations should be marked on the PCB however it is important to note that you NEED to connect the pads under the MCU to the respective pads on the board for USB to work, you also need 5.1K resistors to work with USB PD compatible ports.

the type-c port may be difficult for some to solder so use loads of flux and minimal amounts of solder, its best to solder the large 4 outer pins of the shell first.


### Why a RPI Pico?
uh well why not, I think it would be a nice example for people to use as a example.
When I came up with the idea of this keyboard there was 1 other raspberry pi pico keyboard so I decided it would be cool to make a keyboard.

### PCBWAY

[![PCBWAY](https://4.bp.blogspot.com/-sn_1frB-tto/W_eevs6kyzI/AAAAAAAANhE/ZPlkvH6ysTAMuBJlbtYsSxkC28xaRrZugCLcBGAs/s1600/PCBWay%2BTlogo.png)](http://pcbway.com)

[PCBWAY](http://pcbway.com) Kindly sponsored a batch of PCBs of which you can see [pictures](_pictures/Hotswap/) of inside the pictures folder.
