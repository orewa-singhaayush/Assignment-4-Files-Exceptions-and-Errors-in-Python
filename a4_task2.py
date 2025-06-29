def output():
    try:
        inital=input("Enter the text you want to enter")
        with open ("output.txt",'w') as f:
            f.write(initial +"\n")
        
        additional=input("Enter the additional text you want to add")
        with open ("output.txt",'a') as f:
            f.write(additional + "\n")
         with open ("output.txt",'r') as f :
             final=file.read()
             print("Final content of output.txt :",final)
         
          
          
          