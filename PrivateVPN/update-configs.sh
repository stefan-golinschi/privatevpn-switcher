#!/bin/bash

set -e

# Get the absolute path to the script's directory
script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

# Get the absolute path to the current working directory
current_dir=$(pwd)

# Check if the script is called from its directory
if [ "$script_dir" != "$current_dir" ]; then
    echo "Error: Please run the script from its directory."
    exit 1
fi

# Clean older files
rm -rf PrivateVPN-*.ovpn

base_url="https://ovpnstorage.privatevpn.com/Dedicated-TUN-UDP-128-GCM/"
file_list=("PrivateVPN-AU-Sydney-TUN-1195.ovpn"
           "PrivateVPN-BR-SaoPaulo-TUN-1195.ovpn"
           "PrivateVPN-CA-Toronto-TUN-1195.ovpn"
           "PrivateVPN-CH-Zurich-TUN-1195.ovpn"
           "PrivateVPN-ES-Madrid-TUN-1195.ovpn"
           "PrivateVPN-FR-Paris-TUN-1195.ovpn"
           "PrivateVPN-IN-Mumbai-TUN-1195.ovpn"
           "PrivateVPN-IT-Milan-TUN-1195.ovpn"
           "PrivateVPN-JP-Tokyo-TUN-1195.ovpn"
           "PrivateVPN-NL-Amsterdam-TUN-1195.ovpn"
           "PrivateVPN-NO-Oslo-TUN-1195.ovpn"
           "PrivateVPN-PL-Torun-TUN-1195.ovpn"
           "PrivateVPN-SE-Stockholm-TUN-1195.ovpn"
           "PrivateVPN-UK-London-TUN-1195.ovpn"
           "PrivateVPN-US-LosAngeles-TUN-1195.ovpn"
           "PrivateVPN-US-NewYork-TUN-1195.ovpn"
          )

for file in "${file_list[@]}"
do
    url="${base_url}${file}"
    echo "Downloading $file..."
    wget -q "$url"

    sed -i 's/auth-user-pass/auth-user-pass PrivateVPN\/.pass/g' $file
    #sed -i 's/dev tun/dev tun0/g' $file

    echo -e "\n\n# Up/Down Scripts" >> $file
    echo "script-security 2" >> $file
    echo "up PrivateVPN/scripts/up-script.sh" >> $file
    echo "down PrivateVPN/scripts/down-script.sh" >> $file
    dos2unix $file > /dev/null 2>&1
    
done

echo "Download complete!"
