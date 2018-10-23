#!/usr/bin/python
theNumber = 20
theRoot =4.0
percent =4.47
diff = 0.5 
while ( abs(diff) > 0.0001):
	theRoot = (theRoot + (theNumber/theRoot))/2
	#theRoot = theRoot +  0.001 
	diff = theNumber - (theRoot * theRoot) 
	print "theroot:diff:" + str(theRoot) +":" + str(diff)
print "theroot:diff:" + str(theRoot) +":" + str(diff)
   





