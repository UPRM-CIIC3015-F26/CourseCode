


def get_indexes_for_min_level_standard(levels, min_level):
    indexes = []
    for i in range(len(levels)):
        if levels[i] >= min_level:
            indexes.append(i)
    return indexes


def get_indexes_for_min_level_enumerate(levels, min_level):
    # Use enumerate
    pass



print(get_indexes_for_min_level_standard([10,20, 41, 12, 11], 20 ))
print(get_indexes_for_min_level_enumerate([10,20, 41, 12, 11], 20 ))



def dict_from_keys_and_values_standard(keys, values):
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    return result

def dict_from_keys_and_values_items(keys, values):
    pass

print(dict_from_keys_and_values_standard(["A","B", "C"], [1,2,3]))
print(dict_from_keys_and_values_standard(["A","B", "C"], [1,2,3]))


def frequency_standard(sentence):
    sentence = sentence.lower()
    counts = {}
    for char in sentence:
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts

def frequency_get(sentence):
    pass

print(frequency_standard("hello world"))
print(frequency_get("hello world"))