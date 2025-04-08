#### Problem 3: 
# You are given a set {50, 60, 70, 80, 90}. Remove the number 70 from the set.

my_set1 = {50, 60, 70, 80, 90}
my_set1.remove(70)

print(my_set1)


#### Problem 3: 
# You are given a set {50, 60, 70, 80, 90}. Remove the number 70 from the set.

my_set2 = {50, 60, 70, 80, 90}
my_set2.remove(70)

print("my set after removing 70: " + str(my_set2))

my_set3 = {50, 60, 70, 80, 90}
my_set3.discard(70)  # This will not raise an error if 70 is not in the set

print("my set after removing 70: " + str(my_set3))
