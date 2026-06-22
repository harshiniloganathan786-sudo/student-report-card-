mn= input("Enter the name of the movie you wish to watch:")
nt=int(input("Enter the number of tickets you wish to purchase:"))
age= int(input("Enter your age:"))
s=input("What snacks would you like to purchase?(coke\popcorn\combo)")
tc=200
bc=tc*nt
sc=0
c=0
if age<18:
   c=bc*1/5
   bc=bc-c
   if nt>=5:
       bc-=100
       c+=100
if age>18:
    if nt>=5:
        bc-=100
        c+=100
if s=="coke":
    sc+=80
if s=="popcorn":
    sc+=150
if s=="combo":
    sc+=200
fa=bc+sc
print("-------------RECEIPT-----------------")
print(f"movie:{mn}")
print("tickets:",nt)
print("base cost:",bc)
print("snack cost:",sc)
print("discount:",c)
print("final cost:",fa)
print("-------------------------------------")

  


