# Python Scripts for Easy Log Analysis

This repository provides Python scripts for efficiently extracting information from log files, such as IP addresses, email addresses, and port numbers. Each script reads from a specified log file and uses regular expressions to identify relevant data, optimizing for both accuracy and performance.

## Table of Contents
- [IP Address Extraction](#ip-address-extraction)
- [Email Address Extraction](#email-address-extraction)
- [Port Number Extraction](#port-number-extraction)
- [Usage](#usage)
- [License](#license)

---

### IP Address Extraction

Extracts unique IP addresses from a log file. The script reads the file line by line for memory efficiency and outputs a list of unique IPs.

### Email Address Extraction

Extracts unique email addresses from a log file using regex patterns that cover common email formats, ensuring only unique addresses are returned.

### Port Number Extraction

Extracts valid, unique port numbers from a log file, validating that the ports are within the standard range (0 to 65535).

---

### Usage

1. Place your log file in the same directory as the script or specify the full path.
2. Run the respective script by providing the log file path.
3. The output will display the extracted data, such as unique IP addresses, email addresses, or port numbers.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
