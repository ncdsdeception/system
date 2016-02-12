from GeneratorVirtualView import GenerateVirtualView

RealHosts={}
RealHosts[1]="10.0.0.1/00:00:00:00:00:01"
RealHosts[2]="10.0.0.2/00:00:00:00:00:02"
RealHosts[3]="10.0.0.3/00:00:00:00:00:03"
RealHosts[4]="10.0.0.4/00:00:00:00:00:04"
RealHosts[5]="10.0.0.5/00:00:00:00:00:05"
RealHosts[6]="10.0.0.6/00:00:00:00:00:06"
RealHosts[7]="10.0.0.7/00:00:00:00:00:07"
RealHosts[8]="10.0.0.8/00:00:00:00:00:08"
RealHosts[9]="10.0.0.9/00:00:00:00:00:09"
RealHosts[10]="10.0.0.10/00:00:00:00:00:0a"
RealHosts[11]="10.0.0.11/00:00:00:00:00:0b"
RealHosts[12]="10.0.0.12/00:00:00:00:00:0c"

SubnetSpace="10.0.1"

TargetPort=2
NCDSPort=1
HoneyPotPort=5
NumberSubnets=3
MinNumHoneyPotsInSubnet=10
MaxNumHoneyPotsInSubnet=15
MaxSubnets=48
MaxHosts=255
#Strategy="minhop_maxsub"
Strategy="maxhop_maxsub"

GenView = GenerateVirtualView(MaxSubnets,MaxHosts)
(realhosts, target) = GenView.generatgeView(RealHosts,SubnetSpace,TargetPort,NCDSPort,HoneyPotPort,NumberSubnets,MinNumHoneyPotsInSubnet,MaxNumHoneyPotsInSubnet,Strategy)
