
# For each unique character that appears in the input string, report the number of occurrences of that character in the input.  Report each character on its own line, in descending order based on the number of occurrences. Output values in a dictionary. Each line should be formatted as follows:


def char_count(str):
#   split input str into individual letters in an array
    letter_list = list(str)
    # create a dict varialble
    letter_count_dict = {}
# loops through letter_array and assign dictionary key and values use .get()
    for letter in letter_list:
        if letter in letter_count_dict:
            # print('adding letter count +=1')
            letter_count_dict[letter] += 1
        if not letter in letter_count_dict:
            # print('assigning letter dict')
            letter_count_dict[letter] = 1
    # sort the dictionary by values and declare varriable
    sorted_letter_dict_values = sorted(letter_count_dict.values(), reverse=True)
    # declare a sorted_dictionary varriable and loop through passing values in decending order
    sorted_dictionary = {}
    for value in sorted_letter_dict_values:
        for key in letter_count_dict:
            if letter_count_dict[key] == value:
                sorted_dictionary[key] = letter_count_dict[key]
                break
    return sorted_dictionary

        
# print(char_count('helloooo'))