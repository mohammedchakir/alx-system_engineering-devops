## *0x08. Networking basics #1*

`DevOps`   `Network`   `SysAdmin`

By: Sylvain Kalache

![image](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/285/s7kpNYq.png)

## *Resources:*

Read or watch:

- [What is localhost](https://en.wikipedia.org/wiki/Localhost)
- [What is 0.0.0.0](https://en.wikipedia.org/wiki/0.0.0.0)
- [What is the hosts file](https://www.makeuseof.com/tag/modify-manage-hosts-file-linux/)
- [Netcat examples](https://www.thegeekstuff.com/2012/04/nc-command-examples/)

man or help:

- `ifconfig`
- `telnet`
- `nc`
- `cut`

## *General:*

- What is localhost/127.0.0.1
- What is 0.0.0.0
- What is `/etc/hosts`
- How to display your machine’s active network interfaces

## *Tasks:*

#### [0. Change your home IP](0-change_your_home_IP)

Write a Bash script that configures an Ubuntu server with the below requirements.

Requirements:

- `localhost` resolves to `127.0.0.2`
- `facebook.com` resolves to `8.8.8.8`.
- The checker is running on Docker, so make sure to read [this](http://blog.jonathanargentiero.com/docker-sed-cannot-rename-etcsedl8ysxl-device-or-resource-busy/)

In this example we can see that:

- before running the script, `localhost` resolves to `127.0.0.1` and `facebook.com` resolves to `157.240.11.35`
- after running the script, `localhost` resolves to `127.0.0.2` and `facebook.com` resolves to `8.8.8.8`

If you’re running this script on a machine that you’ll continue to use, be sure to revert `localhost` to `127.0.0.1.` Otherwise, a lot of things will stop working!

    
#### [1. Show attached IPs](1-show_attached_IPs)

Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.

Obviously, the IPs displayed may be different depending on which machine you are running the script on.

Note that we can see our `localhost` IP :)


#### [2. Port listening on localhost](100-port_listening_on_localhost)

Write a Bash script that listens on port `98` on `localhost`.

Connecting to localhost on port 98 using telnet and typing some text.

For the sake of the exercise, this connection is made entirely within `localhost`. This isn’t really exciting as is, but we can use this script across networks as well. Try running it between your local PC and your remote server for fun!

As you can see, this can come in very handy in a multitude of situations. Maybe you’re debugging socket connection issues, or you’re trying to connect to a software and you are unsure if the issue is the software or the network, or you’re working on firewall rules… Another tool to add to your debugging toolbox!
