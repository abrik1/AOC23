def return_int(sample: str):
    arr = []
    for i in range(0, len(sample)):
        try:
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
