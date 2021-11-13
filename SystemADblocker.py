import os
import platform
import ctypes, sys
import time

system = platform.system()
version = platform.release()
codename = os.name
print ("---------------------------")
print ("Your system :", system)
print ("Version : ", version)
print ("Codename ", codename)
print ("---------------------------")

if system == "Windows":
    def WindowsWifi():
        print ("Applying AD protecting DNS on the wifi interface")
        os.system('netsh interface ipv4 show interfaces')
        os.system('netsh interface ip set dns name="Wi-Fi" static 94.140.14.14')
        os.system('netsh interface ip add dns name="Wi-Fi" 94.140.15.15 index=2')
        os.system('netsh interface ip set dnsservers name="Wi-Fi" source=dhcp')
        os.system('pause')
        os.system('cls')

    def WindowsEthernet():
        print ("Applying AD protecting DNS on the ethernet interface")
        os.system('netsh interface ipv4 show interfaces')
        os.system('netsh interface ip set dns name="Ethernet" static 94.140.14.14')
        os.system('netsh interface ip add dns name="Ethernet" 94.140.15.15 index=2')
        os.system('netsh interface ip set dnsservers name="Ethernet" source=dhcp')
        os.system('pause')
        os.system('cls')

    def ChooseWindowsInterface():
        interface = int (input ("Select the interface to block ads on [1] for wifi, [2] for ethernet, [3] for both : "))
        if interface == 1:
            WindowsWifi()

        if interface == 2:
            WindowsEthernet()
            
        if interface == 3:
            WindowsWifi()
            WindowsEthernet()

        if interface > 3:
            print ("Invalid Input, retrying...")
            time.sleep(100)
            os.system('cls')
            ChooseWindowsInterface()
            
    def AvoidWindowsPreloadedAds():
        os.system('cls')
        print("The script will now clear temp files to avoid pre-loaded ads")
        os.system('del %temp%\*.*')
        print ("Don't forget to clear your browser cache :) ")

    def WindowsTestPing():
        hostname = "google-analytics.com" 
        response = os.system("ping -c 1 " + hostname)
        if response == 0:
            print (hostname, 'is up!')
            print ("Sorry :/,The script didn't work, you can retry later")
        else:
            print (hostname, 'is down!')
            print ("System Cleared : ", system, codename, version)
    ChooseWindowsInterface()
    AvoidWindowsPreloadedAds()
    WindowsTestPing()
    
if system == "Linux":
    print ("Linux is not yet supported but it will be soon")
    #def LinuxWifi():

    #def LinuxEthernet():

    #def ChooseLinuxInterface():

    #def AvoidLinuxPreloadedAds():

    #def LinuxTestPing():

if system == "Darwin":
    print ("The script doesn't support macOS, go buy a real pc :)")
