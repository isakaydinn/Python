from tkinter import Y


ylist = []
    
def ilkgirdi(l):
    for i in l:
        if type(i)==list:
            ilkgirdi(i)
        else:
            ylist.append(i)

ilkgirdi([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
print(ylist)

# reverse 

x = [[1, 2], [3, 4], [5, 6, 7]]
yedek = []

def ters(l):
    for i in l:
        if type(i)==list:
            yedek.append(list(reversed(i)))
            
            
        

ters([[1, 2], [3, 4], [5, 6, 7]])
print(list(reversed(yedek)))