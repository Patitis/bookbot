from stats import word_count
from stats import char_count
from stats import sort_dict
import sys
import os

def get_text(filepath):
	
	with open(filepath) as f:
		file_contents = f.read()
	return (file_contents)

def main():
	if  len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	elif not os.path.exists(sys.argv[1]):
		print(f"Error: {sys.argv[1]} does not exist")
		sys.exit(1)
        
	else:
		
		bk_contents=get_text(sys.argv[1])
		w_count=word_count(bk_contents)
		c_count=char_count(bk_contents)
		report=sort_dict(c_count)

		print ("============ BOOKBOT ============")
		print ("Analyzing book found at {sys.argv[1]}")
		print ("----------- Word Count ----------")
		print (f"Found {w_count} total words")
		print ("--------- Character Count -------")
		for line in report:
			for key,value in line.items():
				if key.isalpha():
					print (f"{key}: {value}")
	
main()
