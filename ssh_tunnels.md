# Reverse SSH Tunnel to Hidden Server

To access a server behind a NAT you need to either forward the port or use a reverse SSH tunnel. The latter requires an external service which is likely paid. For this a good service is ngrok (https://ngrok.com/). It's free up to 1GB data out. Then it's $.1/GB. The configs are below:

`/etc/ngrok/ngrok.yml`

```
version: "3"
agent:
    authtoken: <YOUR_TOKEN>

tunnels:
  web:
    proto: tcp
    addr: 22
```

`/etc/systemd/system/ngrok.service`

```
[Unit]
Description=Start ngrok tunnel on startup
After=network-online.target
Wants=network-online.target systemd-networkd-wait-online.service

[Service]
ExecStart=/usr/local/bin/ngrok start --all --config /etc/ngrok/ngrok.yml
ExecReload=/bin/kill -HUP $MAINPID
KillMode=process
IgnoreSIGPIPE=true
Restart=always
RestartSec=3
Type=simple

[Install]
WantedBy=multi-user.target
```

```
$ sudo systemctl enable ngrok.service
$ sudo systemctl start ngrok.service
$ sudo systemctl status ngrok.service
```
