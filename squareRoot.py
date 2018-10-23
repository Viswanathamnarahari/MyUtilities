#!/usr/bin/python
#
#	Calculate root of a number without using sqr root function.
#	Name:squareRoot
#

#theNumber = 20
def	sqrRoot(theNumber):
        diff = 0.5
	theRoot =1.0
	while ( abs(diff) > 0.0001):
		theRoot = (theRoot + (theNumber/theRoot))/2
		#theRoot = theRoot +  0.001 
		diff = theNumber - (theRoot * theRoot) 
	#print "theroot:diff:" + str(theRoot) +":" + str(diff)
	return theRoot
   
print "Enter a number:",
x= input()
theNumber = int(x)
print (sqrRoot(theNumber))






