

# PYTHON SPEED TEST

This Python program is a simple GUI (Graphical User Interface) application that allows users to test their internet speed. The program uses the Speedtest module to measure download speed, upload speed, and ping (latency) time.

## Installation

### Requirements

- Python 3.x
- tkinter module (comes with Python)
- speedtest-cli module

### Installing Modules

To install the speedtest-cli module, run the following command:

```bash
pip install speedtest-cli
```

## Usage

To run the program, execute the following command in your terminal:

```bash
python main.py
```

## Purpose of the Program

This program allows you to measure your internet connection speed. It can test download speed, upload speed, and ping times separately and display the results to the user via a message box.

## How the Program Works

The program uses the tkinter module to create a graphical user interface. The user selects the type of speed test they want to perform (download speed, upload speed, or ping). The selected option is tested using the Speedtest module, and the results are displayed to the user in a message box.

## Methods and Functions

### `downloadSpeed()`

This function is called when the user wants to test the download speed. It sets the global variable `option` to 'Download Speed' and calls the `showSpeed()` function.

### `uploadSpeed()`

This function is called when the user wants to test the upload speed. It sets the global variable `option` to 'Upload Speed' and calls the `showSpeed()` function.

### `ping()`

This function is called when the user wants to test the ping time. It sets the global variable `option` to 'Ping/ms Latency' and calls the `showSpeed()` function.

### `showSpeed()`

This function measures the speed according to the selected test type and displays the result to the user. It uses the Speedtest module to measure download speed, upload speed, or ping time, and displays the result in appropriate units to the user via a message box.

## User Interface

### Main Window

The main window is created using tkinter and includes the following components:

- Title label: 'Speed Test'
- Instruction label: 'SELECT THE OPTION YOU WANT TO TEST'
- Download speed test button: 'Check Download Speed'
- Upload speed test button: 'Check Upload Speed'
- Ping test button: 'Check Ping ms'

Each button calls the corresponding speed test function.


