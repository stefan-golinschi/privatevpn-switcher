# PrivateVPN Configuration

## Password file

The password file is created like this:

```
echo MyUserName > .pass
echo MyPassword >> .pass
```

## Firewalld rules

```bash
firewall-cmd --add-forward-port=port=port-number:proto=tcp|udp|sctp|dccp:toport=port-number
firewall-cmd --add-forward-port=port=port-number:proto=tcp|udp:toport=port-number:toaddr=IP

firewall-cmd --add-masquerade
firewall-cmd --add-forward-port=port=80:proto=tcp:toport=8008 --zone=vpn --permanent
firewall-cmd --add-forward-port=port=443:proto=tcp:toport=8443 --zone=vpn --permanent
```
