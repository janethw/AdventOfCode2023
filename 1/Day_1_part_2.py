import copy


def main():
    two_nums = 0
    count = 0
    total = 0
    valid_digits_dict = {'one': 1, 'two': 2,  'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    def forward_check_line_for_numbers_as_words(line_string):
        for i in range(len(line_string)):
            if line_string[i:i+3] in valid_digits_dict:
                #print(f"at index {i=}: {valid_digits_dict[line_string[i: i+3]]=}")
                # replace the number as a word with the integer
                line_string = line_string.replace(line_string[i:i + 3], str(valid_digits_dict[line_string[i:i + 3]]))

            elif line_string[i:i+4] in valid_digits_dict:
                #print(f"at index {i=}: {valid_digits_dict[line_string[i: i+4]]=}")
                # replace the number as a word with the integer
                line_string = line_string.replace(line_string[i:i + 4], str(valid_digits_dict[line_string[i:i + 4]]))

            elif line_string[i:i+5] in valid_digits_dict:
                #print(f"at index {i=}: {valid_digits_dict[line_string[i: i+5]]=}")
                # replace the number as a word with the integer
                line_string = line_string.replace(line_string[i:i + 5], str(valid_digits_dict[line_string[i:i + 5]]))

        #print(f"after conversion of words, {line_string=}")
        return line_string

    def backward_check_line_for_numbers_as_words(line_string):
        for i in range(len(line_string))[::-1]:
            # print(f"{i=}")
            if line_string[i-2:i+1] in valid_digits_dict:
                # print(f"at index {i=}: {valid_digits_dict[line_string[i-2:i+1]]=}")
                # replace the number as a word with the integer
                line_string = line_string.replace(line_string[i-2:i+1], str(valid_digits_dict[line_string[i-2:i+1]]))

            elif line_string[i-3:i+1] in valid_digits_dict:
                # print(f"at index {i=}: {valid_digits_dict[line_string[i-3:i+1]]=}")
                # replace the number as a word with the integer
                line_string = line_string.replace(line_string[i-3:i+1], str(valid_digits_dict[line_string[i-3:i+1]]))

            elif line_string[i-4:i+1] in valid_digits_dict:
                # print(f"at index {i=}: {valid_digits_dict[line_string[i-4:i+1]]=}")
                # replace the number as a word with the integer
                line_string = line_string.replace(line_string[i-4:i+1], str(valid_digits_dict[line_string[i-4:i+1]]))

        #print(f"after conversion of words, {line_string=}")
        return line_string

    # open file and go through each line of text
    with (open('input.txt') as f):
        for line in f:
            # print(f"{line=}")
            # words_as_nums = words_as_ints(line)
            # print(words_as_nums)

            # convert words to ints when reading forward
            forward_line_as_nums = forward_check_line_for_numbers_as_words(line)

            # convert words to ints when reading backward
            backward_line_as_nums = backward_check_line_for_numbers_as_words(line)
            # print(f"{forward_line_as_nums=}\n{backward_line_as_nums=}")

            # get first int
            for char in forward_line_as_nums:
                # check if it is an int

                if count == 1:
                    break
                if count == 0:
                    try:
                        if isinstance(int(char), int):
                            two_nums = int(char) * 10
                            # print(f"{two_nums=}")
                            count += 1
                    except ValueError:
                        continue

            # get last int
            for char in list(backward_line_as_nums.strip())[::-1]:
                if count == 2:
                    break
                if count == 1:
                    # print(f"{char=}")
                    try:
                        if isinstance(int(char), int):
                            two_nums += int(char)
                            count += 1
                            # print(f"{two_nums=}")
                            # add two-digit number to the total
                            total += two_nums
                            # print(f"{total=}")
                    except ValueError:
                        continue

            count = 0
            two_nums = 0
    print(f"{total=}")
    return total


if __name__ == '__main__':
    main()
