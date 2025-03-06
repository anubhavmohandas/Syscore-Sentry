import psutil
import os
import platform
import socket
import time

# Function to get network details
def get_network_details():
    network_info = psutil.net_if_addrs()
    network_details = {}
    for interface, addresses in network_info.items():
        for addr in addresses:
            if addr.family == socket.AF_INET:
                network_details[interface] = {
                    "IP Address": addr.address,
                    "Netmask": addr.netmask,
                    "Broadcast": addr.broadcast
                }
    return network_details

# Function to get filesystem details
def get_filesystem_details():
    partitions = psutil.disk_partitions()
    fs_details = {}
    for partition in partitions:
        fs_details[partition.device] = {
            "Mount Point": partition.mountpoint,
            "Filesystem Type": partition.fstype,
            "Total Space": psutil.disk_usage(partition.mountpoint).total,
            "Used Space": psutil.disk_usage(partition.mountpoint).used,
            "Free Space": psutil.disk_usage(partition.mountpoint).free
        }
    return fs_details

# Function to get process details
def get_process_details():
    process_details = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        process_details.append({
            "PID": proc.info['pid'],
            "Name": proc.info['name'],
            "Username": proc.info['username']
        })
    return process_details

# Function to get application details
def get_application_details():
    # List running applications (simple approach)
    app_details = []
    for proc in psutil.process_iter(['pid', 'name']):
        app_details.append({
            "PID": proc.info['pid'],
            "Name": proc.info['name']
        })
    return app_details

# Function to get memory details
def get_memory_details():
    memory_info = psutil.virtual_memory()
    swap_info = psutil.swap_memory()
    memory_details = {
        "Total RAM": memory_info.total,
        "Used RAM": memory_info.used,
        "Free RAM": memory_info.free,
        "Total Swap": swap_info.total,
        "Used Swap": swap_info.used,
        "Free Swap": swap_info.free
    }
    return memory_details

# Function to get user details
def get_user_details():
    users = psutil.users()
    user_details = []
    for user in users:
        user_details.append({
            "Username": user.name,
            "Terminal": user.term,
            "Host": user.host,
            "Login Time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(user.started))
        })
    return user_details

# Function to gather all system information
def gather_system_info():
    system_info = {}
    system_info['OS Info'] = platform.uname()
    system_info['Network Details'] = get_network_details()
    system_info['Filesystem Details'] = get_filesystem_details()
    system_info['Process Details'] = get_process_details()
    system_info['Application Details'] = get_application_details()
    system_info['Memory Details'] = get_memory_details()
    system_info['User Details'] = get_user_details()
    
    return system_info

# Function to save system information to a file
def save_system_info_to_file(system_info):
    with open("system_info.txt", "w") as file:
        file.write("System Information:\n")
        file.write("="*50 + "\n")
        
        file.write("\nOS Info:\n")
        file.write(str(system_info['OS Info']) + "\n")
        
        file.write("\nNetwork Details:\n")
        for interface, details in system_info['Network Details'].items():
            file.write(f"Interface: {interface}\n")
            for key, value in details.items():
                file.write(f"{key}: {value}\n")
        
        file.write("\nFilesystem Details:\n")
        for device, details in system_info['Filesystem Details'].items():
            file.write(f"Device: {device}\n")
            for key, value in details.items():
                file.write(f"{key}: {value}\n")
        
        file.write("\nProcess Details:\n")
        for process in system_info['Process Details']:
            file.write(f"PID: {process['PID']} Name: {process['Name']} Username: {process['Username']}\n")
        
        file.write("\nApplication Details:\n")
        for app in system_info['Application Details']:
            file.write(f"PID: {app['PID']} Name: {app['Name']}\n")
        
        file.write("\nMemory Details:\n")
        for key, value in system_info['Memory Details'].items():
            file.write(f"{key}: {value}\n")
        
        file.write("\nUser Details:\n")
        for user in system_info['User Details']:
            file.write(f"Username: {user['Username']} Terminal: {user['Terminal']} Host: {user['Host']} Login Time: {user['Login Time']}\n")

# Main function to execute the script
if __name__ == "__main__":
    print("Gathering system information...")
    system_info = gather_system_info()
    save_system_info_to_file(system_info)
    print("System information has been saved to 'system_info.txt'.")
