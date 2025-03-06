import os
import subprocess

def get_network_details():
    print("\n[Network Details]")
    subprocess.run(["ipconfig", "/all"])
    subprocess.run(["netstat", "-ano"])

def get_file_system_details():
    print("\n[File System Details]")
    subprocess.run(["wmic", "logicaldisk", "get", "name,filesystem,size,freespace"])

def get_process_details():
    print("\n[Process Details]")
    subprocess.run(["tasklist"])

def get_application_details():
    print("\n[Installed Applications]")
    subprocess.run(["wmic", "product", "get", "name"])

def get_memory_details():
    print("\n[Memory Details]")
    subprocess.run(["wmic", "OS", "get", "TotalVisibleMemorySize,FreePhysicalMemory"])

def get_user_details():
    print("\n[User Details]")
    subprocess.run(["whoami"])
    subprocess.run(["net", "user"])

def main():
    while True:
        print("\nSelect an option to fetch system details:")
        print("1. Network Details")
        print("2. File System Details")
        print("3. Process Details")
        print("4. Application Details")
        print("5. Memory Details")
        print("6. User Details")
        print("7. Fetch All Details")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            get_network_details()
        elif choice == "2":
            get_file_system_details()
        elif choice == "3":
            get_process_details()
        elif choice == "4":
            get_application_details()
        elif choice == "5":
            get_memory_details()
        elif choice == "6":
            get_user_details()
        elif choice == "7":
            get_network_details()
            get_file_system_details()
            get_process_details()
            get_application_details()
            get_memory_details()
            get_user_details()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()
