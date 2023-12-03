# Scripts

### Parameters Passed to `--up` Script

1. **TUN/TAP Device Name (`$1`):**
   - The name of the TUN or TAP network interface device created by OpenVPN.
   
2. **Local IP Address (`$2`):**
   - The local IP address assigned to the OpenVPN endpoint.

3. **Port Number (`$3`):**
   - The port number on which the OpenVPN server is listening for incoming connections.

4. **Remote IP Address (`$4`):**
   - The IP address of the remote OpenVPN endpoint.

5. **Remote Port Number (`$5`):**
   - The port number on which the remote OpenVPN endpoint is listening.

These parameters are automatically passed to the `--up` script by OpenVPN when a connection is established. You can use these values in your script to perform custom actions or configurations based on the specifics of the OpenVPN connection.

