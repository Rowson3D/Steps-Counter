import tkinter as tk
import pyperclip
from tkinter import ttk
import os
from PIL import Image, ImageTk
from config import load_config

def create_main_window():
    """Sets up the main GUI window with a better layout."""
    root = tk.Tk()
    root.title("Image Step Calculator")
    root.geometry("500x450")  # Increased to fit combobox
    root.resizable(False, False)  # Disable resizing
    root.configure(bg="#f0f2f5")  # Background color

    # Styling
    font_style = ("Arial", 13)
    label_font = ("Arial", 14, "bold")

    # Apply MUI-like styling to ttk components
    style = ttk.Style()

    # Configure the main window
    root.configure(bg="#f0f2f5")  # Light gray background

    # Configure the frame
    style.configure("TFrame", background="#f0f2f5")

    # Configure Buttons
    style.configure("TButton",
                     background="#2196f3", foreground="white", font=font_style, padding=8, borderwidth=0, relief="flat")
    style.map("TButton",
              background=[("active", "#1976d2"), ("pressed", "#1565c0")],
              foreground=[("active", "white")])

    # Configure Button for specific color.
    style.configure("BlackButton.TButton", foreground="black")  # Specific styling for the button.

    # Configure Labels
    style.configure("TLabel", background="#f0f2f5", font=font_style, padding=5)
    style.configure("TLabel", anchor="center", background="#f0f2f5")
    style.configure("TEntry", font=font_style, padding=5)
    style.configure("TSpinbox", font=font_style, padding=5)

    # Configure the main frame
    main_frame = ttk.Frame(root, padding=20, style="TFrame")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Program Title Label
    title_label = ttk.Label(main_frame, text="Image Step Calculator", font=("Arial", 16, "bold"), style="TLabel")
    title_label.grid(row=0, column=0, columnspan=3, pady=(0,20), sticky="ew")

    # Results Label - for showing results of the calculation
    global results_label
    results_label = ttk.Label(main_frame,
                            text="Images Found:\nRepeats:\nEpochs:\nTotal Steps:\n\nRecommended Folder Name:",
                            wraplength=450, style="TLabel")
    results_label.grid(row=1, column=0, columnspan=3, sticky="ew", padx=20, pady=(0,20))

    # Status label
    global status_label
    status_label = ttk.Label(main_frame, text="", style="TLabel")
    status_label.grid(row=2, column=0, columnspan=3, sticky="ew", padx=20, pady=(0,10))

    # Step Mode Label and Combobox
    mode_label = ttk.Label(main_frame, text="Step Mode:", style="TLabel")
    mode_label.grid(row=3, column=0, sticky="e", padx=(0, 5), pady=(0, 10))

    global step_mode_combo
    step_mode_combo = ttk.Combobox(main_frame, values=["Normal", "Strict", "Prioritize Epochs", "Prioritize Repeats"], state="readonly", font=font_style)
    step_mode_combo.set("Normal")  # Default value.
    step_mode_combo.grid(row=3, column=1, sticky="w", pady=(0, 10))
    
    # Description Label
    global description_label
    description_label = ttk.Label(main_frame, text="First valid result in range.", wraplength=450, style="TLabel", font=("Arial", 10))
    description_label.grid(row=3, column=0, columnspan=3, sticky="ew", padx=20, pady=(0, 10))

    # Batch Size Label and Input
    batch_size_label = ttk.Label(main_frame, text="Batch Size:", style="TLabel")
    batch_size_label.grid(row=4, column=0, sticky="e", padx=(0, 5), pady=(0,10))

    global batch_size_spinbox
    config = load_config()  # Load config values for spinbox.
    default_batch_size = config.get("default_batch_size", 2)
    batch_size_spinbox = ttk.Spinbox(main_frame, from_=1, to=1000, style="TSpinbox") #set min and max
    batch_size_spinbox.set(str(default_batch_size))
    batch_size_spinbox.grid(row=4, column=1, sticky="w", pady=(0,10))

    # Select Folder Button
    global select_folder_button
    select_folder_button = ttk.Button(main_frame, text="Select Image Folder", style='BlackButton.TButton')
    select_folder_button.grid(row=5, column=0, columnspan=3, sticky="ew", padx=20, pady=(0, 10))


    # Configure the grid for dynamic resizing
    main_frame.grid_rowconfigure(1, weight=1)
    main_frame.grid_columnconfigure(0, weight=1)  # Left column, expands
    main_frame.grid_columnconfigure(1, weight=0)  # Center column, does not expand
    main_frame.grid_columnconfigure(2, weight=1)  # Right column, expands

    return root, select_folder_button, batch_size_spinbox, status_label, step_mode_combo, description_label

def update_results(results, num_images, folder_path):
    """Updates the GUI with the calculated results."""
    folder_name = os.path.basename(folder_path)
    results_label.config(text=(
        f"Images Found: {num_images}\n"
        f"Repeats: {results['repeats']}\n"
        f"Epochs: {results['epochs']}\n"
        f"Total Steps: {results['total_steps']}\n\n"
        f"Recommended Folder Name: {results['repeats']}_{folder_name}"
    ))


def copy_to_clipboard(repeats, folder_path):
    """Copies the repeats and folder name to the clipboard for easy pasting."""
    folder_name = os.path.basename(folder_path)
    try:
        pyperclip.copy(f"{repeats}_{folder_name}")
    except pyperclip.PyperclipException:
        tk.messagebox.showinfo("Info", "Pyperclip could not access the clipboard.")

def update_status(message):
    """Updates the status label with a message."""
    status_label.config(text=message)

def update_description(mode, description_label):
        if mode == "Normal":
            description_label.config(text="First valid result in range.")
        elif mode == "Strict":
            description_label.config(text="Factor 1 matches the minimum range value exactly.")
        elif mode == "Prioritize Epochs":
             description_label.config(text="Prioritizes the largest possible epoch value.")
        elif mode == "Prioritize Repeats":
            description_label.config(text="Prioritizes the smallest possible epoch value.")