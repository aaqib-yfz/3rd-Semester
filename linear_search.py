def search(alist,item):
    i =0
    found = False
    while i< len(alist) and not found:
        if alist[i]== item:
            found = True
        else:
            i = i+1
    return found

test=[1,2,4,8,9]
print(search(test,9))