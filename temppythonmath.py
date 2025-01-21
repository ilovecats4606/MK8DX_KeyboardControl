import math

# Function to calculate x and y values based on the angle
def calculate_joystick_values(angle_degrees, magnitude=-25706):
    angle_radians = math.radians(angle_degrees)
    
    # Calculate x and y components
    x_value = int(magnitude * math.cos(angle_radians))
    y_value = int(magnitude * math.sin(angle_radians))
    
    return x_value, y_value

# User input for angle
angle_degrees = float(input("Enter the angle in degrees: "))

# Calculate the x and y values
x, y = calculate_joystick_values(angle_degrees)

# Output the result
print(f"For an angle of {angle_degrees} degrees:")

print(f"x value: {-y if y > 0 else abs(y)}")
print(f"y value: {-x if x > 0 else abs(x)}")
