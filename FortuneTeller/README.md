# Fortune Teller Bot

A delightful Windows application that provides daily fortunes and positive messages to brighten your day. The Fortune Teller Bot can be set to run at startup, ensuring you receive a new fortune each time you log into your computer.

## Features

- Displays random positive fortunes and messages
- Clean, simple popup interface
- Option to install/uninstall from Windows startup
- Version tracking and build date display
- Easy to use and maintain

## Installation

### Method 1: Using the Installer
1. Download the latest release from the releases section
2. Run the installer and follow the on-screen instructions

### Method 2: Manual Installation
1. Clone or download this repository
2. Run the following command to install required dependencies:
   ```
   pip install pywin32
   ```
3. Run the program:
   ```
   python fortune_teller.py
   ```

## Usage

### Running the Program
Simply double-click the executable or run the Python script to receive your fortune:
```
python fortune_teller.py
```

### Installing to Startup
To make the Fortune Teller run automatically when you start your computer:
```
python fortune_teller.py --install
```

### Removing from Startup
To stop the Fortune Teller from running at startup:
```
python fortune_teller.py --uninstall
```

## Building from Source

1. Ensure you have Python 3.x installed
2. Install required dependencies:
   ```
   pip install pywin32
   ```
3. Run the build script:
   ```
   build_fortune_bot.bat
   ```

## Requirements

- Windows operating system
- Python 3.x (for development)
- pywin32 package

## Version History

- Version 1.0: Initial release
  - Basic fortune telling functionality
  - Startup installation capability
  - Simple GUI interface

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues and enhancement requests! 