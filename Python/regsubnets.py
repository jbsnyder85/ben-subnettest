import re
import subnets

class ipAddr(object):
    
    def __init__(self, inputAddr, subMask):
        p = re.compile('(\d{1,3}\.)(\d{1,3}\.)(\d{1,3}\.)(\d{1,3})')
        self.octetOne = int(p.match(inputAddr).group(1).replace('.', ''))
        self.octetTwo = int(p.match(inputAddr).group(2).replace('.', ''))
        self.octetThree = int(p.match(inputAddr).group(3).replace('.', ''))
        self.octetFour = int(p.match(inputAddr).group(4))
        self.subMask = int(subMask)

    def getRange(self):
        self.octetOneLow, self.octetOneHigh = subnets.octetMath(self.octetOne, 1, self.subMask)
        self.octetTwoLow, self.octetTwoHigh = subnets.octetMath(self.octetTwo, 2, self.subMask)
        self.octetThreeLow, self.octetThreeHigh = subnets.octetMath(self.octetThree, 3, self.subMask)
        self.octetFourLow, self.octetFourHigh = subnets.octetMath(self.octetFour, 4, self.subMask)
        return (self.octetOneLow, self.octetTwoLow, self.octetThreeLow, self.octetFourLow), (self.octetOneHigh, self.octetTwoHigh, self.octetThreeHigh, self.octetFourHigh)
