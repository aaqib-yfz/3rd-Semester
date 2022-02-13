# def seqSearch(alist,item):
#     i=0
#     found = False
#     while i < len(alist) and not found:
#         if alist[i]==item:
#             found = True
#         else:
#             i=i+1
#     return found

# test=[1,2,4,5,6]
# print(seqSearch(test,10))

def binsearch(alist,item):
    first=0
    last=len(alist)-1
    found = False
    while first <= last and not found:
        mid=(first + last )// 2
        if alist[mid]==item:
            found = True
        elif alist[mid]<item:
            first = mid + 1
        else:
            last = mid -1
            
    return found 

test = [1,5,6,77,99,86]
print(binsearch(test,3))
            