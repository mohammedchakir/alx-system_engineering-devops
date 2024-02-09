# *0x07. Networking basics #0*

`DevOps`    `Network`

By: Sylvain Kalache

## *Resources:*
Read or watch:

- [OSI model](https://en.wikipedia.org/wiki/OSI_model)
- [Different types of network](https://www.lifewire.com/lans-wans-and-other-area-networks-817376)
- [LAN network](https://en.wikipedia.org/wiki/Local_area_network)
- [WAN network](https://en.wikipedia.org/wiki/Wide_area_network)
- [Internet](https://en.wikipedia.org/wiki/Internet)
- [MAC address](https://whatismyipaddress.com/mac-address)
- [What is an IP address](https://www.bleepingcomputer.com/tutorials/ip-addresses-explained/)
- [Private and public address](https://www.iplocation.net/public-vs-private-ip-address)
- [IPv4 and IPv6](https://www.webopedia.com/insights/ipv6-ipv4-difference/)
- [Localhost](https://en.wikipedia.org/wiki/Localhost)
- [TCP and UDP](https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/)
- [TCP/UDP ports List](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)
- [What is ping /ICMP](https://en.wikipedia.org/wiki/Ping_%28networking_utility%29)
- [Positional parameters](https://www.adminschoice.com/bash-positional-parameters)

man or help:

- `netstat`
- `ping`

## *OSI Model:*

- What it is
- How many layers it has
- How it is organized

## *What is a LAN:*

- Typical usage
- Typical geographical size

## *What is a WAN:*

- Typical usage
- Typical geographical size
## *What is the Internet:*

- What is an IP address
- What are the 2 types of IP address
- What is `localhost`
- What is a subnet
- Why IPv6 was created

## *TCP/UDP:*

- What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
- What is the main difference between TCP and UDP
- What is a port
- Memorize SSH, HTTP and HTTPS port numbers
- What tool/protocol is often used to check if a device is connected to a network



## *Tasks:*

#### [0. OSI model](0-OSI_model)

OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.

It is organized from the lowest level to the highest level:

- The lowest level: layer 1 which is for transmission on physical layers with electrical impulse, light or radio signal
- The highest level: layer 7 which is for application specific communication like SNMP for emails, HTTP for your web browser, etc

Keep in mind that the OSI model is a concept, it’s not even tangible. The OSI model doesn’t perform any functions in the networking process. It is a conceptual framework so we can better understand complex interactions that are happening. Most of the functionality in the OSI model exists in all communications systems.

![4e6a0ad87a65d7054248](https://github.com/mohammedchakir/alx-system_engineering-devops/assets/129831433/f9f69716-5866-4180-ba38-b47cd65f2d2d)

In this project we will mainly focus on:

- The Transport layer and especially TCP/UDP
- On the Network layer with IP and ICMP
The image bellow describes more concretely how you can relate to every level.

![0fc96bd99faa7941b18bcae4c5f90c6acd11791d](https://github.com/mohammedchakir/alx-system_engineering-devops/assets/129831433/ed2ba039-a190-4979-aeb0-f0ead2715dc9)

Questions:

What is the OSI model?

   1- Set of specifications that network hardware manufacturers must respect
   2- The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology
   3- The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology

How is the OSI model organized?

   1- Alphabetically
   2- From the lowest to the highest level
   3- Randomly

#### [1. Types of network](1-types_of_network)

![4b995d4f8078b44afa968d68a98035d2bd7e8fac](https://github.com/mohammedchakir/alx-system_engineering-devops/assets/129831433/a7b20925-c7d7-434a-b928-125d382468f4)

LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.

Questions:

What type of network a computer in local is connected to?

   1- Internet
   2- WAN
   3- LAN

What type of network could connect an office in one building to another office in a building a few streets away?

   1- Internet
   2- WAN
   3- LAN
What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?

   1- Internet
   2- WAN
   3- LAN

    
#### [2. MAC and IP address](2-MAC_and_IP_address)

![1e348ba3bcbb094b02922f821ffeb3d8c5438b7b](https://github.com/mohammedchakir/alx-system_engineering-devops/assets/129831433/40c15156-b4e3-44bf-8680-f24350fa65c1)

Questions:

What is a MAC address?

   1- The name of a network interface
   2- The unique identifier of a network interface
   3- A network interface

What is an IP address?

   1- Is to devices connected to a network what postal address is to houses
   2- The unique identifier of a network interface
   3- Is a number that network devices use to connect to networks

    
#### [3. UDP and TCP](3-UDP_and_TCP)

![3d92e3c4a470f8ecf4c73db511fcbbadaa002e1c](https://github.com/mohammedchakir/alx-system_engineering-devops/assets/129831433/e8092704-f22a-4818-82fa-d601a854b3f0)

Let’s fill the empty parts in the drawing above.

Questions:

- Which statement is correct for the TCP box:
   1- `It is a protocol that is transferring data in a slow way but surely`
   2- `It is a protocol that is transferring data in a fast way and might loss data along in the process`
- Which statement is correct for the UDP box:
   1- `It is a protocol that is transferring data in a slow way but surely`
   2- `It is a protocol that is transferring data in a fast way and might loss data along in the process`
- Which statement is correct for the TCP worker:
   1- `Have you received boxes x, y, z?`
   2- `May I increase the rate at which I am sending you boxes?`

    
#### [4. TCP and UDP ports](4-TCP_and_UDP_ports)

Once packets have been sent to the right network device using IP using either UDP or TCP as a mode of transportation, it needs to actually enter the network device.

If we continue the comparison of a network device to your house, where IP address is like your postal address, UDP and TCP ports are like the windows and doors of your place. A TCP/UDP network device has 65535 ports. Some of them are officially reserved for a specific usage, some of them are known to be used for a specific usage (but nothing is officially declared) and the rest are free of use.

While the full list of ports should not be memorized, it is important to know the most used ports, let’s start by remembering 3 of them:

- 22 for SSH
- 80 for HTTP
- 443 for HTTPS

Note that a specific [IP + port = socket](https://stackoverflow.com/questions/152457/what-is-the-difference-between-a-port-and-a-socket).

Write a Bash script that displays listening ports:

- That only shows listening sockets
- That shows the PID and name of the program to which each socket belongs

    
#### [5. Is the host on the network](5-is_the_host_on_the_network)

![giphy](https://github.com/mohammedchakir/alx-system_engineering-devops/assets/129831433/be7c3515-ea5d-4a7f-aef0-9519d53a66a5)

The Internet Control Message Protocol (ICMP) is a protocol in the Internet protocol suite. It is used by network devices, to check if other network devices are available on the network. The command `ping` uses ICMP to make sure that a network device remains online or to troubleshoot issues on the network.

Write a Bash script that pings an IP address passed as an argument.

Requirements:

- Accepts a string as an argument
- Displays Usage: `5-is_the_host_on_the_network {IP_ADDRESS}` if no argument passed
- Ping the IP 5 times
 
It is interesting to look at the `time` value, which is the time that it took for the ICMP request to go to the `8.8.8.8` IP and come back to my host. The IP `8.8.8.8` is owned by Google, and the quickest roundtrip between my computer and Google was 7.57 ms which is pretty fast, which is a sign that the network path between my computer and Google’s datacenter is in good shape. A slow ping would indicate a slow network.

Next time you feel that your connection is slow, try the `ping` command to see what is going on!
