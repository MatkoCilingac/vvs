import network
import time
import machine
##vytvaranie wifi siete
nic : network.WLAN = network.WLAN(network.AP_IF)
nic.active(False)
time.sleep(0.5)
nic.active(True)

nic.config(essid = "ESP Riso a Ivana", authmode = network.AUTH_OPEN)

##nic.ifconfig(essid = "ESPRisoIvanaZaheslovane", authmode =network.AUTH_WPA2_PSK, password = "123456789")

print(f"Network configuration is {nic.ifconfig()}")

# pripojenie k existujucej wifi sieti
#nic : network.WLAN = network.WLAN(network.STA_IF)
#nic.active(False)
#time.sleep(0.5)
#nic.active(True)

#nic.connect("wifri","")
#while True :
 #   status :list[int] = nic.status()
  #  if status == network.STAT_GOT_IP :
   #     print ("The ESP323 board has connected to the wifi network.\n")
    #    print (f"Networ configuration is {nic.ifconfig()}\n")
     #   break
    #elif status == network.STAT_WRONG_PASSWORD :
     #   print ("The wifi password is wrong.\n")
      #  machine.soft_reset()
    #elif status == network.STAT_NO_AP_FOUND :
     #   print (f"The wifi name is wrong.\n")
      #  machine.soft_reset()
    #elif status == network.STAT_CONNECT_FAIL :
     #   print (f"Connecting to the wifi failed.\n")
      #  machine.soft_reset()

    #print(f"Currrent status  is {status}\n")
    #time.sleep(1)

