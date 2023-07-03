r, b = map(int,input().split())
total = r + b                       
i = 3                            
while True:                      
    if total % i == 0:           
        if (i - 2) * (total // i - 2) == b:    
            print(max(i, total // i), min(i, total // i))
            break
    i += 1