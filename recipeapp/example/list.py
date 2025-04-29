list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
for idx,val in enumerate(list1):
    print(val,list2[idx])
strs1 = ['i am', 'you are', 'my dog is']
strs2 = ['going home', 'taller than me', 'fatty']

for s1, s2 in zip(strs1, strs2):
	print(s1, s2)