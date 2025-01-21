allows softdrifting control with keyboard, good for emulator

Left Joystick (WASD)
W: Move the left joystick up (Full forward).

A: Move the left joystick left (Full left).

D: Move the left joystick right (Full right).

S: Move the left joystick down.

W + A: Up-left diagonal (Softdrift).

W + D: Up-right diagonal (Softdrift.

S + A: Down-left diagonal (45, primarily for gliding).

S + D: Down-right diagonal (45, primarily for gliding).


Buttons

\\: Press the A button.

Backspace: Press the X button.

]: Press the B button.

Insert: Press the Y button.

Shift: Press the R button.

Space: Press the L button.


D-Pad (Arrow Keys)

Up Arrow: Press the D-pad up.

Down Arrow: Press the D-pad down.

Left Arrow: Press the D-pad left.

Right Arrow: Press the D-pad right.


FILES:

ControllerTest.py - the keyboard controller emulator. Dependency is vgamepad, keyboard. Has polling rate delay of 10ms, can adjust by editing the file

ControllerJoystickMeasure.py - shitty angle measuring app. Dependency is pygame.

temppythonmath.py - calculate the X and Y coords for controller. It is so jank, sometimes the values come out negative when they are supposed to be positive and vice versa, so may need to play around with values.

ye.py - temppythonmath.py would not give the absolute edge for coords that were not 0, 90, 180, 270. So this file will make it by entering X and Y values in the file.


have fun lmao, shitty coding and shitty keybinds :))))
