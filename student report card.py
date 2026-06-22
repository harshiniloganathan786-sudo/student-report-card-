input("Name of the student:")
e =int(input("English marks:"))
cs =int(input("CS marks:"))
m =int(input("Mathematics marks:"))
p=int(input("Physics marks:"))
c =int(input("Chemistry marks:"))
L=[e,cs,m,p,c]
Total=sum(L)
Avg=Total/5
Grade=0
if Avg>=90.0 :
      Grade= "A" 
if Avg >=75.0 and Avg<=90.0:
      Grade= "B"
if Avg>=50.0 and Avg<=75.0:
      Grade= "C" 
if Avg < 50.0:
       Grade= "Fail" 
print("----------REPORT CARD----------")  
print(Total)
print(Avg)
print(Grade)
print("Highest mark:",max(L))
print("Lowest mark:",min(L))
print("-------------------------------")



