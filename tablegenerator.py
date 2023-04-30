while True: 
           d=int(input("enter which table you want : "))
           print("\n table of "+str(d)+" is : \n")
           for m in range(10):
                       
                       print(str(d)+" x "+str(m+1)+" = "+str((m+1)*d)+"\n") 
                     
                     
           n=input("do you want to exit (y/n) : ")
           if n =="y":
                    break
           else:
                 print("="*70+"\n")
       