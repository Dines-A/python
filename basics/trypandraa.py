def display(num):
    if num == 0:
        return 
    display(num-1)
    print(num)

display(5)
