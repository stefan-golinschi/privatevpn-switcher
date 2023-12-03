#!/bin/bash

# Get the name of the TUN interface being taken down
tun_interface=$1
firewall_zone=vpn

# Remove the TUN interface from the firewalld zone
firewall-cmd --zone=$firewall_zone --add-interface=$tun_interface

# Additional cleanup or actions can be added here if needed

