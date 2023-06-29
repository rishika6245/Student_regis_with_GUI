import tkinter as tk

# Create a new window
window = tk.Tk()

# Set the title of the window
window.title("My GUI")

# Create a label widget
label = tk.Label(window, text="Hello, World!", font=("Arial", 16))

# Pack the label widget onto the window
label.pack()

# Run the main event loop
window.mainloop()