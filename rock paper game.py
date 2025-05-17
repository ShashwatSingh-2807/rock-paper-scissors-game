import random 
choices = ["rock","paper","scissors"]
print(choices)
userpoint=0
comppoint=0
en=0
while(en==0):
    user=input("enter your choice").lower()
    com=random.choice(choices)
    if(user=="rock" and com=="paper"):
        comppoint+=1
        print("comp choses",com)
    elif(user=="paper" and com=="scissors"):
        comppoint+=1
        print("comp choses",com)
    elif(user=="scissors" and com=="rock"):
        comppoint+=1
        print("comp choses",com,)
    elif(user==com):
        print("comp chooses",com,"draw")
    else:
        print("computer chosses",com)
        userpoint+=1
    en=int(input("enter1 to exit 0 to continue"))
print("your point=",userpoint)
print("comp point=",comppoint)







 


















    










      





