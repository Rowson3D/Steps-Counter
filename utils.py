import tkinter as tk
from tkinter import messagebox

def show_error(message):
    """Displays an error message box."""
    messagebox.showerror("Error", message)


def show_info(message):
    """Displays an informational message box."""
    messagebox.showinfo("Info", message)