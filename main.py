import subprocess
import distro

print("Starting...")

distro_name = distro.name() # returns Fedora Linux

print("Installing haveged...")

if (distro_name == "Fedora Linux"):
    subprocess.run(["sudo", "dnf","-y", "install", "haveged"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("Installed haveged.")

while True:
    adapter_name = input("We need your Wi-Fi interface name. \nHINT: You can find it with the command \"ifconfig\" \nPlease enter your Wi-Fi interface name: ")
    wifi_name = input("Enter hotspot Wi-Fi name: ")

    while True:
        password_name = input("Enter hotspot Wi-Fi password (Minimum 8 characters): ")
        if (len(password_name) >= 8 ):
            break
        else:
            continue
    
    print("Wi-Fi Name: " + wifi_name)
    print("Password:" + password_name)

    while True:
        confirm_input = input("Do you confirm? (Enter \"yes\" or \"no\"): ")
        if (confirm_input == "yes"):
            break
        elif (confirm_input == "no"):
            break
        else:
            continue

    if confirm_input == "yes":
        break
    elif confirm_input == "no":
        continue

subprocess.run(["sudo", "create_ap", adapter_name, adapter_name, wifi_name, password_name])
