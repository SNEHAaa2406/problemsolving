import tkinter as tk

# 1. Initialize the main application window
root = tk.Tk()
root.title("My First GUI")
root.geometry("300x150")  # Width x Height

# 2. Create a text widget (Label)
label = tk.tkinter.Label(root, text="Hello, Pythonista!", font=("Arial", 14))
label.pack(pady=20)  # Add layout spacing

# 3. Create a clickable action widget (Button)
def on_click():
    label.config(text="Button Clicked!")

button = tk.Button(root, text="Click Me", command=on_click)
button.pack()

# 4. Start the application loop (keeps window open)
root.mainloop()
