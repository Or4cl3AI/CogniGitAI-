import tkinter as tk
from tkinter import messagebox

def main():
    # Create the main window
    root = tk.Tk()

    # Hide the main window (you can remove this line if you want to see the main window)
    root.withdraw()

    # Show a message box dialog
    messagebox.showinfo("Greetings", "Hello, welcome to the dialog system!")

    # Close the main window
    root.destroy()

if __name__ == "__main__":
    main()
