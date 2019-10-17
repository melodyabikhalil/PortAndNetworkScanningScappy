from scapy.all import ARP, Ether, srp

target_ip = "192.168.1.1/24"

def network_scan(target_ip):
    arp = ARP(pdst=target_ip)
    
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    clients = []
    
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    return clients
