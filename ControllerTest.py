import vgamepad as vg
import keyboard
from time import sleep

# Initialize the virtual gamepad
gamepad = vg.VX360Gamepad()

print("Press ESC to quit...")

try:
    while not keyboard.is_pressed('esc'):
        # Map WASD to left joystick
        if keyboard.is_pressed('w') and keyboard.is_pressed('a'):
            gamepad.left_joystick(x_value=-23570, y_value=22761)  # (left softdrift)
        elif keyboard.is_pressed('w') and keyboard.is_pressed('d'):
            gamepad.left_joystick(x_value=23570, y_value=22761)  # (right softdrift)
        elif keyboard.is_pressed('s') and keyboard.is_pressed('a'):
            gamepad.left_joystick(x_value=-23169, y_value=-23169) # (high left glider)
        elif keyboard.is_pressed('s') and keyboard.is_pressed('d'):
            gamepad.left_joystick(x_value=23169, y_value=-23169) # (high right glider)
        elif keyboard.is_pressed('w'):
            gamepad.left_joystick(x_value=0, y_value=32767)  # Up
        elif keyboard.is_pressed('a'):
            gamepad.left_joystick(x_value=-32767, y_value=0)  # Left
        elif keyboard.is_pressed('d'):
            gamepad.left_joystick(x_value=32767, y_value=0)  # Right
        elif keyboard.is_pressed('s'):
            gamepad.left_joystick(x_value=0, y_value=-32767)  # Down
        else:
            gamepad.left_joystick(x_value=0, y_value=0)  # Neutral

        # Map buttons
        if keyboard.is_pressed('\\'):
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        else:
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)

        if keyboard.is_pressed('backspace'):
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        else:
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)

        if keyboard.is_pressed(']'):
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        else:
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

        if keyboard.is_pressed('insert'):
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        else:
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)

        if keyboard.is_pressed('shift'):
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        else:
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)

        if keyboard.is_pressed('space'):
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        else:
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)

        # Map arrow keys to D-pad
        if keyboard.is_pressed('up'):
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        else:
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)

        if keyboard.is_pressed('down'):
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        else:
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)

        if keyboard.is_pressed('left'):
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        else:
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)

        if keyboard.is_pressed('right'):
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        else:
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)

        # Update the gamepad state
        gamepad.update()

        sleep(0.01)  # Polling rate to reduce CPU usage, this is for my school potato. might as will just remove it lmao if you have a good system

except KeyboardInterrupt:
    print("Exiting...")
