import RPi.GPIO as GPIO
import tkinter as tk

# Configure the GPIO using Broadcom (BCM) numbering scheme
GPIO.setmode(GPIO.BCM)

# Pin numbers associated with LEDs
LED_PINS = {'red': 17, 'green': 27, 'yellow': 22}

# Set all LEDs are initially off
for led_pin in LED_PINS.values():
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.output(led_pin, GPIO.LOW)

# Function to control which LED should be turned on
def activate_led(led_color):
    # First, turn off all the LEDs
    for led_pin in LED_PINS.values():
        GPIO.output(led_pin, GPIO.LOW)
    # then, turn on the specified LED
    GPIO.output(LED_PINS[led_color], GPIO.HIGH)

# Close the GUI window
def shutdown():
    GPIO.cleanup()  # Clean up GPIO settings
    root.destroy()  # Close the Tkinter window

# Create the main Tkinter window
root = tk.Tk()
root.title("LED Controller")

# Track which LED is currently selected
active_led = tk.StringVar(value='red')

# Create radio buttons for LED color choices
tk.Radiobutton(root, text="Red LED", variable=active_led, value='red', command=lambda: activate_led('red')).pack(anchor=tk.W)
tk.Radiobutton(root, text="Green LED", variable=active_led, value='green', command=lambda: activate_led('green')).pack(anchor=tk.W)
tk.Radiobutton(root, text="Yellow LED", variable=active_led, value='yellow', command=lambda: activate_led('yellow')).pack(anchor=tk.W)

# Add button to exit the program 
tk.Button(root, text="Exit", command=shutdown).pack()

# Start the Tkinter event loop
root.mainloop()
