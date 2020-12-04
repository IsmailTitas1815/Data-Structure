def rpower(num,idx):
    if(idx==1):
       return(num)
    else:
       return(num*rpower(num,idx-1))
base=int(input("Enter number: "))
exp=int(input("Enter index: "))
rpow=rpower(base,exp)
print("{} raised to {}: {}".format(base,exp,rpow))