
class Node(object):

    def __init__(self,shortName=None,ip_addr=None,decepted_ip_addr=None,eth_addr=None,decepted_eth_addr=None,isHoneypot=False,isRouter=False,switchPort=0):
        self.shortName = shortName
        self.ip_addr = ip_addr
        self.decepted_ip_addr = decepted_ip_addr
        self.eth_addr = eth_addr
        self.decepted_eth_addr = decepted_eth_addr
        self.switchPort = switchPort
        self.isHoneypot = isHoneypot
        self.isRouter = isRouter