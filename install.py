import os 
import time 
if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")
input("please connect to internet via network cable, then press enter")
print("updating system")
os.system("apt update")
os.system("apt upgrade")
print("installing apt packages")
os.system("apt install alsa-utils")
os.system("apt install libespeak1")
os.system("apt install net-tools")
os.system("apt install wpasupplicant")
os.system("apt install python3-rpi.gpio")
os.system("apt install bpytop")
print("installing pip3 packages")
os.system("pip3 install wikipedia")
os.system("pip3 install datetime")
os.system("pip3 install speechRecognition")
os.system("pip3 install pyttsx3")
os.system("pip3 install gpiozero")
os.system("pip3 install pyaudio")
print("seting up start.service")
os.system("mv start.service /etc/systemd/system/start.service")
os.system("systemctl enable start")
print("wifi setup")

connectNet = False
while(connectNet):

    os.system("iw dev")
    interface = input("please enter the name of the wifi interface as it appears above: ")
    print("scanning for networks")
    os.system("ifconfig "+interface+" up")
    print(os.system("nmcli dev wifi"))
    netName = input("enter the name of the network you wish to connect to as it appears above (leave blank if you wish to continue without wifi): ")
    password = input("enter network password (leave blank if none): ")
    if(netName == ""):
        connectNet = False
    
    os.system("iwconfig "+interface+" essid "+netName)
    if(password != ""):
        os.system("iwconfig "+interface+" key "+password)
    response = os.system("ping -c 1 -W 0.5 connectivity-check.ubuntu.com")
    if(response == 0):
        connectNet = False
        print("connection confirmed")
    else:
        print("could not verify connection")
print("")
print("wifi connectivity is not currently supported")
print("")
time.sleep(5)
print("restarting")
#os.system("shutdown -r now")
