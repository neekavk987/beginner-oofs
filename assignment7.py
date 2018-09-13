n=open("python_assignment7_data.txt","r+")
name_list=[]
for x in range (0,13):
    item=n.readline()
    item=item.rstrip()
    if item not in name_list:
     name_list.append(item)
print(name_list)
    
    
    
   
    
