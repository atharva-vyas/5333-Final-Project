# How to make wg-portal function as intended
1) docker compose down 
2) docekr prune images -a
3) docekr compose up -d --build
4) docker restart wg-portal
5) log into wg-portal
6) check if you can see the interfaces that were running on the wireguard server
7) if you are using the my custom made wiregurad configs initially:
	1) add a endpoint address in the peer defaults (131.186.6.60:5182)
	2) in the "IP Networks" & "Allowed IP Address" add the subnet address (10.13.13.0/24)
	3) hit "APPLY PEER DEFAULTS"

> "IP Networks" is used my wg-portal to dynamically assign ip's to new configs/devices that join the network
> "Allowed IP Addresses" is used by the wg-portal to specify what traffic is allowed to flow through the config/wireguard vpn
