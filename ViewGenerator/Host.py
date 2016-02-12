
class Host(object):

    def __init__(self,name,ip,mac,port):
        self.shortName=name
        self.realIP=ip
        self.macaddress=mac
        self.portNum=port
        self.deceptiveIP=""
        self.distance=0


    def setDecIPAddr(self,decIP):
        self.deceptiveIP=decIP