# Vulnerability Scanner

## Overview
The Vulnerability Scanner is a Python-based tool that leverages Nmap to scan websites and detect potential vulnerabilities such as SQL injection and XSS (Cross-Site Scripting). This tool also includes a Tkinter-based GUI for easy user interaction.

## Features
- **SQL Injection Detection**: Identifies potential SQL injection points in URLs.
- **XSS Detection**: Detects cross-site scripting vulnerabilities.
- **Port Scanning**: Uses Nmap to scan and list open ports on the target server.
- **Graphical User Interface (GUI)**: Easy-to-use interface for running scans and viewing results.

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `nmap` library
- `tkinter` library

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/vulnerability-scanner.git
    ```

2. Navigate to the project directory:
    ```bash
    cd vulnerability-scanner
    ```

3. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the `app.py` script to start the GUI:
    ```bash
    python app.py
    ```

2. Enter the URL or IP address you want to scan in the input field and click on "Start Scan".

3. The results will be displayed in a new window showing the detected vulnerabilities and open ports.

## Project Structure
- `app.py`: Main script containing the GUI and scanning logic.
- `README.md`: Project documentation.
- `requirements.txt`: List of required Python libraries.

## Contributing
Contributions are welcome! Please fork this repository and submit pull requests for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements
- [Nmap](https://nmap.org/) for the powerful network scanning tool.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI framework.
- The Python community for developing and maintaining useful libraries.

