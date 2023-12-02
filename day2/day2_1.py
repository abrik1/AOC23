def is_game_possbile(input: str):
    input = input.split(';')
    id = int(input[0].split(":")[0].split("Game")[1].lstrip().rstrip())
    input[0] = input[0].split(":")[1].lstrip()

    for i in input:
        for j in i.split(','):
            if "red" in j and int(j.split("red")[0].rstrip().lstrip()) > 12 or "blue" in j and int(j.split("blue")[0].lstrip().rstrip()) > 14 or "green" in j and int(j.split("green")[0].lstrip().rstrip()) > 13:
                return False
            
    return id

if __name__ == "__main__":
    arr = []
    with open("day2_data", 'r') as dataset:
        data = dataset.read().splitlines()

        for i in data:
            if is_game_possbile(i) != False:
                arr.append(is_game_possbile(i))

    dataset.close()
    print(sum(arr))
