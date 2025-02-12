# VEX Python Control Loop 

""" Initialize motor control (replace with your actual VEX motor control code) """
# Example:
# from vex import Motor
# left_motor = Motor(Ports.LEFT_MOTOR)
# right_motor = Motor(Ports.RIGHT_MOTOR)

""" Initialize controller input (VEX specific) """ 
# Example:
# from vex import Controller, Buttons
# controller = Controller()
# button_a = controller.buttonA
# button_b = controller.buttonB


def set_motor_speed(left_speed, right_speed):
    """Sets the speed of both motors."""
    # Replace with your VEX motor control code. Example:
    # left_motor.spin(FORWARD, left_speed, PERCENT)
    # right_motor.spin(FORWARD, right_speed, PERCENT)
    print(f"Left Motor: {left_speed}, Right Motor: {right_speed}")  # testing

def get_controller_input():
    """Returns a tuple: (A_pressed, B_pressed)."""
    A_pressed = button_a.pressing 
    B_pressed = button_b.pressing
    return A_pressed, B_pressed


# Constants (adjust these)
FORWARD_SPEED = 50  # Percent of motor speed
BACKWARD_SPEED = -50
AUTO_SPEED = 100
STABLE_TIME = 0.1  # Seconds for debouncing

# Main control loop
def control_loop():
    while True:  # Or some other loop condition

        A_pressed, B_pressed = get_controller_input()

        # Debouncing/Double-checking Logic
        stable_a = False
        stable_b = False

        start_time = time.time()  # Import time for time.time()
        while time.time() - start_time < STABLE_TIME:
            current_a, current_b = get_controller_input()
            if current_a == A_pressed:
                stable_a = True
            else:
                stable_a = False

            if current_b == B_pressed:
                stable_b = True
            else:
                stable_b = False

            if not stable_a or not stable_b:
                break  # Buttons changed, restart check

        # Control Logic (using constants)
        if stable_a and stable_b:
            set_motor_speed(AUTO_SPEED, AUTO_SPEED)  # e.g. Auto-run
        elif stable_a and not stable_b:
            set_motor_speed(FORWARD_SPEED, FORWARD_SPEED) # Forward
        elif not stable_a and stable_b:
            set_motor_speed(BACKWARD_SPEED, BACKWARD_SPEED)  # Backward
        else:
            set_motor_speed(0, 0)  # Stop

        # VEX Specific: Add a small delay (important for VEX)
        vex.sleep(20) # 20 milliseconds is usually good

#============================================================
# Import necessary modules 
from vex import *  
import time  # For time.time()
vex = vex() # Initialize vex library

# Start the control loop
control_loop()