import tkinter as tk
from tkinter import filedialog
from image_counter import count_images_recursively
from step_calculator import calculate_steps
from gui_utils import create_main_window, update_results, copy_to_clipboard, update_status, update_description
from tkinter import ttk
import os
from utils import show_error, show_info
from config import load_config, save_config
import time


def select_folder():
    """Handle folder selection and processing."""
    folder_path = filedialog.askdirectory(title="Select Image Folder")
    if folder_path:
        update_status("Counting images...")
        try:
            num_images = count_images_recursively(folder_path)
            if num_images == 0:
                 show_info("No images were found in selected path.")
                 update_status("")
                 return
            process_results(num_images, folder_path)
            update_status(f"Folder scanned, images found: {num_images}")
        except Exception as e:
             show_error(f"An error occurred: {e}")
             update_status("") #clear message
        finally:
            config = load_config() #load config
            config["last_folder"] = folder_path #set last folder
            save_config(config) # save the config.

def process_results(num_images, folder_path):
    """Process the folder and update GUI"""
    update_status("Calculating results...")
    try:
        batch_size = batch_size_spinbox.get() # get value from spinbox
        if not batch_size.isdigit(): #Ensure valid digit.
            show_error("Batch size must be a positive integer.")
            return
        batch_size = int(batch_size) #convert to integer

        if batch_size <= 0:
            show_error("Batch size must be a positive integer.")
            return
        config = load_config()  #Load config to get ranges
        min_range = config["min_repeats_range"]
        max_range = config["max_repeats_range"]
        min_steps_range = config["min_total_steps_range"]
        max_steps_range = config["max_total_steps_range"]
        step_mode = step_mode_combo.get()
        results = calculate_steps(num_images, batch_size, min_range, max_range, min_steps_range, max_steps_range, step_mode)

        if results:
             update_results(results, num_images, folder_path)
             copy_to_clipboard(results["repeats"], folder_path)
             update_status("Results calculated!")
        else:
            show_error("No suitable results found, try a different batch size or another dataset.")
            update_status("") #clear message
    except ValueError as e:
        show_error(f"Invalid input value: {e}")
        update_status("")  # clear message
    except Exception as e:
        show_error(f"An error occurred: {e}")
        update_status("")  # clear message


def mode_changed(event):
    update_description(step_mode_combo.get(), description_label) #added call to function to update description.

if __name__ == "__main__":
    root, select_folder_button, batch_size_spinbox, status_label, step_mode_combo, description_label = create_main_window()  # GUI setup
    select_folder_button.config(command=select_folder)  # Connect Button to command.
    update_description(step_mode_combo.get(), description_label) #Initial call to set default description.
    step_mode_combo.bind("<<ComboboxSelected>>", mode_changed) # Update description on mode changed.
    
    # Placeholder for results - added in gui_utils
    root.mainloop()