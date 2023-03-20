# python3
#221RDB216

def build_heap(data):
    swaps = []
size = len(data)
    for i in range(size // 2, -1, -1):
        darbiba(data, i, swaps)


    return swaps

def darbiba(data, i, swaps):
    size = len(data)
    mindex = i
    leftS = 2 * i + 1
    rightS = 2 * i + 2
    if leftS < size and data[leftS] < data[mindex]:
        mindex = leftS
    if rightS < size and data[rightS] < data[mindex]:
        mindex = rightS
    if mindex != i:
        swaps.append((i, mindex))
        data[i], data[mindex] = data[mindex], data[i]
        darbiba(data, mindex, swaps)


def main():
    inputz = input()
    if "I" in inputz:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
    elif "F" in inputz:
        input_fails = input()
        locations = './tests/'
        locations_faila = os.path.join(locations, input_fails)
        with open(locations_faila, mode="r") as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
        
if __name__ == "__main__":
    main()
    #RobertsKarlisKaudze

