# In binary search all the values have to be sorted unlike linear search only one value is sorted.
# list = [4,7,8,12,45,99]
# To find the element in above list we need to get lower bound (index[0]) and upper bound(index[5]) for above list
# L , U for upper and lower bounds.
# Find the mid index 
# mid index = lower + upper / 2
#           = 0 + 5 / 2
        #   = 2-------- the value is 8 from above list.
# Search : 45 
# we are doing integer division not float.
# If you are searching for smaller or bigger value.
# If value is smaller then change upper bound and mid index becomes upper bound.
# If value is bigger then change lower bound and mid index becomes lower bound.




pos = -1    

def binary_search(list,n):
    l=0
    u=len(list)-1

    while l<= u:
        mid = (l+u)//2      # integer division for floor value.
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid
            else:
                u = mid

list = [4,7,8,12,45,99]
n = 7
if binary_search(list,n):
    print("found at",pos+1)
else:
    print("not found")
            
        
    



