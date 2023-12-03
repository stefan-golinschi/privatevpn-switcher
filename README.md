# OpenVPN Auto Switcher

## Overview

The OpenVPN Auto Switcher is a Python script designed to streamline the process of switching between different OpenVPN configurations. It provides a terminal menu to choose from available OpenVPN configuration files, updates the configuration, restarts the OpenVPN service, and displays the external IP address using wtfismyip.com.

## Features

- **Configuration Management:** Automatically detects and lists available OpenVPN configurations in a specified directory.
- **User Interaction:** Provides an interactive terminal menu for users to select an OpenVPN configuration.
- **Service Restart:** Restarts the OpenVPN service after switching configurations to apply changes.
- **IP Information:** Fetches and displays the external IP address using wtfismyip.com.

## Prerequisites

- Python 3
- The `simple_term_menu` library
- OpenVPN installed and configured
- Systemd for managing services (for service restart functionality)

## Setup

1. Clone the repository or download the script (`auto_openvpn_switcher.py`) to your local machine.
2. Create a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
