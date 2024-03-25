import subprocess
import random
import re
import inquirer

################################### Functions ##################################

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
    inquirer.List(
            "MAC Address options", message="Choose Any Mac Address!!", choices=["Random","Custom!!"]
        )
    ]
    result = inquirer.prompt(options) 
    f2r = str(result)  
    fresult = f2r
    reg_choice = re.search(r"Random|Custom!!", fresult)  
    choice = reg_choice.group(0)
    if choice == "Random":                  
            return randmac() 
    elif choice == "Custom!!":
            print("Custom working perfectly!!")
            custom = input("Enter the your custom MAC Address ==> ")
            choosen_custom = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", custom)
            if choosen_custom:
                return choosen_custom.group(0)
            else:
                print("[+] Invaild Mac Address!!")
                quit("Please Try Again and Enter a vaild MAC Address!!")

def randmac():
    hex_list = ['a','b','c','d','e','f',1,2,3,4,5,6,7,8,9]
    output_list = [str(random.choice(hex_list)) + str(random.choice(hex_list)) for n in range (6)]
    mac = (":".join(output_list))
    return mac


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

    print("[+] You have selected eth0!!")

    final_interface = "eth0"
else:
    
    print("Invaild Choice!!")
    quit("Please Try Again!!")



mac = options()

# mac = input(
#     # "[+] Input you prefered mac address below 👇\n"
#     # "Example --> 11:22:33:44:55:66\n"
#     # "==> "
#     options()
# )



print(f"[+] You entered {mac}")
command(final_interface,mac)

print(f"[+] Changing {final_interface} interface to {mac}.....")

if new_mac == mac:

    print("They are same!!")
else:

    print("[+] Mac Address has be changed!!")

# print(f"[+] Succesfully Changed The Mac Address")

if result:
    print(result())
else:
    print("Can't Read Mac Address!!")




quit("\nChalo Sahab ab me chalta hu!!")


