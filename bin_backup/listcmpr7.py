L1=list(map(int,input("enter the first list of integers(space-separated):").split()))
L2=list(map(int,input("enter the second list of integers(space-separated):").split()))
if len(L1)==len(L2):
    print("the two lists are  same length")
else:
    print("the two lists are not same length")
if sum(L1)==sum(L2):
    print("the two lists are same value")
else:
    print("the two lists are not  same value")
common_values=set(L1).intersection(set(L2))
if common_values:
    print(f"common values b/w the lists:{common_values}")
else:
    print("no common values b/w the lists")
