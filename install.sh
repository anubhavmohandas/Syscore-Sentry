#!/bin/bash

# Colors for terminal output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${CYAN}
╔══════════════════════════════════════════════════════════════════════════╗
║  ███████╗██╗   ██╗███████╗ ██████╗ ██████╗ ██████╗ ███████╗             ║
║  ██╔════╝╚██╗ ██╔╝██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝             ║
║  ███████╗ ╚████╔╝ ███████╗██║     ██║   ██║██████╔╝█████╗               ║
║  ╚════██║  ╚██╔╝  ╚════██║██║     ██║   ██║██╔═══╝ ██╔══╝               ║
║  ███████║   ██║   ███████║╚██████╗╚██████╔╝██║     ███████╗             ║
║  ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚══════╝             ║
║                                                                          ║
║   ███████╗███████╗███╗   ██╗████████╗██████╗ ██╗   ██╗                  ║
║   ██╔════╝██╔════╝████╗  ██║╚══██╔══╝██╔══██╗╚██╗ ██╔╝                  ║
║   ███████╗█████╗  ██╔██╗ ██║   ██║   ██████╔╝ ╚████╔╝                   ║
║   ╚════██║██╔══╝  ██║╚██╗██║   ██║   ██╔══██╗  ╚██╔╝                    ║
║   ███████║███████╗██║ ╚████║   ██║   ██║  ██║   ██║                     ║
║   ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝                     ║
║                                                                          ║
║  Installation Script                                                     ║
╚══════════════════════════════════════════════════════════════════════════╝
${NC}"

echo -e "${YELLOW}[*] Starting SysCore Sentry installation...${NC}"

# Check if Python 3 is installed
echo -e "${YELLOW}[*] Checking for Python 3...${NC}"
if command -v python3 &>/dev/null; then
    echo -e "${GREEN}[✓] Python 3 is installed${NC}"
else
    echo -e "${YELLOW}[!] Python 3 is not installed. Installing...${NC}"
    if command -v apt-get &>/dev/null; then
        sudo apt-get update
        sudo apt-get install -y python3 python3-pip
    elif command -v yum &>/dev/null; then
        sudo yum install -y python3 python3-pip
    elif command -v brew &>/dev/null; then
        brew install python3
    else
        echo -e "${YELLOW}[!] Could not install Python 3. Please install it manually.${NC}"
        exit 1
    fi
fi

# Install required packages
echo -e "${YELLOW}[*] Installing required Python packages...${NC}"
python3 -m pip install psutil tabulate colorama

# Make the Python script executable
echo -e "${YELLOW}[*] Making script executable...${NC}"
chmod +x system_monitor.py

# Create a symlink for easier access
echo -e "${YELLOW}[*] Creating symlink for easy access...${NC}"
if [ -d "/usr/local/bin" ]; then
    sudo ln -sf "$(pwd)/system_monitor.py" /usr/local/bin/syscore-sentry
    echo -e "${GREEN}[✓] Created symlink: syscore-sentry${NC}"
else
    echo -e "${YELLOW}[!] Could not create symlink${NC}"
fi

# Generate README.md
echo -e "${YELLOW}[*] Generating README.md file...${NC}"
cat > README.md << 'EOF'
# 🖥️ SysCore Sentry - Advanced System Monitoring Tool 🔍

![SysCore Sentry Banner](https://img.shields.io/badge/SysCore-Sentry-blue?style=for-the-badge&logo=computer)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

## 📋 Overview

SysCore Sentry is an advanced system monitoring and diagnostics tool that provides comprehensive insights into your system's health and performance. It collects and displays detailed information about various components of your system, making it easier to identify potential issues and bottlenecks.

![SysCore Sentry Demo](https://i.imgur.com/placeholder.png)

## ✨ Key Features

- 🧠 **Comprehensive System Analysis**: Collects detailed information about CPU, memory, disk, and network usage
- 🔒 **Security Monitoring**: Basic security checks and port monitoring
- 💻 **Process Tracking**: Identifies resource-intensive processes
- 🌐 **Network Activity**: Monitors network interfaces and connections
- 📊 **Visual Reporting**: Presents information in well-formatted tables for easy reading
- 💾 **Report Generation**: Saves detailed reports in JSON format for further analysis
- 🎨 **User-Friendly Interface**: Colorful interactive command-line interface

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

## 📜 Requirements

- Python 3.6 or higher
- psutil
- tabulate
- colorama

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Created with ❤️ by [Anubhav Mohandas](https://github.com/anubhavmohandas)
EOF

echo -e "${GREEN}[✓] README.md generated successfully${NC}"
echo -e "${GREEN}[✓] All done! SysCore Sentry is now installed.${NC}"
echo -e "${CYAN}To run the tool, use: ./system_monitor.py or syscore-sentry${NC}"