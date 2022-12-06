import os 
import time 
print("installer v 1.0.1")
if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")
input("please connect to internet via network cable, then press enter")
print("what do you want to do")
print("1: full install (run this for first time setup)")
print("2: update system packages")
print("3: install apt packages")
print("4: install pip3 packages")
print("5: setup wifi")
installMode = int(input("mode: "))
if(installMode == 1 or installMode == 2):
    print("updating system")
    os.system("apt update")
    os.system("apt upgrade")
if(installMode == 1 or installMode == 3):
    print("installing apt packages")
    os.system("apt install alsa-utils")
    os.system("apt install libespeak1")
    os.system("apt install net-tools")
    os.system("apt install wpasupplicant")
    os.system("apt install python3-rpi.gpio")
    os.system("apt install ntp")
    os.system("apt install wpasupplicant")
    os.system("apt install iw")
    os.system("apt install bpytop")
if(installMode == 1 or installMode == 4):
    print("installing pip3 packages")
    os.system("pip3 install wikipedia")
    os.system("pip3 install datetime")
    os.system("pip3 install speechRecognition")
    os.system("pip3 install pyttsx3")
    os.system("pip3 install gpiozero")
    os.system("pip3 install pyaudio")
if(installMode == 1):
    print("seting up start.service")
    os.system("mv start.service /etc/systemd/system/start.service")
    os.system("mv network-wireless@.service /etc/systemd/system/network-wireless@.service")
    os.system("systemctl enable start.service")
    os.system("systemctl enable network-wireless@.service")
    os.system("ln -s /etc/systemd/system/network-wireless@.service /etc/systemd/system/multi-user.target.wants/network-wireless@wlan0.service")
    os.system("chmod +x start.sh")
    os.system("chmod +x netStart.sh")
    os.system("chmod +x /etc/systemd/system/network-wireless@.service")
    os.system("chomd +x /exc/systemd/system/start.service")
if(installMode == 1 or installMode == 5):
    print("wifi setup")

    connectNet = True
    while(connectNet):
        
        interface = os.system("iw dev")
        interface = input("please enter the name of the wifi interface as it appears above: ")
        print("scanning for networks")
        os.system("ifconfig "+interface+" up")
        print(os.system("nmcli dev wifi"))
        netName = input("enter the name of the network you wish to connect to as it appears above (leave blank if you wish to continue without wifi): ")
        password = input("enter network password (leave blank if none): ")
        if(netName == ""):
            connectNet = False
        
        os.system("wpa_passphrase "+ netName+ "| sudo tee /etc/wpa_supplicant.conf")
        if(password != ""):
            os.system("wpa_passphrase "+netName + password + " | tee /etc/wpa_supplicant.conf")
        os.system("wpa_supplicant -c /etc/wpa_supplicant.conf -i "+interface)
        response = os.system("ping -c 1 -W 0.5 connectivity-check.ubuntu.com")
        if(response == 0):
            connectNet = False
            print("connection confirmed")
        else:
            print("could not verify connection")

time.sleep(5)
print("restarting")
os.system("shutdown -r now")
