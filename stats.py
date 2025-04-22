def word_count(txt_input):
	w_number=len(txt_input.split())
	return (w_number)

def char_count(txt_input):
	txt_input=txt_input.lower()
	all_chars=list(txt_input)
	char_dict={}
	for char in all_chars:
		if char in char_dict:
			char_dict[char] +=1
		else:
			char_dict[char] = 1
	return char_dict

def sort_dict(input_dict):


	dict_list=[]
	for key,value in input_dict.items():
		dict_list.append({key:value})


	dict_list.sort(reverse=True, key=lambda x: list(x.values())[0])
	return dict_list
