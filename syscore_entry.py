#!/usr/bin/env python3
"""
System Monitoring Tool
Created by Anubhav Mohandas
Collects detailed information about system state and stores it in a file.
"""

import os
import sys
import platform
import datetime
import subprocess
import socket
import json
import time
try:
    import psutil
    from tabulate import tabulate
    from colorama import Fore, Back, Style, init
except ImportError:
    print("Missing required packages. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil", "tabulate", "colorama"])
    import psutil
    from tabulate import tabulate
    from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

class SystemMonitor:
    def __init__(self, output_file="system_health_report.json"):
        self.output_file = output_file
        self.system_info = {}
        self.collection_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    

    def display_banner(self):
        """Display a colorful banner for the tool"""
        banner = f"""
{Fore.CYAN}╔════════════════════════════════════════════════════════════════════════════════════╗
{Fore.CYAN}║ {Fore.YELLOW}███████╗██╗   ██╗███████╗ ██████╗ ██████╗ ██████╗ ███████╗                  {Fore.CYAN}║
{Fore.CYAN}║ {Fore.YELLOW}██╔════╝╚██╗ ██╔╝██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝                  {Fore.CYAN}║
{Fore.CYAN}║ {Fore.YELLOW}███████╗ ╚████╔╝ ███████╗██║     ██║   ██║██████╔╝█████╗                    {Fore.CYAN}║
{Fore.CYAN}║ {Fore.YELLOW}╚════██║  ╚██╔╝  ╚════██║██║     ██║   ██║██╔══██╗██╔══╝                    {Fore.CYAN}║
{Fore.CYAN}║ {Fore.YELLOW}███████║   ██║   ███████║╚██████╗╚██████╔╝██║  ██║███████╗                  {Fore.CYAN}║
{Fore.CYAN}║ {Fore.YELLOW}╚══════╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝                  {Fore.CYAN}║
{Fore.CYAN}║                                                                             {Fore.CYAN}║
{Fore.CYAN}║ {Fore.GREEN}███████╗███████╗███╗   ██╗████████╗██████╗ ██╗   ██╗                        {Fore.CYAN}║
{Fore.CYAN}║ {Fore.GREEN}██╔════╝██╔════╝████╗  ██║╚══██╔══╝██╔══██╗╚██╗ ██╔╝                        {Fore.CYAN}║
{Fore.CYAN}║ {Fore.GREEN}███████╗█████╗  ██╔██╗ ██║   ██║   ██████╔╝ ╚████╔╝                         {Fore.CYAN}║
{Fore.CYAN}║ {Fore.GREEN}╚════██║██╔══╝  ██║╚██╗██║   ██║   ██╔══██╗  ╚██╔╝                          {Fore.CYAN}║
{Fore.CYAN}║ {Fore.GREEN}███████║███████╗██║ ╚████║   ██║   ██║  ██║   ██║                           {Fore.CYAN}║
{Fore.CYAN}║ {Fore.GREEN}╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝                           {Fore.CYAN}║
{Fore.CYAN}║                                                                             {Fore.CYAN}║
{Fore.CYAN}║ {Fore.MAGENTA}Advanced System Monitoring & Diagnostics Tool v2.0                          {Fore.CYAN}║
{Fore.CYAN}║ {Fore.WHITE}Created by: {Fore.LIGHTRED_EX}Anubhav Mohandas                                                {Fore.CYAN}║
{Fore.CYAN}╚═══════════════════════════════════════════════════════════════════════════════════╝
    """
        print(banner)
        print(f"{Fore.YELLOW}[*] {Fore.WHITE}System scan initiated at: {Fore.GREEN}{self.collection_time}")
        print(f"{Fore.YELLOW}[*] {Fore.WHITE}Running on: {Fore.GREEN}{platform.system()} {platform.release()}")
        print()
        
    def collect_basic_system_info(self):
        """Collect basic system information"""
        print(f"{Fore.BLUE}[+] {Fore.WHITE}Collecting basic system information...")
        
        self.system_info["basic_info"] = {
            "collection_time": self.collection_time,
            "hostname": socket.gethostname(),
            "platform": platform.system(),
            "platform_release": platform.release(),
            "platform_version": platform.version(),
            "architecture": platform.machine(),
            "processor": platform.processor(),
            "python_version": platform.python_version(),
            "boot_time": datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        }
        
    def collect_memory_info(self):
        """Collect memory usage information"""
        print(f"{Fore.BLUE}[+] {Fore.WHITE}Collecting memory information...")
        
        virtual_memory = psutil.virtual_memory()
        swap_memory = psutil.swap_memory()
        
        self.system_info["memory_info"] = {
            "total_memory": f"{virtual_memory.total / (1024**3):.2f} GB",
            "available_memory": f"{virtual_memory.available / (1024**3):.2f} GB",
            "used_memory": f"{virtual_memory.used / (1024**3):.2f} GB",
            "memory_percent": f"{virtual_memory.percent}%",
            "swap_total": f"{swap_memory.total / (1024**3):.2f} GB",
            "swap_used": f"{swap_memory.used / (1024**3):.2f} GB",
            "swap_percent": f"{swap_memory.percent}%"
        }
        
    def collect_disk_info(self):
        """Collect disk usage information"""
        print(f"{Fore.BLUE}[+] {Fore.WHITE}Collecting disk information...")
        
        partitions = []
        for partition in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                partition_info = {
                    "device": partition.device,
                    "mountpoint": partition.mountpoint,
                    "filesystem_type": partition.fstype,
                    "total_size": f"{usage.total / (1024**3):.2f} GB",
                    "used": f"{usage.used / (1024**3):.2f} GB",
                    "free": f"{usage.free / (1024**3):.2f} GB",
                    "usage_percent": f"{usage.percent}%"
                }
                partitions.append(partition_info)
            except PermissionError:
                continue
        
        self.system_info["disk_info"] = partitions
        
        # IO statistics
        io_counters = psutil.disk_io_counters()
        if io_counters:
            self.system_info["disk_io_info"] = {
                "read_count": io_counters.read_count,
                "write_count": io_counters.write_count,
                "read_bytes": f"{io_counters.read_bytes / (1024**3):.2f} GB",
                "write_bytes": f"{io_counters.write_bytes / (1024**3):.2f} GB"
            }
        
    def collect_network_info(self):
        """Collect network information"""
        print(f"{Fore.BLUE}[+] {Fore.WHITE}Collecting network information...")
        
        # Network interfaces
        interfaces = []
        for interface_name, interface_addresses in psutil.net_if_addrs().items():
            for address in interface_addresses:
                if address.family == socket.AF_INET:
                    interfaces.append({
                        "interface": interface_name,
                        "ip_address": address.address,
                        "netmask": address.netmask,
                        "broadcast": address.broadcast
                    })
        
        # Network connections
        connections = []
        for conn in psutil.net_connections(kind='inet'):
            try:
                connections.append({
                    "proto": "TCP" if conn.type == socket.SOCK_STREAM else "UDP",
                    "local_address": f"{conn.laddr.ip}:{conn.laddr.port}" if hasattr(conn, 'laddr') and conn.laddr else "N/A",
                    "remote_address": f"{conn.raddr.ip}:{conn.raddr.port}" if hasattr(conn, 'raddr') and conn.raddr else "N/A",
                    "status": conn.status if hasattr(conn, 'status') else "N/A",
                    "pid": conn.pid if hasattr(conn, 'pid') and conn.pid else "N/A"
                })
            except (AttributeError, KeyError):
                pass
        
        # Network IO statistics
        io_counters = psutil.net_io_counters()
        network_stats = {
            "bytes_sent": f"{io_counters.bytes_sent / (1024**2):.2f} MB",
            "bytes_recv": f"{io_counters.bytes_recv / (1024**2):.2f} MB",
            "packets_sent": io_counters.packets_sent,
            "packets_recv": io_counters.packets_recv,
            "error_in": io_counters.errin,
            "error_out": io_counters.errout,
            "drop_in": io_counters.dropin,
            "drop_out": io_counters.dropout
        }
        
        self.system_info["network_info"] = {
            "interfaces": interfaces,
            "connections": connections,
            "statistics": network_stats
        }
        
    def collect_process_info(self):
        """Collect information about running processes"""
        print(f"{Fore.BLUE}[+] {Fore.WHITE}Collecting process information...")
        
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'username', 'status', 'cpu_percent', 'memory_percent', 'create_time', 'cmdline']):
            try:
                process_info = proc.info
                process_info['create_time'] = datetime.datetime.fromtimestamp(process_info['create_time']).strftime("%Y-%m-%d %H:%M:%S")
                process_info['cmdline'] = ' '.join(proc.cmdline()) if proc.cmdline() else ""
                processes.append(process_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        
        # Sort by CPU usage (highest first)
        processes = sorted(processes, key=lambda p: p['cpu_percent'], reverse=True)
        self.system_info["process_info"] = processes[:50]  # Limiting to top 50 to keep file size reasonable
        
    def collect_user_info(self):
        """Collect information about logged-in users"""
        print(f"{Fore.BLUE}[+] {Fore.WHITE}Collecting user information...")
        
        users = []
        for user in psutil.users():
            users.append({
                "name": user.name,
                "terminal": user.terminal,
                "host": user.host,
                "started": datetime.datetime.fromtimestamp(user.started).strftime("%Y-%m-%d %H:%M:%S")
            })
        
        self.system_info["user_info"] = users
        
    def collect_application_info(self):
        """Collect information about installed applications"""
        print(f"{Fore.BLUE}[+] {Fore.WHITE}Collecting application information...")
        
        installed_apps = []
        
        # This approach varies by OS
        try:
            if platform.system() == "Windows":
                # For Windows
                import winreg
                key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")
                for i in range(0, winreg.QueryInfoKey(key)[0]):
                    try:
                        subkey_name = winreg.EnumKey(key, i)
                        subkey = winreg.OpenKey(key, subkey_name)
                        try:
                            name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                            version = winreg.QueryValueEx(subkey, "DisplayVersion")[0]
                            installed_apps.append({"name": name, "version": version})
                        except (WindowsError, KeyError):
                            pass
                    except (WindowsError):
                        continue
            
            elif platform.system() == "Linux":
                # For Debian-based Linux
                try:
                    output = subprocess.check_output("dpkg --get-selections", shell=True, text=True)
                    for line in output.splitlines():
                        package = line.split()[0]
                        installed_apps.append({"name": package, "version": "N/A"})
                except subprocess.CalledProcessError:
                    # For Red Hat-based Linux
                    try:
                        output = subprocess.check_output("rpm -qa", shell=True, text=True)
                        for line in output.splitlines():
                            installed_apps.append({"name": line, "version": "N/A"})
                    except subprocess.CalledProcessError:
                        pass
            
            elif platform.system() == "Darwin":  # macOS
                try:
                    output = subprocess.check_output("ls -la /Applications", shell=True, text=True)
                    for line in output.splitlines():
                        if ".app" in line:
                            parts = line.split()
                            if len(parts) > 8:
                                app_name = parts[8].replace(".app", "")
                                installed_apps.append({"name": app_name, "version": "N/A"})
                except subprocess.CalledProcessError:
                    pass
        
        except Exception as e:
            installed_apps.append({"error": f"Unable to fetch application info: {str(e)}"})
        
        self.system_info["application_info"] = installed_apps
    
    def collect_cpu_info(self):
        """Collect detailed CPU information"""
        print(f"{Fore.BLUE}[+] {Fore.WHITE}Collecting CPU information...")
        
        cpu_info = {
            "physical_cores": psutil.cpu_count(logical=False),
            "total_cores": psutil.cpu_count(logical=True),
            "cpu_freq_current": f"{psutil.cpu_freq().current:.2f} MHz" if hasattr(psutil.cpu_freq(), 'current') else "N/A",
            "cpu_freq_min": f"{psutil.cpu_freq().min:.2f} MHz" if hasattr(psutil.cpu_freq(), 'min') else "N/A",
            "cpu_freq_max": f"{psutil.cpu_freq().max:.2f} MHz" if hasattr(psutil.cpu_freq(), 'max') else "N/A",
            "cpu_percent_per_core": [f"{percentage}%" for percentage in psutil.cpu_percent(interval=1, percpu=True)],
            "cpu_percent_overall": f"{psutil.cpu_percent(interval=1)}%"
        }
        
        self.system_info["cpu_info"] = cpu_info
    
    def collect_security_info(self):
        """Collect basic security information"""
        print(f"{Fore.BLUE}[+] {Fore.WHITE}Collecting security information...")
        
        security_info = {}
        
        # Windows-specific security info
        if platform.system() == "Windows":
            try:
                # Check Windows Defender status
                defender_status = subprocess.check_output(
                    "powershell -Command \"Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled\"",
                    shell=True, text=True
                )
                security_info["windows_defender"] = defender_status.strip()
                
                # Check firewall status
                firewall_status = subprocess.check_output(
                    "netsh advfirewall show allprofiles state", 
                    shell=True, text=True
                )
                security_info["windows_firewall"] = firewall_status.strip()
            except:
                security_info["windows_security_check"] = "Failed to retrieve Windows security information"
        
        # Linux-specific security info
        elif platform.system() == "Linux":
            try:
                # Check iptables
                iptables_status = subprocess.check_output(
                    "which iptables && iptables -L | grep -c 'Chain'", 
                    shell=True, text=True
                )
                security_info["firewall_rules"] = f"{iptables_status.strip()} iptables chains found"
            except:
                try:
                    # Try ufw if iptables fails
                    ufw_status = subprocess.check_output(
                        "which ufw && ufw status", 
                        shell=True, text=True
                    )
                    security_info["firewall_status"] = ufw_status.strip()
                except:
                    security_info["linux_firewall_check"] = "No firewall information available"
        
        # Common security checks
        try:
            # List listening ports
            if platform.system() == "Windows":
                netstat_output = subprocess.check_output(
                    "netstat -ano | findstr LISTENING", 
                    shell=True, text=True
                )
            else:
                netstat_output = subprocess.check_output(
                    "netstat -tuln | grep LISTEN", 
                    shell=True, text=True
                )
            
            # Parse and clean up the output
            listening_ports = []
            for line in netstat_output.splitlines():
                listening_ports.append(line.strip())
            
            security_info["listening_ports"] = listening_ports[:20]  # Limit to 20 ports
        except:
            security_info["listening_ports_check"] = "Failed to retrieve listening ports"
        
        self.system_info["security_info"] = security_info
    
    def collect_all_info(self):
        """Collect all system information"""
        self.collect_basic_system_info()
        self.collect_memory_info()
        self.collect_disk_info()
        self.collect_network_info()
        self.collect_process_info()
        self.collect_user_info()
        self.collect_application_info()
        self.collect_cpu_info()
        self.collect_security_info()
        
    def save_to_file(self):
        """Save the collected information to a file"""
        print(f"{Fore.GREEN}[+] {Fore.WHITE}Saving system information to {self.output_file}...")
        with open(self.output_file, 'w') as f:
            json.dump(self.system_info, f, indent=4)
        print(f"{Fore.GREEN}[+] {Fore.WHITE}System information saved to {Fore.YELLOW}{self.output_file}")
    
    def display_summary(self):
        """Display a summary of the collected information"""
        print(f"\n{Fore.CYAN}{'='*30} SYSTEM HEALTH SUMMARY {'='*30}{Fore.RESET}")
        
        # Basic info
        print(f"\n{Fore.YELLOW}--- Basic System Information ---{Fore.RESET}")
        basic_info = self.system_info["basic_info"]
        basic_table = []
        for key, value in basic_info.items():
            basic_table.append([key, value])
        print(tabulate(basic_table, headers=["Property", "Value"], tablefmt="grid"))
        
        # CPU info
        print(f"\n{Fore.YELLOW}--- CPU Information ---{Fore.RESET}")
        cpu_info = self.system_info["cpu_info"]
        cpu_table = []
        for key, value in cpu_info.items():
            if key != "cpu_percent_per_core":
                cpu_table.append([key, value])
        print(tabulate(cpu_table, headers=["Property", "Value"], tablefmt="grid"))
        
        # Memory info
        print(f"\n{Fore.YELLOW}--- Memory Information ---{Fore.RESET}")
        memory_info = self.system_info["memory_info"]
        memory_table = []
        for key, value in memory_info.items():
            memory_table.append([key, value])
        print(tabulate(memory_table, headers=["Property", "Value"], tablefmt="grid"))
        
        # Disk info (first few entries)
        print(f"\n{Fore.YELLOW}--- Disk Information (Top Partitions) ---{Fore.RESET}")
        disk_headers = ["Device", "Mount Point", "Total", "Used", "Free", "Usage %"]
        disk_table = []
        for partition in self.system_info["disk_info"][:3]:  # Show first 3 partitions
            disk_table.append([
                partition["device"],
                partition["mountpoint"],
                partition["total_size"],
                partition["used"],
                partition["free"],
                partition["usage_percent"]
            ])
        print(tabulate(disk_table, headers=disk_headers, tablefmt="grid"))
        
        # Network interfaces
        print(f"\n{Fore.YELLOW}--- Network Interfaces ---{Fore.RESET}")
        if self.system_info["network_info"]["interfaces"]:
            interface_headers = ["Interface", "IP Address", "Netmask", "Broadcast"]
            interface_table = []
            for interface in self.system_info["network_info"]["interfaces"]:
                interface_table.append([
                    interface["interface"],
                    interface["ip_address"],
                    interface["netmask"],
                    interface["broadcast"] if interface["broadcast"] else "N/A"
                ])
            print(tabulate(interface_table, headers=interface_headers, tablefmt="grid"))
        else:
            print("No network interfaces found")
        
        # Top processes
        print(f"\n{Fore.YELLOW}--- Top Processes (by CPU usage) ---{Fore.RESET}")
        process_headers = ["PID", "Name", "User", "Status", "CPU %", "Mem %"]
        process_table = []
        for proc in self.system_info["process_info"][:5]:  # Show top 5 processes
            process_table.append([
                proc["pid"],
                proc["name"],
                proc["username"],
                proc["status"],
                f"{proc['cpu_percent']:.1f}%",
                f"{proc['memory_percent']:.1f}%"
            ])
        print(tabulate(process_table, headers=process_headers, tablefmt="grid"))
        
        # Logged-in users
        print(f"\n{Fore.YELLOW}--- Logged-in Users ---{Fore.RESET}")
        if self.system_info["user_info"]:
            user_headers = ["Username", "Terminal", "Host", "Login Time"]
            user_table = []
            for user in self.system_info["user_info"]:
                user_table.append([
                    user["name"],
                    user["terminal"],
                    user["host"],
                    user["started"]
                ])
            print(tabulate(user_table, headers=user_headers, tablefmt="grid"))
        else:
            print("No users currently logged in")
            
        print(f"\n{Fore.GREEN}Full report saved to: {Fore.YELLOW}{self.output_file}{Fore.RESET}")

def run_interactive_mode():
    """Run the system monitor in interactive mode"""
    monitor = SystemMonitor()
    monitor.display_banner()
    
    print(f"{Fore.CYAN}Select information to collect:")
    print(f"{Fore.YELLOW}[1] {Fore.WHITE}All system information (comprehensive scan)")
    print(f"{Fore.YELLOW}[2] {Fore.WHITE}Basic system information only")
    print(f"{Fore.YELLOW}[3] {Fore.WHITE}Memory and CPU information")
    print(f"{Fore.YELLOW}[4] {Fore.WHITE}Disk information")
    print(f"{Fore.YELLOW}[5] {Fore.WHITE}Network information")
    print(f"{Fore.YELLOW}[6] {Fore.WHITE}Process information")
    print(f"{Fore.YELLOW}[7] {Fore.WHITE}User and application information")
    print(f"{Fore.YELLOW}[8] {Fore.WHITE}Security information")
    print(f"{Fore.YELLOW}[0] {Fore.WHITE}Exit")
    
    choice = input(f"\n{Fore.GREEN}Enter your choice (1-8): {Fore.RESET}")
    
    if choice == "0":
        print(f"{Fore.RED}Exiting system monitor...")
        sys.exit(0)
    elif choice == "1":
        monitor.collect_all_info()
    elif choice == "2":
        monitor.collect_basic_system_info()
    elif choice == "3":
        monitor.collect_basic_system_info()
        monitor.collect_memory_info()
        monitor.collect_cpu_info()
    elif choice == "4":
        monitor.collect_basic_system_info()
        monitor.collect_disk_info()
    elif choice == "5":
        monitor.collect_basic_system_info()
        monitor.collect_network_info()
    elif choice == "6":
        monitor.collect_basic_system_info()
        monitor.collect_process_info()
    elif choice == "7":
        monitor.collect_basic_system_info()
        monitor.collect_user_info()
        monitor.collect_application_info()
    elif choice == "8":
        monitor.collect_basic_system_info()
        monitor.collect_security_info()
    else:
        print(f"{Fore.RED}Invalid choice. Collecting all information by default.")
        monitor.collect_all_info()
    
    # Display summary
    monitor.display_summary()
    
    # Ask if user wants to save to file
    save_choice = input(f"\n{Fore.GREEN}Save full report to file? (y/n): {Fore.RESET}").lower()
    if save_choice == 'y' or save_choice == 'yes':
        filename = input(f"{Fore.GREEN}Enter filename (default: system_health_report.json): {Fore.RESET}")
        if filename:
            monitor.output_file = filename
        monitor.save_to_file()
    else:
        print(f"{Fore.YELLOW}Report not saved to file.")
    
    print(f"\n{Fore.CYAN}Thank you for using SysCore Sentry!{Fore.RESET}")
        
def main():
    """Main function to run the system monitor"""
    try:
        run_interactive_mode()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Monitoring cancelled by user{Fore.RESET}")
        sys.exit(1)
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Fore.RESET}")
        sys.exit(1)
    
if __name__ == "__main__":
    main()