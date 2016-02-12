import pickle as Pickle
from Node import Node


class Policy(object):

    def __init__(self):
        self.nodes = self.readNodes()

    def updateNode(self,node):
        index=0
        for n in self.nodes:
            if node.eth_addr == n.eth_addr:
                self.nodes[index] = node
            index+=1

    def getNode(self,eth_addr):
        for n in self.nodes:
            if n.eth_addr == eth_addr:
                return n

    def specifyAccessPolicy(self):
        hosts = []
        honeypots = []
        honeyrouters = []

        for n in self.nodes:
            if n.isHoneypot:
                honeypots.append(n)
            elif n.isHoneyRouter:
                honeyrouters.append(n)
            else:
                hosts.append(n)

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
        hosts = []
        honeypots = []
        honeyrouters = []

        for n in self.nodes:
            if n.isHoneypot:
                honeypots.append(n)
            elif n.isHoneyRouter:
                honeyrouters.append(n)
            else:
                hosts.append(n)

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

        routes[hosts[1].ip_addr + "-" + honeypots[3].ip_addr] = routes_2
        routes[hosts[2].ip_addr + "-" + honeypots[4].ip_addr] = routes_3
        return routes

    def readNodes(self):
        nodes = []
        input = open('policy.pkl', 'rb')
        nodes = Pickle.load(input)
        print(nodes[2].ip_addr)
        return nodes

        '''
        nodes.append(Node("10.0.0.1", "00:00:00:00:00:01", False, False, 1))
        nodes.append(Node("10.0.0.2", "00:00:00:00:00:02", False, False, 2))
        nodes.append(Node("10.0.0.3", "00:00:00:00:00:03", False, False, 3))
        nodes.append(Node("10.0.0.5", "00:00:00:00:00:05", True, False, 1))
        nodes.append(Node("10.0.0.6", "00:00:00:00:00:06", True, False, 1))
        nodes.append(Node("10.0.0.7", "00:00:00:00:00:07", True, False, 1))
        nodes.append(Node("10.11.0.8", "00:00:11:00:00:08", True, False, 1))
        nodes.append(Node("10.12.0.9", "00:00:12:00:00:09", True, False, 1))
        nodes.append(Node("10.11.0.0", "00:00:01:11:00:00", False, True, 1))
        nodes.append(Node("10.12.0.0", "00:00:01:12:00:00", False, True, 1))
        '''