def return_int(sample: str):
    arr = []
    for i in range(0, len(sample)):
        try:
            if sample[i] == "o" and sample[i:i+3] == "one":
                arr.append(1)
            elif sample[i] == "t" and sample[i:i+3] == "two":
                arr.append(2)
            elif sample[i] == "t" and sample[i:i+5] == "three":
                arr.append(3)
            elif sample[i] == "f" and sample[i:i+4] == "four":
                arr.append(4)
            elif sample[i] == "f" and sample[i:i+4] == "five":
                arr.append(5)
            elif sample[i] == "s" and sample[i:i+3] == "six":
                arr.append(6)
            elif sample[i] == "s" and sample[i:i+5] == "seven":
                arr.append(7)
            elif sample[i] == "e" and sample[i:i+5] == "eight":
                arr.append(8)
            elif sample[i] == "n" and sample[i:i+4] == "nine":
                arr.append(9)
            else:
                arr.append(int(sample[i]))
        except (IndexError, ValueError):
            continue

    if len(arr) > 1:
        return int(str(arr[0]) + str(arr[len(arr)-1]))
    else:
        return int(str(arr[0]) + str(arr[0]))


if __name__ == "__main__":
    outputs = []
    
    with open("data", 'r') as dataset:
        data = dataset.read().splitlines()

        for i in data:
            outputs.append(return_int(i))

        dataset.close()

        print(sum(outputs))
