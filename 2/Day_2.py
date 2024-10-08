def main():

    # create dict to add data from input.txt
    game_dict = {}

    # read in code from input.txt
    with (open('input.txt') as f):
        for line in f:
            print(line)
            # Set dict key
            raw_key, raw_value = line.strip().split(':')
            key = int(raw_key[5:])
            print(f"{key=}")

            # Get dict of dicts for the three cube colours
            print(f"{value=}")
            game_dict[key] = raw_value


if __name__ == "__main__":
    main()