s =input()
s= s.title()
s=s.lower()
for i in s:
    if (i<'a' or i>'z') and i!=' ':
        s = s.replace(i, "")
s= s.replace("  ",' ')
s.strip()
lst = s.split(" ")
Name =""
for x in lst:
    if x != lst[-1]:
        Name = Name + x[0]
Name= Name +'.'+lst[-1]
print(Name)
