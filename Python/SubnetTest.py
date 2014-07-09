from Tkinter import *
from subnets import *
from random import randint

root = Tk()
root.title("            Subnet Test")
root.minsize(430, 300)
root.maxsize(430, 300)

#Static label creation
Label(root, text="Device Address").grid(column = 1, row = 0, columnspan = 20, pady=(10, 5))
Label(root, text="CIDR Mask").grid(column=16, row=1, padx = 5, columnspan = 4)
instrText = "Given the above address, figure out and enter the network (lowest)"
instrText2 = "and broadcast (highest) addresses in the subnet"
Label(root, text=instrText).grid(column=0, row=3, columnspan=20)
Label(root, text=instrText2).grid(column=0, row=4, columnspan=20)
Label(root, text="Network Address").grid(column = 1, row = 5, columnspan = 20, pady=(5, 3))
Label(root, text="Broadcast Address").grid(column = 1, row = 8, columnspan = 20, pady=(3, 3))

#Iterating over repetetive label creation
octetNames = ("Octet One", "Octet Two", "Octet Three", "Octet Four")
columnLoc = 0
for x in octetNames:
    Label(root, text=x).grid(column=columnLoc, row=1, padx=5, columnspan=4)
    columnLoc += 4

columnLoc = 0
for x in octetNames:
    Label(root, text=x).grid(column=columnLoc, row=6, padx = 5, columnspan = 5)
    Label(root, text=x).grid(column=columnLoc, row=9, padx = 5, columnspan = 5)
    columnLoc += 5

#Generating the test address
aOneOOneV, aOneOTwoV, aOneOThrV, aOneOFouV, aOneSubMaskV = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
def genSubnet():
    for x in (aOneOOneV, aOneOTwoV, aOneOThrV, aOneOFouV):
        x.set(randint(0, 255))

genSubnet()
aOneSubMaskV.set(randint(1, 32))
#Creating test address labels  
x = {'column': 0, 'row': 2, 'columnspan': 4}
aOneOOne = Label(root, textvariable=aOneOOneV)
aOneOTwo = Label(root, textvariable=aOneOTwoV)
aOneOThr = Label(root, textvariable=aOneOThrV)
aOneOFou = Label(root, textvariable=aOneOFouV)
aOneSubMask = Label(root, textvariable=aOneSubMaskV)
aOneSubMask.grid(column=16, row=2, columnspan = 4)
for y in (aOneOOne, aOneOTwo, aOneOThr, aOneOFou):
    y.grid(x)
    x['column'] += 4

#Creating low address entry fields
addTwoOctOne = Entry(root, width=5)
addTwoOctTwo = Entry(root, width=5)
addTwoOctThree = Entry(root, width=5)
addTwoOctFour = Entry(root, width=5)
lowAddress = (addTwoOctOne, addTwoOctTwo, addTwoOctThree, addTwoOctFour)
x = {'column': 0, 'row': 7, 'columnspan': 5}
for y in (lowAddress):
    y.grid(x)
    x['column'] += 5

#Creating high address entry fields
addThrOctOne = Entry(root, width=5)
addThrOctTwo = Entry(root, width=5)
addThrOctThree = Entry(root, width=5)
addThrOctFour = Entry(root, width=5)
highAddress = (addThrOctOne, addThrOctTwo, addThrOctThree, addThrOctFour)
x = {'column': 0, 'row': 10, 'columnspan': 5}
for y in highAddress:
    y.grid(x)
    x['column'] += 5

def doItAgain(): #Clearing text fields and killing the popup
    genSubnet()
    aOneSubMaskV.set(randint(1, 32))
    for x in lowAddress:
        x.delete(0, END)
    for x in highAddress:
        x.delete(0, END)
    toplevel.destroy()

def popupWindow(): #Generating a popup with win / loss text
    global toplevel
    toplevel = Toplevel()
    if matchAddress() == True:
        Label(toplevel, text="Good jorb").grid(column=0, row=0)
        buttonWin = Button(toplevel, text="A winner is you", command=doItAgain)
        buttonWin.grid(column=0, row=1)
    else:
        Label(toplevel, text="You're bad at this").grid(column=0, row=0)
        buttonLose = Button(toplevel, text="Try an easier one", command=doItAgain)
        buttonLose.grid(column=0, row=1)
    mainloop()

def matchAddress(): #Testing user entries against external function
    userLow = '.'.join((str(addTwoOctOne.get()), str(addTwoOctTwo.get()), str(addTwoOctThree.get()), str(addTwoOctFour.get())))
    userHigh = '.'.join((str(addThrOctOne.get()), str(addThrOctTwo.get()), str(addThrOctThree.get()), str(addThrOctFour.get())))
    testAdd = ', '.join((str(aOneOOne.cget("text")), str(aOneOTwo.cget("text")), str(aOneOThr.cget("text")), str(aOneOFou.cget("text"))))
    subnetRange = printSubnetRange(aOneOOne.cget("text"), aOneOTwo.cget("text"), \
                  aOneOThr.cget("text"), aOneOFou.cget("text"), aOneSubMask.cget("text"))
    if userLow == subnetRange[0] and userHigh == subnetRange[1]:
        return True
    else:
        return False

buttonOne = Button(root, text="Check your answers", command=popupWindow)
buttonOne.grid(column=7, row=11, columnspan=6)
root.mainloop()
