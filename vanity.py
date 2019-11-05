def let_num(letter):
	if letter in "abc":
		return ("2")
	if letter in "def":
		return ("3")
	if letter in "ghi":
		return ("4")
	if letter in "jkl":
		return ("5")
	if letter in "mno":
		return ("6")
	if letter in "pqrs":
		return ("7")
	if letter in "tuv":
		return ("8")
	if letter in "wxyz":
		return ("9")

def lets_nums(code):
	res = ""
	for x in range(len(code)):
		res = res + str(let_num(code[x]))
	print(res)
	return (res)

def vanity(codes, numbers):
	result = []
	for x in range(len(codes)):
		nums = lets_nums(codes[x])
		for y in range(len(numbers)):
			if nums in numbers[y]:
				result.append(numbers[y])
	return (result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    codes_count = int(input().strip())

    codes = []

    for _ in range(codes_count):
        codes_item = input()
        codes.append(codes_item)

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = input()
        numbers.append(numbers_item)

    result = vanity(codes, numbers)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
