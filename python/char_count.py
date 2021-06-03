def char_count(str):
	char_dict = {}

	str = str.replace(' ', '')

	for i in str:
		if i in char_dict:
			char_dict[i] += 1
		else:
			char_dict[i] = 1

	sorted_dict = dict(sorted(char_dict.items(), key=lambda x: x[1], reverse=True))

	return sorted_dict

print(char_count("aaabbc"))
print(char_count("an apple a day will keep the doctor away"))