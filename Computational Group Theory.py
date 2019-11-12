#Evan Walker

G = [[2,0,1],
     [0,1,2],
     [1,2,0]]  #should be a group
Z = [[0,1,2,3,4,5],
     [1,2,0,5,3,4],
     [2,0,1,4,5,3],
     [3,5,4,0,1,2],
     [4,3,5,2,0,1],
     [5,4,3,1,2,0]]  #should not be a group due to associativity (3*1)*3 != 3*(1*3)
X = [[0,1,2,3,4],
     [1,2,3,4,0],
     [2,3,4,0,1],
     [3,4,0,1,2],
     [4,0,1,2,3]]  #should be a group
Y = [[2,0,1,3],
     [0,1,2,3],
     [1,2,3,0],
     [3,3,0,2]]  #should return not a group because the element 3 appears twice in a row and in a col, which means inverses are not unique and therefore not a group
X2 = [[1,1,2,3,4],
     [1,2,3,4,0],
     [2,3,4,0,1],
     [3,4,0,1,2],
     [4,0,1,2,3]]  #should be not be a group because of inverse and idnetity
K = [[0,1,2,3],
     [1,0,3,2],
     [2,3,0,1],
     [3,2,1,0]]    #should be a group
H = [0,1,2]
L = [0,1]
M = [[1,2,3,4],
     [2,4,1,3],
     [3,1,4,2],
     [4,3,2,1]]

#example of two dimm array and small method
def is_commutative(G):
    n = len(G)
    return all(G[x][y] == G[y][x] for x in range(n) for y in range(n))





def create_Zgroup(m): # m is the modulus
    G = []
    for n in range(m):
        G.append(n%m)
    #print(G)
    return G

F = create_Zgroup(172)
#M = create_Zgroup(39)

def create_Zsubgroup(G,n,m): # n is the elemnt to generate subgroup, m is the modulus
    S = []
    for z in range(len(G)):
        if((n*z)%m not in S):
            S.append((n*z)%m)
    print("<",n,"> =",S)
    print()
    #if(S != G and len(S) != 1):
      #  print()
    #print(S)
    return S


#create_Zsubgroup(M,3,39)
def find_sizesmallsubgroup(G,n,m,z): #n,m are elements that should be in subgroup, z is the modulu
    L = []
    x = 1
    while x <= len(G):
        S = create_Zsubgroup(G,x,z)
        print(S)
        print()
        if(n in S and m in S):
            L.append(len(S))  # needs to be smaller than every other length of S, so it is incorrect until it can compare each value
        x = x + 1
    """z = 1
    while z != 0:
        for y in range(len(L)):
            if(L[y] < L[0]):
                a = L[0]
                L[0] = L[y]
                L[y] = L[0]
        for x in range(len(L)):
            if()"""

def find_othersubgroup(G,n,m): # n is the element which generates a subgroup and m is the modulus
    S = create_Zsubgroup(G,n,m)
    for x in range(len(G)):
        if(x != n):
            V = create_Zsubgroup(G,x,m)
            if(V == S):
                print(x)
                print()
           
def find_Zorder(n,m): #n = element, m is the modulus
    x = 1
    while x <= m:
        if((n*x)%m == 0):
            return x
        x = x + 1



def find_Uorder(n,m): #n = element, m is the modulus
    x = 1
    while x <= m:
        if((n**x)%m == 1):
            print("element " , n, " has order " , x)
            return x;
        x = x + 1
def find_allorder(n,m):
    x=n
    while x < m:
        #if(find_Zorder(x,m) == m):
        print("element " , x, " has order " , find_Zorder(x,m))
        x=x+1
def printall_subgroups(G,m):
    for x in range(len(G)):
        create_Zsubgroup(G,x,m)

#find_allorder(0,22)
#printall_subgroups(F,77)
#find_Uorder(9,10)
#find_Uorder(38,81)
#find_Uorder(49,81)
#find_othersubgroup(M,1,77)
    
#print(find_sizesmallsubgroup(F,116,112,172))
#print(find_sizesmallsubgroup(M,2,4,5))






def print_group(G):  #for neatness and readability in the print
    n = len(G)
    print("(Maybe)Group = ")
    for x in range(n):
        for y in range(n):
            print(G[x][y], end=" ")
        print()
    print()

#part a)
def is_group(G):
    print("___________________________________GROUP TEST___________________________________")
    print_group(G)
    e = find_identity(G)
    if(e == None):
        print("This is not a group because it has no identity")
        print()
        return False
    print("Group Identity e = ", e)
    if(check_inverses(G,e) and is_associative(G)):
        print("This is a Group")
        print()
        return True
    else:
        print("This is not a group")
        print()
        return False
        
        
        
def find_identity(G):
    n = len(G)
    m = 0
    for x in range(n):
        for y in range(n):
            if (G[x][y] == y and G[y][x] == y):
                print("x = ", x)
                print("y = ", y)
                m = m + 1
            else:
                m = 0
            if (m == n):
                return x
    return None

def check_inverses(G,e):
    n = len(G)
    count = 0
    for x in range(n):
        for y in range(n):
            if (G[x][y] ==  e and G[y][x] == e):
                print(x , " is an inverse of " , y)
                count = count + 1
    if(count == n): #there must be an identity element in each row/col because every inverse element is unique, therefore the # of inverses found(count) must equal the # of rows/cols
        print("all elements have inverses")
        return True
    else:
        print("not all elements have inverses")
        return False
                
def is_associative(G):
    n = len(G)
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if(G[G[x][y]][z] != G[x][G[y][z]]):
                    print("This group is not associative because")
                    print( "(",x,"op",y,")op",z," != ",x,"op(",y,"op",z,")")
                    print("where op is the operation under the group")
                    return False
    print("This group is associative")
    return True

#part b)
def is_subgroup(H,G):
    print("_________________________________SUBGROUP TEST________________________________")
    
    n = len(G)
    m = len(H)
    if(is_group(G) == False):
        print("This is not a group in the first place, therefore the subgroup is not a subgroup")
        return False
    print("(Maybe)Subgroup = ")
    print(H)
    e = has_identity(H,G)
    if(m > n):
        print("the sugroup is larger than the group itself and therefore is not a subgroup")
        return False
    if(e == None):
        print("H has no identity, therefore is not a group in the first place")
        return False
    if(is_closed(H,G) == False):
        print("H is not a subgroup because of closure")
        return False
    if(has_inverses(H,G,e) == False):
        print("not every element has an inverse, therefore not a subgroup")
        return False
    print("This is a subgroup, lucky you")
    print()
    return True
    
def has_identity(H,G):
    n = len(H)
    count  = 0
    for x in range(n):
        for y in range(n):
            if (G[H[x]][H[y]] == H[y] and G[H[y]][H[x]] == H[y]):
                count = count + 1
            else:
                count = 0
            if (count == n):
                print("Subgroup Identity e = ", H[x])
                return H[x]
    return None

def is_closed(H,G):
    n = len(H)
    count = 0
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if(G[H[x]][H[y]] not in H):  # checking closure of H
                    return False
    print("the subgroup is closed under the operation")
    return True

def has_inverses(H,G,e):
    n = len(H)
    count  = 0
    for x in range(n):
        for y in range(n):
            if (G[H[x]][H[y]] == e and G[H[y]][H[x]] == e):
                print(H[x] , " is an inverse of " , H[y])
                count = count + 1
    if(count == n):
        print("every element has an inverse")
        return True
    else:
        return False
    
    
is_group(M)













    
