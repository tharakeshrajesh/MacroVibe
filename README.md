# MacroVibe
A lazily made macropad that doesn't use a key matrix and has one rotary encoder.

![image](/images/whole.png)
![image](/images/pcb_3d.png)
![image](/images/side_view.png)

### Schematics and PCB
![image](/images/schematics.png)
![image](/images/pcb_kicad.png)

Both were made in KiCad 9.0, highly recommend, will use from now on.

### Case
![image](/images/case.png)

This case was made in Fusion360, I spent most of the time on this stupid case than any other part of the project because the keyholes and other holes would not line up
so I had to try like 5 times before I kind of got it.

### Firmware
![image](/images/firmware.png)

Firmware was coded using KMK so you will need a program to flash your RP2040.
Keycodes/macros are not set in the code so you will have to manually set those in main.py.

### Setup
1. Get the cases and PCB printed and order the parts.
2. Solder the parts onto the PCB.
3. Assemble the PCB and case.
4. Flash your edited main.py onto the RP2040.
5. Pray and test.

## BOM
| Item | Quantity | Average cost (USD)|
|:----------:|:----------:|:----------:|
|XIAO RP2040 DIP|x1|~$4|
|Cherry MX Switches|x7|~$5|
|SK6812 MINI LEDs|x2|~$3|
|Blank DSA Keycaps|x7|~$6|
|M3x16 Bolt|x4|~$2|
|M3 Heatset|x4|~$1|
|Alps EC11E Rotary Encoder|x1|~$2|
|PCB|x1|~$3|
|3D printed top case|x1|~$2|
|3D printed bottom case|x1|~$2|
|Total||~$30|
<<<<<<< HEAD

### Credits
Encoder knob was made by (void)[https://www.printables.com/@void] on (printables)[https://www.printables.com]. Page (here)[https://www.printables.com/model/347536-encoder-knob].
Special thanks to alexren and qcoral for making a guide on how to make a hackpad. Page (here)[https://hackpad.hackclub.com].
=======
>>>>>>> d4087209b6da23e5d6a54caaffc7c0f2957f77c2
