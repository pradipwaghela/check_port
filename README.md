# Port Checker

Port Checker is a simple GUI-based tool written in Python that helps you verify whether a specific port is in use on a given IP address or hostname. It features a user-friendly interface and provides feedback directly in the application.

## Features

* Verify port status for a specific IP address or hostname
* User-friendly GUI interface
* Inline result display
* Help and About menu sections
* Portable with standalone executable capability

## Requirements

* Python 3.6 or later
* Libraries:
   * `tkinter` (pre-installed with Python)
   * `socket`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/port-checker.git
```

2. Navigate to project directory:
```bash
cd port-checker
```

3. (Optional) Create virtual environment:
```bash
python -m venv env
source env/bin/activate # On Windows: env\Scripts\activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Script

Run directly with Python:
```bash
python check_port_gui.py
```

### Building an Executable

1. Install PyInstaller:
```bash
pip install pyinstaller
```

2. Generate executable:
```bash
pyinstaller --onefile --noconsole check_port_gui.py
```

3. Executable will be in the `dist` directory.

## GUI Instructions

1. Enter IP address or hostname
2. Enter port number
3. Click **Check Port**
4. View results inline

## Help and About

* **Help**: Access usage instructions from GUI menu
* **About**: View author and version information

## Contributing

Contributions welcome! Fork the repository and submit pull requests.

## License

MIT License. See LICENSE file for details.

## Author

**Pradip Waghela**  
Email: pradip.waghela787@gmail.com  
© 2024 

## Feedback and Support

Report issues or suggestions via repository issues or contact the author.