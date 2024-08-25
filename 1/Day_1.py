# Answer is: 54597

def main():
    two_nums = 0
    count = 0
    total = 0

    with (open('input.txt') as f):
        for line in f:
            # print(f"{line}")
            # get first int
            for char in line:
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
            for char in list(line.strip())[::-1]:
                if count == 2:
                    break
                if count == 1:
                    # print(f"{char=}")
                    try:
                        if isinstance(int(char), int):
                            two_nums += int(char)
                            count += 1
                            print(f"{two_nums=}")
                            # add two-digit number to the total
                            total += two_nums
                            # print(f"{total=}")
                    except ValueError:
                        continue

            count = 0
            two_nums = 0
        print(total)
        return total


if __name__ == '__main__':
    main()
