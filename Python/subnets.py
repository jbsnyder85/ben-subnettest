import sys

def validateIP(octetOne, octetTwo, octetThree, octetFour):
    addrArray = []
    for x in (octetOne, octetTwo, octetThree, octetFour):
        if type(x) == int and (-1 < x < 256):
            addrArray.append(str(x))
        else:
            return 0
    return 1

def octetMath(octetIP, octetNum, subnetMask):
    subnetArray = []
    if (float(subnetMask) / float(octetNum)) > 8:                               #If this octet is inside the mask, return the octet as-is
        subnetArray.append(octetIP)
        subnetArray.append(octetIP)
        return subnetArray
    else:
        if (subnetMask - (8 * (octetNum-1))) <= 0:                              #If this octet is partially or completely outside the mask
        #not (subnetMask - (8 * octetNum)) % 8 or                               #Completely outside, return the full range
            subnetArray.append(0)
            subnetArray.append(255)
            return subnetArray
        else:
            ipNums = (2**(((8*octetNum)-subnetMask)%8))                         #2 to the power of the masked bits gives us a range
            subnetArray.append(ipNums * (octetIP / ipNums))                     #Int division to give us a low number
            subnetArray.append(ipNums * (octetIP / ipNums) + (ipNums - 1))      #Low number plus range for the high number
            return subnetArray


def printSubnetRange(octetOne, octetTwo, octetThree, octetFour, subnetMask):
    highArray = ['','','','']
    lowArray = ['','','','']
    if validateIP(octetOne, octetTwo, octetThree, octetFour):
        lowArray[0], highArray[0] = octetMath(octetOne, 1, subnetMask)
        lowArray[1], highArray[1] = octetMath(octetTwo, 2, subnetMask)
        lowArray[2], highArray[2] = octetMath(octetThree, 3, subnetMask)
        lowArray[3], highArray[3] = octetMath(octetFour, 4, subnetMask)
        lowNum =  str(lowArray[0]) + '.' + str(lowArray[1]) + '.' + str(lowArray[2]) + '.' + str(lowArray[3])
        highNum =  str(highArray[0]) + '.' + str(highArray[1]) + '.' + str(highArray[2]) + '.' + str(highArray[3])
        return [lowNum, highNum]
    else:
        return "One of your octets is invalid"
