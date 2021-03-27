

def calculate_fizzbuzz(
    count=100, fizzcount=3, buzzcount=5,
    fizzname='Fizz', buzzname='Buzz'
):
    ret = [''] * count
    for i in range(1, count + 1):
        if i % fizzcount == 0 and i % buzzcount == 0:
            ret[i - 1] = fizzname + buzzname
        else:
            if i % fizzcount == 0:
                ret[i - 1] = fizzname
            elif i % buzzcount == 0:
                ret[i - 1] = buzzname
            else:
                ret[i - 1] = i
    return ret
