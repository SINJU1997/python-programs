#Write a Python script to concatenate the following dictionaries to create a new one.
dt1={'A': 15, 'B': 10, 'C' : 12 }  
dt2={'E': 18,'B': 20,'D' : 16 } 
dt1.update(dt2)
print("Updated dict is %s" % dt1)
