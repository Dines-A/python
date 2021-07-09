# ALL OF THIS DID BY MY OWN 

""" # # # # # 
    # # # # # 
    # # # # # 
    # # # # # 
    # # # # #     """  
for r in range(1,6):
    for i in range(1,6):
        print("#",end=" ")
    print("")

""" # 
    # # 
    # # # 
    # # # # 
    # # # # #      """
for r in range(1,6):
    for i in range(r):
        print("#",end=" ")
    print("")



""" # # # # # 
    # # # # 
    # # #  
    # # 
    #            """ 

for r in range(1,6):
    for i in range(r,6):
        print("#",end=" ")
    print("")


""" 1 2 3 4
    2 3 4
    3 4
    4            """
for i in range(1,4+1):
    for j in range(i,4+1):
        print(j,end=" ")
    print() 

""" A P Q R
    A B Q R
    A B C R
    A B C D 
A='ABCD'
B='PQR'
for r in range(0,5):
    for j in range(0,4):
        print(A[:r]+B[j:],end=" ")
    print()

"""
"""  
source : telusco comment     
str1='ABCD'
str2='PQR'
for i in range(4):
    print(str1[ : i+1 ] + str2[ i : ])"""