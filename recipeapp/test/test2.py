list1=["aaa","bbb","ccc","ddd","eee"]
list2=["111","222","333","444","555"]
'''
for idx,val in enumerate(list1):
    print(f"{val}-{list2[idx]}")
'''
for s1,s2 in zip(list1,list2):
    print(f"{s1}-{s2}")

