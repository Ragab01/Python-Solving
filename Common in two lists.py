list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Convert lists to sets and find the intersection
common_elements = list(set(list1) & set(list2))

print("Common elements:", common_elements)