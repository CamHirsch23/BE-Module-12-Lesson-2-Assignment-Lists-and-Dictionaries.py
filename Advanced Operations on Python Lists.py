# Task 1: List Comprehension for Squares
def squares(n):
    return [i * i for i in range(1, n + 1)]

# Task 2: Reversing a Sublist
def reverse_sublist(lst, i, j):
    lst[i:j+1] = lst[i:j+1][::-1]
    return lst

# Task 3: Merging Two Sorted Lists
def merge_sorted_lists(list1, list2):
    merged_list = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append remaining elements
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list

# Example usage:
n = 10
print("Squares from 1 to n:", squares(n))

lst = [10, 20, 30, 40, 50, 60, 70, 80]
i, j = 2, 5
print("Original list:", lst)
print("Reversed sublist from index", i, "to", j, ":", reverse_sublist(lst, i, j))

list1 = [1, 3, 5]
list2 = [2, 4, 6]
print("Merged sorted lists:", merge_sorted_lists(list1, list2))
