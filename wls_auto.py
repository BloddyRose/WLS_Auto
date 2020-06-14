import os
import sys
import pyfiglet
import wget
import shutil
# https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi


def v_m():
    print("\t---Activating Virtual Support!...Please Wait---\n\t---Disk Management Will Run in a second do not exit---")
    print("\t---Virtual Machine---")
    os.system(
        "powershell dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart")
    print("\t---DONE---")
    print("\n")
    print("\n")


def wls():
    print("\t---Activating Wls Support!...Please Wait---\n\t---Disk Management Will Run in a second do not exit---")
    os.system("powershell dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart")
    print("\t---Wls 1 Installed---\tNow will Install WLS 2 and set it to Default---")
    os.system("powershell dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart && wsl --set-default-version 2")
    print("\t---DONE---")
    print("\n")
    print("\n")


def update():
    print("\t---Downloading Kernel Update!...Please Wait---\n\t---Will Run in a second do not exit Follow The Instructions---")
    url = "https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi"
    file = wget.download(url)
    os.system('cmd msiexec /i %s /qn' % file)
    print("\n")
    print("\n")


def main():
    while True:
        print("\n")
        print("\t----Welcome to WLS auto installer!")
        print("\t----My Name is BloddyRose and I made this scrit for those u don/'t know to install WLS 2.")
        print("\t---Only for 2004 update Windows 10, And cpu with VM support!")

        print("\n")

        print("\t 1. Activate Virtual Machine Support.")
        print("\t 2. Activate WLS1 and Update to WLS2.")
        print("\t 3. Download Update for Linux Kernel.")
        print("\t 4. How to install.")
        print("\t Write reboot or r for Reboot (After 1 ,2 ,3 Very Recommended!)")

        choice = input("\t>>> ")
        if choice == "1":
            v_m()

        elif choice == "2":
            wls()

        elif choice == "3":
            update()

        elif choice == "4":
            print("\t---To install an Linux System go to Microsoft Store---\n")
            print(
                "\t---And Run It from Start Menu or Command Prompt if you know the name.")
            result = pyfiglet.figlet_format("Bloddy Rose", font="digital")
            print(result)
            print("\t---Github https://github.com/BloddyRose")
        elif choice == "reboot" or "r":
            print("\t---Rebooting...")
            os.system("shutdown -t 10 -r -f")


main()
