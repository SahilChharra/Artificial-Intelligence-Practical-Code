start = [[1,2,3],
          [4,5,6],
          [0,7,8]]
goal = [[1,2,3],
         [4,5,6],
         [7,8,0]]

print(start)
print(goal)

def h_calculate(s,g):
    count=0
    for i in range(3):
        for j in range(3):
            if(s[i][j]!=0):
                if(s[i][j]!=g[i][j]):
                    count+=1               
    return count

def f_calculate(h,g):
    fe=g+h
    return fe

def move(s,g,h):
    print(s)
    for i in range(3):
        for j in range(3):
            if(s[i][j]==0):
                x, y=i, j
                break
    
    if(x==0):
        if(y==0):
            s[x][y]=s[x+1][y]
            s[x+1][y]=0
            g=g+1
            he = h_calculate(s,goal)
            print(he,h)
            if(he>h):
                s[x+1][y]=s[x][y]
                s[x][y]=0
                g=g-1
                
    if(x==2):
        if(y==0):
            s[x][y]=s[x][y+1]
            s[x][y+1]=0
            g=g+1
            he=h_calculate(s,goal)
            print(he,h)
            print(s)
            if(he>h):
                s[x][y+1]=s[x][y]
                s[x][y]=0
                g=g-1
        
        if(y==1):
            s[x][y]=s[x][y+1]
            s[x][y+1]=0
            g=g+1
            he=h_calculate(s,goal)
            print(he,h)
            print(s)
            if(he>h):
                s[x][y+1]=s[x][y]
                s[x][y]=0
                g=g-1

               
g=0                                            
h=h_calculate(start,goal)
f=f_calculate(h,g)
print(h)
print(f)

while(start!=goal):
    move(start,g)