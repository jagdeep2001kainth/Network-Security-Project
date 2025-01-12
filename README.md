ICMP Redirect attack (Man in the middle attack)

Name – Jagdeep Kainth

March 15, 2024 

Executive summary

This report explains about the packet redirection functionality provided by internet Control Message protocol(ICMP). The report discussing about what presence of ICMP Redirect messages in the network usually tells. Man in the Middle attack are one of the most common and dangerous cyber-attack, that can be a great harm to the security and privacy of the network. In this attack, a attacker(malicious actor) tries to intercept and change the communication between two hosts , for example a user and a web application page or a client and a server or even two different devices communicating on the same network. The attacker can steal important information of the victim, alter that information, inject malware, steal credential, redirect traffic. There are some recommendations to prevent this attack from happening. Client can use secure communication protocols for this such as HTTPS and avoid using http Client should only consider using those web pages that has SSL(secure socket layer) certificate. Usage of SSH (secure shell), SFTP(Secure File Transfer Protocol) for file transfers are highly recommended. Using VPN, and applying strong encryption and authentication protocols, firewalls, antivirus software can protect against MITM attack. 
[ Rublon Authors, December 14, 2023 ]

Attack Description 
An error message that a router sends to the IP packet sender is known as an ICMP redirect. Redirects are used by routers to let senders know that their following packets sent to the same destination should use a different router if they think a packet is being routed wrongly. One may utilize ICMP redirection by attackers to alter the victim's path. The aim of this operation is to initiate an ICMP redirect attack against the victim, so that the malicious router container (10.9.0.111) will be used as the victim's router when it receives packets addressed to 192.168.60.5. Since the attacker controls the malicious router, the attacker has the ability to intercept packets, alter them, and then resend the altered packets.
In this lab experiment, we will create a virtualized environment using docker container in seed ubuntu virtual machine. The attacker (10.9.0.105) used the malicious router to gain access to victim (10.9.0.5) computer. The attacker will intercept the packets that were being send through legitimate router 10.9.0.11 to the network 192.168.60.11. The picture given below is the exact topology used in this experiment. [ Wenliang Du, 2020 ]
