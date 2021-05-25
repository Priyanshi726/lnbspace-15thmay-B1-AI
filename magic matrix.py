def MagicMatrix(n): 
    
    Matrix = [[0 for x in range(n)] for y in range(n)]    
    p = n / 2
    b = n - 1
    num = 1
    while num <= (n * n): 
        if p == -1 and b == n:  
            p = 0
            b = n - 2
            
        else:                     
            if p < 0:
                p = n - 1
            if b == n:
                b = 0
                
        if Matrix[int(p)][int(b)]:
            p = p + 1
            b = b - 2
            continue
        
        else: 
            Matrix[int(p)][int(b)] = num 
            num = num + 1
            p = p - 1
            b = b + 1

            
    print ("Sum of each row or column: ",n * (n * n + 1)/2, "\n") 
    for i in range(0, n): 
        for j in range(0, n): 
            print('%2d ' % (Matrix[i][j]),end = '') 
             
            if j == n - 1:  
                print()
            

n=int(input("Number of rows of the Magic Matrix: "))
MagicMatrix(n)
           
