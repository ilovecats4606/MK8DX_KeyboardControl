import math

# Current joystick values
x_value =  #PUT X VALUE
y_value =  #PUT Y VALUE


max_magnitude = 32767  # 16bit

# Calculate current magnitude
magnitude = math.sqrt(x_value**2 + y_value**2)

# Scale values to maximum magnitude
x_new = int(x_value * max_magnitude / magnitude)
y_new = int(y_value * max_magnitude / magnitude)

print(f"Scaled joystick values: x={x_new}, y={y_new}")
