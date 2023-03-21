first_set = {1, 5, 7, 4, 5}
second_set = {4, 5, 6, 7, 8}
 
#INTERSECTION
intersection_set = first_set & second_set
 
print(intersection_set)  

diff_set = first_set - second_set
 
print(diff_set) 

union_set = first_set | second_set
 
print(union_set)

sym_diff=first_set.symmetric_difference(second_set)
print(sym_diff)
