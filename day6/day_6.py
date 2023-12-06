def return_winning_ways(time: int, distance: int):
    num = 0
    for i in range(1, min(time, distance)):
        if i * (time - i) > distance:
            num = num + 1

    return num

if __name__ == "__main__":
    with open('dataset', 'r') as dataset:
        data = dataset.read().split("\n")
        time = data[0].split()
        distance = data[1].split()

        time.pop(0)
        distance.pop(0)
        
    dataset.close()

    time = list(map(int, list(time)))
    distance = list(map(int, list(distance)))
    num = 1

    for i in range(0, len(time)):
        num = num * return_winning_ways(time[i], distance[i])

    print(num)
