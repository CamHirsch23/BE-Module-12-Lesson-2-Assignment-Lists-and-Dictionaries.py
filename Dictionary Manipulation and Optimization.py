# Task 1: Merge two dictionaries
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

# Task 2: Find intersection of two dictionaries
def find_dictionary_intersection(dict1, dict2):
    intersection = {key: dict1[key] for key in dict1 if key in dict2 and dict1[key] == dict2[key]}
    return intersection

# Task 3: Count frequency of words in a list using a dictionary
def count_word_frequency(words):
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

# Testing the functions
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = merge_dictionaries(dict1, dict2)
print(f"Merged Dictionary: {merged_dict}")

intersection_dict = find_dictionary_intersection(dict1, dict2)
print(f"Intersection Dictionary: {intersection_dict}")

word_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_frequency = count_word_frequency(word_list)
print(f"Word Frequency: {word_frequency}")
