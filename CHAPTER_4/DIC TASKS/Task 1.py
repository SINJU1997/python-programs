#Write a Python script to sort (ascending and descending) a dictionary by value.
numdt = {"a":86,"b":2,"c":78,"d":1}

sorted_dt = {key: value for key, value in sorted(numdt.items(), key=lambda item: item[1])}

print("Sorted dic (ascending) is %s" %sorted_dt )
