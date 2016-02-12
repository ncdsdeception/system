from scapy.all import *
from scapy.layers.inet import *

class RouteHandler(object):

    def __init__(self,nv):
        self.networkview = nv

    def createRouteResponse(self, pkt):
        src_eth = pkt[0][Ether].src
        dst_eth = pkt[0][Ether].dst
        src_ip = pkt[0][IP].src
        dst_ip = pkt[0][IP].dst
        cur_ttl = pkt[0][IP].ttl

        route = self.networkview.getRouteToIP(dst_ip)

        hop=0
        if route != None:
            for h in route.hops:
                print("Checking hop " + str(hop) + " to " + str(h.decepted_ip_addr) + " cur ttl=" + str(cur_ttl))
                hop_ip = h.decepted_ip_addr
                hop_eth = h.decepted_eth_addr
                if cur_ttl==hop and hop_ip!=dst_ip:
                    #icmp time exceed during transmission
                    ether = Ether(src=hop_eth, dst=src_eth)
                    ip = IP(src=hop_ip, dst=src_ip)
                    icmp = ICMP(type=11, code=0)
                    #resp = ether/ip/icmp/pkt[0][IP]/pkt[0][UDP]
                    resp = ether/ip/icmp/IPerror(str(pkt[0][IP]))
                    #recalculate checksum
                    resp.show2()
                    return resp
                if cur_ttl==hop and hop_ip==dst_ip:
                    #icmp destination and port unreachable
                    ether = Ether(src=hop_eth, dst=src_eth)
                    ip = IP(src=hop_ip, dst=src_ip)
                    icmp = ICMP(type=3, code=3)
                    resp = ether/ip/icmp/IPerror(str(pkt[0][IP]))
                    #recalculate checksum
                    resp.show2()
                    return resp
                hop+=1




