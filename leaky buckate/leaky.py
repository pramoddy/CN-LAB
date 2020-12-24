size=int(input("Enter the size of bucket : "))
output_rate=int(input("Enter the output rate : "))
num=int(input("Enter the number of packate : "))
for v in range(0,num):
    packate_size=int(input("Enter the packete size : "))
    if packate_size >= size:
        print("the buckate is full")
    elif ((packate_size<=size) and (packate_size<=output_rate)):
        print("Buckate output sucessful!....")
        print("last byte sent:")
        print(packate_size)
    else:
        print("buckate output succesfull")
        print("Bytes outputted")
        print(output_rate)
        print("last byte sent")
        print(packate_size-output_rate)
        

    
    
    
