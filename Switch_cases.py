Input = input("Enter a phrase: ") # taking input.

def switch():		# making a function. You can do this without function as well.
	converted = ""  
	for i in Input:
		if i >= "A" and i <= "Z":
			converted = converted + i.lower()	#if in uppercase, we'll convert it to lowercase.
		else:
			converted = converted + i.upper()	#If in lower, will be converted to upper.

	return converted	#returning the result.

print(switch())


# Without using function...
'''
converted = ""  
for i in Input:
	if i >= "A" and i <= "Z":
		converted = converted + i.lower()
	else:
		converted = converted + i.upper()
print(converted)

'''