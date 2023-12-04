def return_number(string: str):
    # first remove Card Id:
    string = string.split(":")
    string.pop(0)
    string = string[0].split('|')

    winning_nums = list(map(int, string[0].split()))
    nums_on_card = list(map(int, string[1].split()))

    num = 0
    counter = 0

    for i in nums_on_card:
        if i in winning_nums:
            if counter == 0 and num == 0:
                num = 1
            else:
                num = num * 2
            counter = counter + 1

    return num

if __name__ == "__main__":
    arr = []
    with open("day4_data", 'r') as dataset:
        data = dataset.read().splitlines()
        for i in data:
            arr.append(return_number(i))

    dataset.close()
    print(sum(arr))
