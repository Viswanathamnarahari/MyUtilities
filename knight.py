#!/usr/bin/python
#version information
#All notes are related to startFrom(00)
#1. Stops after 46 hops with message dead end reached at curRC: 71

NOHOP      = 80  #No Hop to this point
EMPTY      = 81  #Not occupied point


#BOARD      = [EMPTY] * 64
              #0  1  2  3  4  5  6  7
BOARD      = [81,81,81,81,81,81,81,81, #0
              81,81,81,81,81,81,81,81, #1 
              81,81,81,81,81,81,81,81, #2
              81,81,81,81,81,81,81,81, #3
              81,81,81,81,81,81,81,81, #4
              81,81,81,81,81,81,81,81, #5
              81,81,81,81,81,81,81,81, #6
              81,81,81,81,81,81,81,81] #7
              
previousRC = NOHOP
currentRC  = 00
nextRC8    = [NOHOP] * 8
nextRC512  = [NOHOP] * 512
stackRC    = []
hopsRC     = []

def next8HopRC(cell):
    #For current cell calculate 8 hops
    #update nextRC512 array with corresponding hops

    nextRC8     = [NOHOP] * 8
    #get Row and Column 
    Row = cell // 8
    Col = cell %  8
    
    Rm2 = Row - 2
    Rm1 = Row - 1
    Rp1 = Row + 1
    Rp2 = Row + 2

    Cm2 = Col - 2
    Cm1 = Col - 1
    Cp1 = Col + 1
    Cp2 = Col + 2

    if ( (Rm2 >= 0 ) and ( Cm1 >= 0)) :
      nextRC8[0] = packRC(Rm2,Cm1)

    if ( (Rm2 >= 0 ) and ( Cp1 <= 7)) :
      nextRC8[1] = packRC(Rm2,Cp1)

    if ( (Rm1 >= 0 ) and ( Cm2 >= 0)) :
      nextRC8[2] = packRC(Rm1,Cm2)

    if ( (Rm1 >= 0 ) and ( Cp2 <= 7)) :
      nextRC8[3] = packRC(Rm1,Cp2)

    if ( (Rp1 <= 7 ) and ( Cm2 >= 0)) :
      nextRC8[4] = packRC(Rp1,Cm2)

    if ( (Rp1 <= 7 ) and ( Cp2 <= 7)) :
      nextRC8[5] = packRC(Rp1,Cp2)

    if ( (Rp2 <= 7 ) and ( Cm1 >= 0)) :
      nextRC8[6] = packRC(Rp2,Cm1)

    if ( (Rp2 <= 7 ) and ( Cp1 <= 7)) :
      nextRC8[7] = packRC(Rp2,Cp1)

    #update nextRC512 with the date we got in nextRC8
    for i in range (8):
      #nextRC512[cell + i] = nextRC8[i]
      nextRC512[(cell * 8) + i] = nextRC8[i]

    return nextRC8 
    
def packRC(row,col):
      return ( (row * 10) + col )    


def calcNextHopRC():
    #Initialize 64 X 8 locations to NOHOP
    for i in range(64):
      print CellToRC(i), next8HopRC(i),
      #for j in range(8):
      #  print nextRC512[i +j],
      print ""
      

def initialize():
      print "Initializing"
      calcNextHopRC()


def convertToString(digit):
    if digit <= 7:
      return "0"+str(digit)
    else:
      highDigit = digit // 10
      lowDigit  = digit % 10
      return str(highDigit) + str(lowDigit)
def cellHoppable(RowCol):
      # Check if it is NOHOP(out of boundary) or not touched or EMPTY ( in previous hops)
      if ((RowCol == NOHOP) or (BOARD[RCtoCell(RowCol)] != EMPTY)):
        return False
      else:
        return True

def nextHopRCs(RowCol):
      #mcell = RCtoCell(RowCol)
      mcell = RCtoCell(RowCol) * 8
      nextHops = []
      for i in range(8):
        if cellHoppable(nextRC512[mcell + i]):
          nextHops.append(nextRC512[mcell + i])
      return nextHops
      
def RCtoCell(RowCol):
      return (((RowCol // 10) *8 ) + (RowCol % 10))
def CellToRC(cell):
      row = cell // 8
      col = cell  % 8
      return (row * 10)+col

def displayBoard():
  print "     0  1  2  3  4  5  6  7"
  for r in range(8):
    print r," ",
    for c in range(8):
      print convertToString(BOARD[(r*8)+c]),
      #print r,c,
      #sys.stdout.flush()
    print " "
def displaynextRC512():
      print nextRC512
      print len(nextRC512)
def hopF(curRC,nextRC):
      print "hopF executing with :", curRC,nextRC
      BOARD[RCtoCell(curRC)] = nextRC
      #displayBoard()
def StartFrom(curRC):
    #HopBK : Hop back two steps. Effects entries in stackRC. curRC changes. Arises when no nextRC available
    #HopBH : curRC remains same. nextRC changes
    UseNewNextHopRCs = True

    while (len(stackRC)/2 <= 63):
      if UseNewNextHopRCs:
        curHops = nextHopRCs(curRC)
        print "curRC:",curRC,curHops,"Got fresh possible hops for ",curRC

      UseNewNextHopRCs = True   

      curHopsLen = len(curHops)
      if curHopsLen >=1:    #check if we can do atleast one hop from curRC
         stackRC.append(curRC)
         stackRC.append(curHops)
         hopsRC.append(curRC)
         ##print "hopsRC:", len(hopsRC),":",hopsRC
         ##print "stackRC:", len(stackRC),":",stackRC
         #
         nextRC = curHops[curHopsLen-1]
         hopF(curRC,nextRC)
         curRC = nextRC
      else:
         #dead end reached. prepare for hop back from CurRC
         print "hopsRC:", len(hopsRC),":",hopsRC
         UseNewNextHopRCs = False
         print "No hops available from curRC:",curRC,"Trying to hop back"
          
         NotFoundTwoRC = True
         
         while  NotFoundTwoRC:
          
          preRC = hopsRC.pop()
          BOARD[RCtoCell(preRC)] = EMPTY
          
          curHops = stackRC.pop()
          curRC   = stackRC.pop()
          
          if len(curHops) == 1 :
             print "Ignoring recent single hop possibilityi", curRC, "-->", curHops 
             NotFoundTwoRC = True    #Continue while NotFoundTwoRC loop
          else :                     
             #We have more than two possible hops
             curHops.pop()           #Take out one possible RC
             curRC = curRC           #Just for clarity, otherwise it is already done above. 
           
             NotFoundTwoRC  = False

initialize()
displayBoard()
#displaynextRC512()
#print "00",nextHopRCs(00)
#Iteration starts here.
curRC = 00
StartFrom(00)
print "All done!"
