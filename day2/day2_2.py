def is_game_possbile(input: str):
    input = input.split(';')
    input[0] = input[0].split(":")[1].lstrip()
    red_array = [] 
    green_array = []
    blue_array = []

    for i in input:
        for j in i.split(','):
            if "red" in j:
                red_array.append(int(j.split()[0].lstrip().rstrip()))
            elif "green" in j:
                green_array.append(int(j.split()[0].lstrip().rstrip()))
            else:
                blue_array.append(int(j.split()[0].lstrip().rstrip()))

    red_array.sort()
    green_array.sort()
    blue_array.sort()

    return red_array[len(red_array)-1] * green_array[len(green_array) - 1] * blue_array[len(blue_array) - 1]

if __name__ == "__main__":
    arr = []
    with open("day2_data", 'r') as dataset:
        data = dataset.read().splitlines()

        for i in data:
            if is_game_possbile(i) != False:
                arr.append(is_game_possbile(i))

    dataset.close()
    print(sum(arr))
