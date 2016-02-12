
from pox.core import core
import pox.openflow.libopenflow_01 as of
import pox.openflow.nicira as nx
from pox.lib.util import str_to_bool
from pox.lib.packet.ethernet import ethernet
import pox.lib.packet as pkt
import pox.lib.packet.arp as arp
import pox.lib.packet.icmp as icmp
import pox.lib.packet.tcp as tcp
import pox.lib.packet.ipv4 as ipv4
from pox.lib.addresses import IPAddr, EthAddr
from pox.NCDS_controller.Node import Node

log = core.getLogger()

class Policy(object):

    def specifyAccessPolicy(self):
        hosts = self.listHosts()
        honeypots = self.listHoneypots()
        honeyrouters = self.listHoneyRouters()

        mapping = {}

        access_1 = []
        access_1.append(hosts[1])
        access_1.append(hosts[2])
        access_1.append(honeypots[0])
        access_1.append(honeypots[2])
        access_1.append(honeypots[4])
        access_1.append(honeyrouters[1])

        access_2 = []
        access_2.append(hosts[2])
        access_2.append(honeypots[1])
        access_2.append(honeypots[3])
        access_2.append(honeyrouters[0])

        access_3 = []
        access_3.append(hosts[1])
        access_3.append(honeypots[0])
        access_3.append(honeypots[1])
        access_3.append(honeypots[4])
        access_3.append(honeyrouters[1])

        mapping[hosts[0].ip_addr] = access_1
        mapping[hosts[1].ip_addr] = access_2
        mapping[hosts[2].ip_addr] = access_3

        return mapping

    def specifyRoutePolicy(self):
        hosts = self.listHosts()
        honeypots = self.listHoneypots()
        honeyrouters = self.listHoneyRouters()

        routes = {}

        routes_2 = []

        route_2_1 = []
        route_2_1.append(honeyrouters[0])
        route_2_1.append(honeypots[3])
        routes_2.append(route_2_1)

        routes_3 = []

        route_3_1 = []
        route_3_1.append(honeyrouters[1])
        route_3_1.append(honeypots[4])
        routes_3.append(route_3_1)

        routes[hosts[1]].ip_addr = routes_2
        routes[hosts[2].ip_addr] = routes_3
        return routes

    def listHosts(self):
        hosts = []
        hosts.append(Node(IPAddr("10.0.0.1"), EthAddr("00:00:00:00:00:01"), False, False, 1))
        hosts.append(Node(IPAddr("10.0.0.2"), EthAddr("00:00:00:00:00:02"), False, False, 2))
        hosts.append(Node(IPAddr("10.0.0.3"), EthAddr("00:00:00:00:00:03"), False, False, 3))
        return hosts

    def listHoneypots(self):
        honeypots = []
        honeypots.append(Node(IPAddr("10.0.0.5"), EthAddr("00:00:00:00:00:05"), True, False, 1))
        honeypots.append(Node(IPAddr("10.0.0.6"), EthAddr("00:00:00:00:00:06"), True, False, 1))
        honeypots.append(Node(IPAddr("10.0.0.7"), EthAddr("00:00:00:00:00:07"), True, False, 1))
        honeypots.append(Node(IPAddr("10.11.0.8"), EthAddr("00:00:11:00:00:08"), True, False, 1))
        honeypots.append(Node(IPAddr("10.12.0.9"), EthAddr("00:00:12:00:00:09"), True, False, 1))
        return honeypots

    def listHoneyRouters(self):
        honeyrouters = []
        honeyrouters.append(Node(IPAddr("10.11.0.0"), EthAddr("00:00:01:11:00:00"), False, True, 1))
        honeyrouters.append(Node(IPAddr("10.12.0.0"), EthAddr("00:00:01:12:00:00"), False, True, 1))
        return honeyrouters