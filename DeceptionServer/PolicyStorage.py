import pickle as Pickle
from Node import Node

class PolicyStorage(object):

    def writeNodes(self):
        output = open('policy.pkl', 'wb')
        Pickle.dump(self.listNodes(), output, Pickle.HIGHEST_PROTOCOL)

        #output = open('policy.pkl', 'rb')
        #n2 = Pickle.load(output)
        #print(n2.ip_addr)


    def listNodes(self):
        nodes = []
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
        return nodes