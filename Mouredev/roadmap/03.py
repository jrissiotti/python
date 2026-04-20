# 03 Data structure

# Lists
my_list = ["Jorge", "Hacker", "Python", 19]
print(my_list)

my_list.append("Rissiotti")
print(my_list)

my_list.remove("Hacker")
print(my_list)
print(my_list[1])

my_list[1] = "Skeleton"
print(my_list)

my_list.sort(key = str) # 19 is still int; key = str only uses it as text for sorting, it doesn't convert it 
print(my_list)

# Tuples
my_tuple = ()