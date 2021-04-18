
s =input()
s= s.title()
s.replace(".",'')
s.strip()
lst = s.split(" ")
Name =""
for i in lst:
    if i!= lst[-1]:
        Name=Name+i[0]
Name= Name +'.'+lst[-1]
print(Name)