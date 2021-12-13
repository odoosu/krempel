##### calculate data transfer rate
    t = 120s | a = 25MB
    s = a/t = 25MB / 120s = 0,208MB/s
---
    s = 7MB/s | a = 134GB*1024 = 137216MB
    t = a/s = 137216MB / 7MB/s = 19602s
---
    t = 1,5h*3600 = 5400s | s = 200b/s / 8 = 25B/s / 1024 = 0,0244KB/s
    a = s*t = 0,0244KB/s * 5400s = 131,84KB/s
---

##### Vocabulary
Private network	: private address space of IP addresses, commonly used for LAN, specified by ranges (CIDR notation)
CIDR notation	: specifies subnetmask by decimal representation of leading 1-bit's (Class A -> 11111111.0.0.0)
Class C network	: 192.168.178.0/24	255.255.255.0	-> 254 possible IP addresses per network		| 2,097,150 possible networks
Class B newwork	: 172.16.0.0/16		255.255.0.0		-> 65,534 possible IP addresses per network		| 65,534 possible networks
Class A network	: 10.0.0.0/8		255.0.0.0		-> 16,777,214 possible IP addresses per network	| 126 possible networks
Sensor	- duh
Actor	- triggers action
Edge	- start/endpoint devices like routers
Fog		- network of sensors, IOT devices, edge devices and servers which carry out the calculation


##### IPv4
32-bit = 4,294,967,296 (2^32) unique addresses
In essence it forms the Internet. It uses a logical addressing system and performs routing, which is the forwarding of packets
from a source host to the next router that is one hop closer to the intended destination host on another network.

It's composed of with four ocetes seperated by dots (172.16.54.1 <- decimal representation) 
'Octets' because in binary notation the equivalent would be 10101100.00010000.11111110.0000001
[composition of an IPv4 address](https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/IPv4_address_structure_and_writing_systems-en.svg/799px-IPv4_address_structure_and_writing_systems-en.svg.png)

##### IPv6
128-bit = 2^128 unique addresses
IPv6 addresses consists of 8 groups of 4 hexadecimal digits seperated by : and can be represented in a shortend notation
Groups of zeros can be represented as :: and leading zeros can be truncated
2001:0db8:0000:0000:0000:8a2e:0370:1337 -> 2001:db8::8a2e:370:1337

[composition of an IPv6 address](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/IPv6_address_terminology-en.svg/720px-IPv6_address_terminology-en.svg.png)
##### WAN <- LAN <- PAN
Wide Area Networks consists of multiple Local Area Networks
Personal Area Networks are used to pair two devices over a shorter distance, like bluetooth


##### ARP
The Address Resolution Protocol uses broadcasting to translate layer 2(MAC-) and 3(IP-) addresses (also in reverse) in a network
[example](https://i.ytimg.com/vi/y2QA2GkoFwU/maxresdefault.jpg)
IPv6 equivalent would be the Neighbour Discovery Protocol


##### DHCP
Client uses broadcast to discover the router which then sends an offer (says hello) that's because there can be multiple (or none)
DHCP clients inside a network
Client then sends an request and recieves an IP address

[bild :)](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/DHCP_session.svg/424px-DHCP_session.svg.png)

##### Was ist ein cyperphysisches System?
Hab keine gute Beschreibung gefunden, aber auch keine lust ordentlich zu suchen

###### Good stuff
[Morpheus Tutorials](https://www.youtube.com/watch?v=QEsQkpG6I4w&list=PLNmsVeXQZj7rjW6OL4aGL-L1SzBUijh8r)