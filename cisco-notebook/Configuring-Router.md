# Configuring a Router.  

## Initial Configuration.  

* Go to Privileged EXEC mode  
```  
> enable  
```  
* Go to global configuration mode  
```  
# configure terminal  
```  
* Rename the device  
```  
(config)# hostname the-router-name
```  
* Disable name translations in host address name  
```  
(config)# no ip domain-lookup
```  
* Secure management   
```  
(config)# service password-encryption  
(config)# security passwords min-length 10
(config)# login block-for 120 attempts 3 within 25
(config)# enable secret the-privilege-password  
(config)#
(config)#
(config)# ip domain-name the-domain-name
(config)# crypto key generate rsa 
1024 
(config)# ip ssh version 2
(config)# ip ssh time-out 120
(config)# username the-user privilege 15 secret the-password 
(config)#
(config)# 
(config)# line console 0
(config-line)# password the-console-password
(config-line)# login
(config-line)# logging synchronous
(config-line)# exec-timeout 60
(config-line)# exit
(config)#
(config)#
(config)# line vty 0 4
(config-line)# password the-vty-password
(config-line)# transport input ssh
(config-line)# login local
(config-line)# logging synchronous
(config-line)# exec-timeout 60
(config-line)# login
(config-line)# exit
```  
* Configure a banner   
```  
(config)# banner motd the-message
(config)# exit
```  

## Configure a interface.  

* Interface Addressing  
```
interface interface-name
description the-description
ip address IPv4-Address Subnet-Mask
ipv6 address IPv6-Address
ipv6 address FE80::1 link-local 
no shutdown
```  
* Interface serial clock configuration  
```
clock rate 12800
```
* Subinterfaces for VLAN (example for the Blue Network)
```  
interface g6/0.10
encapsulation dot1Q 10
ip address 192.168.1.1 255.255.255.248

interface g6/0.20
encapsulation dot1Q 20
ip address 192.168.1.9 255.255.255.248

interface g6/0.30
encapsulation dot1Q 30
ip address 192.168.1.17 255.255.255.248

interface g6/0.150
encapsulation dot1Q 150
ip address 192.168.1.25 255.255.255.248
exit

interface g6/0.100
encapsulation dot1Q 100
ip address 192.168.1.33 255.255.255.252
exit

interface g6/0
no shutdown 
exit 
```   

## Configure Routing Protocol  

* OSPF  
```
router ospf 10
router-id 1.1.1.1
network IPv4-Address 0.0.0.255 area 0
network IPv4-Address 0.0.0.255 area 0
network IPv4-Address 0.0.0.255 area 0
end
```

## Save the configuration  

* Save  
```  
# copy running-config startup-config
```   
* Save the configuration to a ftp server  
```  
# copy running-config ftp:
```  
