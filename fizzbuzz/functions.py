

def calculate_fizzbuzz(
    count=100, fizz_count=3, buzz_count=5,
    fizz_name='Fizz', buzz_name='Buzz'
):
    ret = [''] * count
    for i in range(1, count + 1):
        if i % fizz_count == 0 and i % buzz_count == 0:
            ret[i - 1] = fizz_name + buzz_name
        else:
            if i % fizz_count == 0:
                ret[i - 1] = fizz_name
            elif i % buzz_count == 0:
                ret[i - 1] = buzz_name
            else:
                ret[i - 1] = i
    return ret
