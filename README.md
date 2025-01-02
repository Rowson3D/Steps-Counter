# Image Step Calculator

This Python-based GUI application calculates the optimal steps for training a machine learning model using a folder of images.

## How it works

The script takes a folder as input, iterates through all images recursively, and calculates two factors (repeats and epochs) based on the number of images and a user-provided batch size.

## Files

*   `main.py`: The entry point for the application.
*   `image_counter.py`: Contains the image counting logic.
*   `step_calculator.py`: Contains the core step calculation logic.
*   `gui_utils.py`: Handles GUI elements and layout.
*   `run.bat`: A batch script for running on Windows.
*   `run.sh`: A bash script for running on Unix-like systems (macOS, Linux).
*   `requirements.txt`: Lists Python package dependencies.
*   `README.md`: This file.

## Prerequisites

*   Python 3.6 or higher.
*   Pillow (`PIL`) library for image processing.

## Installation and Setup

1.  Clone or download this repository.
2.  Navigate to the project directory.
3.  Install dependencies using `pip`:
    ```
    pip install -r requirements.txt
    ```
4.  Run the application:
    *   **Windows:** Double-click `run.bat`, or run it via command prompt.
    *   **Unix-like:** `chmod +x run.sh && ./run.sh`.

## Usage

1.  Run the application as indicated above
2.  Click the "Select Folder" button and choose the folder containing your images.
3.  A dialog box will prompt you to enter the batch size.
4.  The application will then calculate and display the appropriate 'repeats', 'epochs', and 'total_steps' in the GUI window.

## Developer Notes

*   The code is structured in a modular way for easy understanding and maintenance.
*   Error handling is implemented to provide a better user experience.
*   The program prompts for a batch size via dialog box
*  The batch size is validated in the dialog, preventing the program from crashing.
*  A message box is shown if no images are found in the given directory.

## To Do

*   Add progress updates when scanning the image folder.
*   Consider adding logging.
*   Make it so the results are copied to clipboard