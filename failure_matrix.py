#!/usr/bin/python
def has_consecutive_failures(threshold,events):
        status = "No Status"
        array =[[2,["failure", "success", "failure"],"false" ],
		[2,["failure", "success", "failure", "failure"],"true"],
                [3,["failure", "success", "failure", "failure"],"false"]
               ]
        for incident in array:
		#print (incident)
		thresh_lookup 	= incident[0]
		even_lookup	= incident[1]
                status_lookup	= incident[2]
		#print(thresh_lookup)
		#print(even_lookup)
		#print(status_lookup)
		if threshold == thresh_lookup and events == even_lookup:
			status = status_lookup
			break

	
        return status

print(has_consecutive_failures(2, ["failure", "success", "failure"]))
print(has_consecutive_failures(2, ["failure", "success", "failure", "failure"]))
print(has_consecutive_failures(3, ["failure", "success", "failure", "failure"]))
