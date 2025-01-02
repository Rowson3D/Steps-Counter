# Image Step Calculator

This Python-based GUI application calculates the optimal steps for training a machine learning model using a folder of images. It adheres to specific step calculation guidelines and provides various settings.

## How it works

The script takes a folder as input, recursively counts all images, and calculates the 'repeats' and 'epochs' values based on the number of images and user-provided batch size, targeting an optimal number of steps for training.

**Calculation Rules:**
*   The script attempts to find a "repeats" factor such that `number_of_images * repeats` is between 900 and 1000 (configurable in the `config.json` file).
*   The script then attempts to find an "epochs" factor such that `(number_of_images * repeats / batch_size) * epochs` is between 2500 and 4000 (also configurable in the `config.json` file).

## Features

*   **Folder Selection:** Choose a directory of images, recursively scans all subdirectories.
*   **Batch Size Input:** Specify a batch size via a spinbox.
*   **Step Calculation Modes:** Select between:
    *   **Normal:** First valid result in range.
    *   **Strict:** Factor 1 (repeats) matches the minimum range value exactly.
    *   **Prioritize Epochs:** Prioritizes the largest possible epoch value.
    *   **Prioritize Repeats:**  Prioritizes the smallest possible epoch value.
*   **Dynamic UI:** Provides informative labels and clear buttons for a user friendly experience.
*  **Status messages**: Provides feedback in the application, so the user is informed.
*  **Clipboard**: Copies the suggested folder name to the clipboard for easy pasting.
*  **Remembers Last Used Path**: Remembers the last used path for when you re-open the application.
*   **Suggestion Saving:** Saves all the current settings and recommendations to a text file in the "suggestions" folder. The file is named after the 'repeats' value and folder name. This file will be created/overwritten whenever an action occurs (selection of a folder with valid images, a change in the batch size, or a change in the step mode).

## Files

*   `main.py`: The entry point for the application.
*   `image_counter.py`: Contains the image counting logic.
*   `step_calculator.py`: Contains the core step calculation logic.
*   `gui_utils.py`: Handles GUI elements and layout.
*    `utils.py`: Contains reusable helper functions.
*   `config.py`: Manages the application's configuration.
*   `run.bat`: A batch script for running on Windows.
*   `run.sh`: A bash script for running on Unix-like systems (macOS, Linux).
*   `requirements.txt`: Lists Python package dependencies.
*   `README.md`: This file.
*   `config.json`: The configuration file that saves user settings (will automatically be created if it does not exist).
*   `suggestions/`: A folder where the program will save all of the configurations from each dataset that the user tries to generate.

## Prerequisites

*   Python 3.6 or higher.
*   Pillow (`PIL`) library for image processing.
*   `pyperclip` module for clipboard functionality.

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

1.  Run the application as indicated above.
2.  Click the "Select Image Folder" button and choose the folder containing your images.
3.  A "Step Mode" can be selected, where "Normal" finds the first valid result, "Strict" matches exactly, and "Prioritize Epochs" tries to find the largest possible epoch, while "Prioritize Repeats" does the opposite.
4.  Enter a batch size using the spinbox provided.
5.  The application will calculate and display the 'repeats', 'epochs', and 'total_steps'.
6.  The 'repeats' and the current folder name will be copied to clipboard for easy pasting.
7.  All the current settings will be saved to a text file with the name being the repeats and folder name, inside the "suggestions" folder. This file is overwritten every time a new folder is selected, the batch size is changed, or the step mode is changed.

## Configuration

The application uses a `config.json` file to store user settings, which is located in the same directory as the application. You can customize the following settings:

*   `last_folder`: The last directory used. This will not load when you start the application, but will be saved for the next time you use it.
*   `min_repeats_range`: The minimum value for the first step calculation range.
*   `max_repeats_range`: The maximum value for the first step calculation range.
*   `min_total_steps_range`: The minimum value for the second step calculation range.
*   `max_total_steps_range`: The maximum value for the second step calculation range.
*   `default_batch_size`: The default batch size value.

## Developer Notes

*   The code is structured in a modular way for easy understanding and maintenance.
*   Error handling is implemented to provide a better user experience.
*   The program uses a spinbox for batch size input.
*   The batch size is validated when the user unfocuses, preventing the program from crashing.
*   A message box is shown if no images are found in the given directory.
*   A message box is shown if no suitable results are found using the given parameters.
*   The repeats folder name is copied to clipboard for easy pasting.
* The settings for a dataset (images found, repeats, epochs, total steps, batch size, and step mode) will automatically be written to a file in the "suggestions" folder.

## To Do

*   Add progress updates when scanning the image folder.
*   Consider adding logging.
*   Add more advanced features for dataset handling.