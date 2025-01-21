import pygame
import math

def get_angle(x, y):
    """
    Calculate the angle of the joystick movement.
    Up is 0 degrees, right is 90, down is 180, and left is 270.
    """
    if x == 0 and y == 0:
        return None  # No movement detected

    # atan2(y, x) assumes that positive y is down, we want to invert that.
    # We swap the roles of x and y and adjust for the system where up is 0
    angle = math.degrees(math.atan2(x, -y))  # Invert y and swap axes
    angle = (angle + 360) % 360  # Normalize angle to [0, 360)

    return angle


def main():
    # Initialize Pygame and joystick module
    pygame.init()
    pygame.joystick.init()

    # Detect connected joysticks
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        print("No joysticks detected. Please connect a joystick and try again.")
        return

    print("Available joysticks:")
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        print(f"{i}: {joystick.get_name()}")

    # Prompt user to select a joystick
    selected_index = -1
    while selected_index < 0 or selected_index >= joystick_count:
        try:
            selected_index = int(input(f"Select a joystick (0-{joystick_count - 1}): "))
        except ValueError:
            print("Invalid input. Please enter a number.")

    joystick = pygame.joystick.Joystick(selected_index)
    joystick.init()
    print(f"Using joystick: {joystick.get_name()}")

    # Main loop to detect joystick angles
    running = True
    print("Move the joystick to see the angle. Press Ctrl+C to exit.")
    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    x = joystick.get_axis(0)  # X-axis (range [-1, 1])
                    y = joystick.get_axis(1)  # Y-axis (range [-1, 1])

                    x_scaled = x * 25706
                    y_scaled = y * 25706

                    angle = get_angle(x_scaled, y_scaled)
                    if angle is not None:
                        print(f"Angle: {angle:.2f} degrees")

            pygame.time.wait(50)  # Limit update rate

    except KeyboardInterrupt:
        print("Exiting...")

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
