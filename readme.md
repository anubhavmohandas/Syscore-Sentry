# 🖥️ SysCore Sentry - Advanced System Monitoring Tool 🔍

![SysCore Sentry Banner](https://img.shields.io/badge/SysCore-Sentry-blue?style=for-the-badge&logo=computer)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

## 📋 Overview

SysCore Sentry is an advanced system monitoring and diagnostics tool that provides comprehensive insights into your system's health and performance. It collects and displays detailed information about various components of your system, making it easier to identify potential issues and bottlenecks.

## ✨ Key Features

- 🧠 **Comprehensive System Analysis**: Collects detailed information about CPU, memory, disk, and network usage
- 🔒 **Security Monitoring**: Basic security checks and port monitoring
- 💻 **Process Tracking**: Identifies resource-intensive processes
- 🌐 **Network Activity**: Monitors network interfaces and connections
- 📊 **Visual Reporting**: Presents information in well-formatted tables for easy reading
- 💾 **Report Generation**: Saves detailed reports in JSON format for further analysis
- 🎨 **User-Friendly Interface**: Colorful interactive command-line interface

<!-- ## 🖼️ Screenshots -->


## 🚀 Installation

Use the provided installation script to set up SysCore Sentry:

```bash
chmod +x install.sh
./install.sh
```

Or install manually:

```bash
# Install required Python packages
pip install psutil tabulate colorama

# Make the script executable
chmod +x system_monitor.py
```

## 📖 Usage

Run the tool in interactive mode:

```bash
./system_monitor.py
```

Or use the symlink if created during installation:

```bash
syscore-sentry
```

Follow the on-screen menu to select the information you want to collect:

1. All system information (comprehensive scan)
2. Basic system information only
3. Memory and CPU information
4. Disk information
5. Network information
6. Process information
7. User and application information
8. Security information
0. Exit

## 📊 Sample Output

```
╔══════════════════════ SYSTEM HEALTH SUMMARY ══════════════════════╗

--- Basic System Information ---
+------------------+-------------------------+
| Property         | Value                   |
+==================+=========================+
| collection_time  | 2025-03-06 10:15:30    |
| hostname         | user-desktop           |
| platform         | Linux                   |
| platform_release | 5.4.0-104-generic      |
| architecture     | x86_64                  |
+------------------+-------------------------+

--- CPU Information ---
+---------------------+-------------+
| Property            | Value       |
+=====================+=============+
| physical_cores      | 4           |
| total_cores         | 8           |
| cpu_freq_current    | 2500.00 MHz |
| cpu_percent_overall | 15.2%       |
+---------------------+-------------+
```

## 💡 How It Works

SysCore Sentry uses Python's `psutil` library to gather system information without requiring root privileges in most cases. It presents the information in an easy-to-understand format using colorful tables and provides options to save comprehensive reports for later analysis.

## 🛠️ Advanced Usage

You can use SysCore Sentry for:

- 🔍 **System Troubleshooting**: Identify resource-intensive processes and performance bottlenecks
- 📈 **Performance Monitoring**: Track system resource usage over time
- 🔒 **Security Checks**: View listening ports and basic security information
- 📊 **System Inventory**: Collect detailed information about hardware and installed applications

## 📜 Requirements

- Python 3.6 or higher
- psutil
- tabulate
- colorama

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Created with ❤️ by [Anubhav Mohandas](https://github.com/anubhavmohandas)

---

⭐ If you find this tool useful, please consider giving it a star on GitHub! ⭐