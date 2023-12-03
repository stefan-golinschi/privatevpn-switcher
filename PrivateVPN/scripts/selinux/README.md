# SELinux

The SELinux policy is required when you try to modify firewalld rules using a up/down script in a openvpn config within a systemd service, like `openvpn-client@.service`.

Apply this policy using `semodule`:

```
semodule -i policy.pp
```


