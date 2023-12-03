#!/usr/bin/env python3

import os
import subprocess
import requests
import time

from simple_term_menu import TerminalMenu

# Local Configuration
OPENVPN_CONFIGFILE = "privatevpn.conf"
CONFIG_DIR = "./PrivateVPN"
OPENVPN_SERVICEFILE = "openvpn-client@privatevpn.service"


def get_configs(config_dir) -> dict:
    """
    Retrieve OpenVPN configuration files from the specified directory.

    Parameters:
        - config_dir (str): The directory containing OpenVPN configuration files.

    Returns:
        dict: A dictionary mapping human-readable names (without '.ovpn' extension)
              to the corresponding file names within the provided directory.

    Example:
        Given a directory structure with OpenVPN configuration files:
        ```
        /path/to/configs
        ├── example_config1.ovpn
        ├── example_config2.ovpn
        ├── example_config3.ovpn
        ```
        Calling `get_configs('/path/to/configs')` would return:
        ```
        {'example_config1': 'example_config1.ovpn',
         'example_config2': 'example_config2.ovpn',
         'example_config3': 'example_config3.ovpn'}
        ```
    """
    configs = {}
    for root, dirs, files in os.walk(config_dir):
        for file in files:
            if ".ovpn" in file:
                config = {}
                file_name = file
                pretty_name = file.rstrip(".ovpn")
                configs[pretty_name] = file_name
    return configs


def restart_systemd_service(service_name):
    """
    Restart a systemd service.

    Parameters:
        - service_name (str): The name of the systemd service to restart.

    Raises:
        subprocess.CalledProcessError: If the subprocess to restart the service fails.

    Example:
        Calling `restart_systemd_service('my_service')` attempts to restart the 'my_service' systemd service.
        If successful, it prints a success message. If an error occurs during the restart, an exception is raised
        with an error message indicating the failure.
    """
    try:
        subprocess.run(["sudo", "systemctl", "restart",
                       service_name], check=True)
        print(f"The {service_name} service has been restarted.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Unable to restart {service_name} service. {e}")


def wtfismyip():
    """
    Retrieve information about the public IP address from wtfismyip.com.

    Returns:
        dict or None: A dictionary containing information about the public IP address
                      if the request is successful. Returns None if an error occurs.

    Example:
        ip_info = wtfismyip()
        if ip_info:
            print("IP Address:", ip_info["YourFuckingIPAddress"])
            print("Location:", ip_info["YourFuckingLocation"])
            print("ISP:", ip_info["YourFuckingISP"])
            # Add more fields as needed
        else:
            print("Failed to retrieve IP information.")
    """

    url = "https://wtfismyip.com/json"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        json_data = response.json()
        return json_data

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def select_openvpn_config(configs):
    """
    Display a terminal menu for selecting an OpenVPN configuration file.

    Parameters:
        configs (dict): A dictionary mapping configuration names to file names.

    Returns:
        str or None: The selected OpenVPN configuration file name, or None if no configuration
                     files are available or an error occurs.
    """
    options = list(configs.keys())

    if not options:
        print("No OpenVPN configurations available.")
        return None

    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()

    selected_item = options[menu_entry_index]
    return selected_item


def main():
    configs = get_configs(CONFIG_DIR)
    selected_config = select_openvpn_config(configs)

    if selected_config:
        # Remove old link
        try:
            os.unlink(OPENVPN_CONFIGFILE)
        except FileNotFoundError:
            # If already removed, do nothing
            pass

        selected_item_path = os.path.join(
            CONFIG_DIR, configs[selected_config])
        os.symlink(selected_item_path, OPENVPN_CONFIGFILE)
        restart_systemd_service(OPENVPN_SERVICEFILE)

        time.sleep(5)
        myip = wtfismyip()
        print(
            f"External IP: {myip['YourFuckingIPAddress']}[{myip['YourFuckingLocation']}]")


if __name__ == "__main__":
    main()

