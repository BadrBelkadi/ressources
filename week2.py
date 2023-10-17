def test_function(array):
	new_list = []
	new_string = ""

	for char in array :
		new_list.append(chr(char))
		
	for char in new_list :
		new_string += char

    # we could perform both actions in one loop.

	lower_string = new_string.lower()

	letter_string = lower_string[2:10] * 2

	return letter_string





