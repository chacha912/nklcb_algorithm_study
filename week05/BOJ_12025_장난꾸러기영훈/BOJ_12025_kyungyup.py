
def solution():
    s = input()
    k = int(input())
    binary = bin(k-1)
    bit = ""
    answer = ""

    count = 0
    p = len(binary)-1
    for i in s:
        if i == "1" or i == "2":
            count += 1
        if i == "6":
            bit += "1"
            count += 1
        elif i == "7":
            bit += "2"
            count += 1
        else:
            bit += i
    if k > 2**count:
        print(-1)
        return

    for i in bit[::-1]:
        if i == "1":
            if binary[p] == "1":
                answer = "6" + answer
                p -= 1
            elif binary[p] == "0":
                answer = i + answer
                p -= 1
            else:
                answer = i + answer

        elif i == "2":
            if binary[p] == "1":
                answer = "7" + answer
                p -= 1
            elif binary[p] == "0":
                answer = i + answer
                p -= 1
            else:
                answer = i + answer
        else:
            answer = i + answer
    print(answer)

    return


solution()
