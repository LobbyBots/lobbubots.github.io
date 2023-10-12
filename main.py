import tkinter as tk

# Create a function to change the color of the window
def change_color(color):
    window.configure(bg=color)

# Create the main window
window = tk.Tk()
window.title("LED Color Changer")

# Create buttons to change the color
red_button = tk.Button(window, text="Red", command=lambda: change_color("red"))
green_button = tk.Button(window, text="Green", command=lambda: change_color("green"))
blue_button = tk.Button(window, text="Blue", command=lambda: change_color("blue"))

# Pack the buttons
red_button.pack()
green_button.pack()
blue_button.pack()

# Start the Tkinter event loop
window.mainloop()