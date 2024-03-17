# MAC Address Changer

This Python script allows you to change the MAC address of your network interfaces easily. It's particularly handy for situations where you need to spoof your MAC address for security or testing purposes.

## Requirements

- Python 3.x
- `inquirer` library (install via `pip install inquirer`)

## How to Use

1. Clone the repository to your local machine.

2. Run the script:

    ```bash
    python mac_changer.py
    ```

3. Follow the on-screen instructions to select the interface and choose a MAC address.

## Features

- Select your network interface (WiFi or Ethernet).
- Choose from a list of pre-defined MAC addresses or input your custom MAC address.
- Automatically retrieves your current MAC address.
- Changes your MAC address seamlessly.

## Usage Example

```bash
[+] Select between interfaces👇 
💁 wlan0 (Wifi)
💁 eth0 (Ethernet)
➿➿➿➿➿➿➿➿➿➿
==> wlan0

[+] You have selected wlan0!!

Choose Any Mac Address!!
  ◉ 00:0a:95:9d:68:22
  ◉ 00:0a:95:9d:68:23
  ◉ 00:15:5d:29:8e:76
  ◉ 00:15:5d:29:8e:77
  ◉ 00:24:d7:7c:ef:80
  ◉ 00:24:d7:7c:ef:81
  ◉ 00:50:56:c0:00:01
  ◉ 00:50:56:c0:00:02
  ◉ 00:e0:4c:53:44:55
  ◉ 00:e0:4c:53:44:56
  ◉ Custom!!

==> 00:0a:95:9d:68:22

[+] You entered 00:0a:95:9d:68:22

[+] Changing wlan0 interface to 00:0a:95:9d:68:22.....

[+] Mac Address has been changed!!

Current MAC Address: 00:0a:95:9d:68:22

Chalo Sahab ab me chalta hu!!
```
## Usage

1. Navigate to the project directory:
    ```bash
    cd mac-address-changer
    ```

2. Run the script:
    ```bash
    python mac_changer.py
    ```

3. Follow the on-screen instructions to select the network interface and specify the MAC address.

## Requirements

- Python 3.x
- `inquirer` library (install via `pip install inquirer`)

## How it Works

The script utilizes the `subprocess` module to interact with the system's network configuration. It provides functions to set the MAC address of the specified interface.

## Functions

- `command`: Executes system commands to manipulate network interface configurations.
- `result`: Retrieves the current MAC address of the system.
- `options`: Provides a menu to select predefined MAC addresses or enter a custom one.

## Notes

- Ensure you have appropriate permissions to modify network interfaces.
- Use this script responsibly and only on networks you own or have explicit permission to modify.
- For any issues or improvements, feel free to open an issue or submit a pull request.
- Happy networking! 🚀

