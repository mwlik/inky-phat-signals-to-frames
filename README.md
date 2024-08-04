# Inky Phat (e-paper displays) SPI Signals to Images

A short script that converts the Pimoroni Inky Phat signals to frames (reversed from the behavior of the [official library](https://github.com/pimoroni/inky)).

Written during CrewCTF 2024 for the Sniff Two challenge.

Note: This would work for [Waveshare Inch E-Ink Display pHAT](https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT), with some modification cause they have similar protocols.

Another Note: the script excpects a csv file with this format (this was exported a .sal file)
```
Time [s],Packet ID,MOSI,DC
4.108880200000000,0,0x12,0x00
5.109988000000000,0,0x01,0x00
5.110044320000000,0,0xF9,0xFF
5.110062800000000,0,0x00,0xFF
```
## Images

![image](https://github.com/user-attachments/assets/59343660-4f01-4fdd-b848-ff6482ee0a8a)
![image](https://github.com/user-attachments/assets/511eee09-0989-4f0b-8420-97e06ad5762f)
