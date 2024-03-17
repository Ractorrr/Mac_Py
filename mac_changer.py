import subprocess

import re
import inquirer

# ################################## Functions ##################################

def command (final_interface, mac):
    subprocess.call(f"ifconfig {final_interface} down", shell=True)
    subprocess.call(f"ifconfig {final_interface} hw ether {mac}", shell=True)
    subprocess.call(f"ifconfig {final_interface} up", shell=True)


def result ():
    result_1 = subprocess.check_output(["ifconfig"]).decode("utf-8")
    result  = re.search(r".ether \w\w:\w\w:\w\w:\w\w:\w\w:\w\w", result_1)
    final_result = result
    if final_result:
        return final_result.group(0)
    else:
        print("Unable to find Mac Address")
        quit()


def options ():
    options = [
    inquirer.Checkbox(
            "MAC Address options", message="Choose Any Mac Address!!", choices=["00:0a:95:9d:68:22","00:0a:95:9d:68:23","00:15:5d:29:8e:76","00:15:5d:29:8e:77","00:24:d7:7c:ef:80","00:24:d7:7c:ef:81","00:50:56:c0:00:01","00:50:56:c0:00:02","00:e0:4c:53:44:55","00:e0:4c:53:44:56","Custom!!"]
        )
    ]
    result = inquirer.prompt(options) 
    final = result.get("Mac address is ", result)
    f_result = str(final)
    #print(type(f_result))
    #result = ", ".join(item for item in final if isinstance(item, str))
    #final_1 = final.decode("utf-8")
    #final_1 = "".join(final)
    #return f_result 
    choosen_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", f_result)
    #return choosen_mac.group(0)
    if choosen_mac:
        return choosen_mac.group(0)
    else:
        custom = input("Enter the your custom MAC Address ==> ")
        choosen_custom = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", custom)
        if choosen_custom:
            return choosen_custom.group(0)
        else:
            print("[+] Invaild Mac Address!!")
            quit()
    
###############################################################################

new_mac = result()
final_interface = "a"
updated_mac = None


interface = input(
    "[+] Select between interfaces👇 \n"
    "💁 wlan0 (Wifi)\n"
    "💁 eth0 (Ethernet)\n"
    "➿➿➿➿➿➿➿➿➿➿\n"
    "==> "
)



if interface == "1" or interface == "wlan0":
    print("[+] You have selected wlan0!!")
    final_interface = "wlan0"
elif interface == "2" or interface == "eth0":  
    print()
    print("[+] You have selected eth0!!")
    print()
    final_interface = "eth0"
else:
    print()
    print("error!!")



mac = options()


# mac = input(
#     # "[+] Input you prefered mac address below 👇\n"
#     # "Example --> 11:22:33:44:55:66\n"
#     # "==> "
#     options()
# )


print()
print(f"[+] You entered {mac}")
command(final_interface,mac)
print()
print(f"[+] Changing {final_interface} interface to {mac}.....")

if new_mac == mac:
    print()
    print("They are same!!")
else:
    print()
    print("[+] Mac Address has be changed!!")

# print(f"[+] Succesfully Changed The Mac Address")
print()
if result:
    print(result())
else:
    print("Can't Read Mac Address!!")


quit("\nChalo Sahab ab me chalta hu!!")


