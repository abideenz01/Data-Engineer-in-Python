# Four ways to combine lists
#1. 
Letters=['a','b','c','d']
Numbers=[1,2,3,4]
combine_list=Letters + Numbers
print(combine_list)
print("----------------------------")
#3.
#2.
Letters_1=['a','b','c','d']
Numbers_2=[1,2,3,4]
combine_list_1=[Letters, Numbers]
print(combine_list_1)
print("----------------------------")
#3.
Letters_2=['a','b','c','d']
Numbers_2=[1,2,3,4]
Numbers_2.extend(Letters_2)
print(Numbers_2)
print("----------------------------")
#4. zip creates pairs of ids and Names
Ids=[101,102,103,104]
Names=['Zain','Ali','Alice','Joseph']
comb_list=list(zip(Ids,Names))
print(f"(ID,Name): {comb_list}")

