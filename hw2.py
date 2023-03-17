def exchange(amount):
    coin = [500, 100, 50, 10]
    for i in coin:
        print(i, '원 동전의 개수:', amount//i)
        amount%=i

def get_integer(prompt):
    return int(input(prompt))

prompt = '동전으로 교환하고자 하는 금액은? '
exchange(get_integer(prompt))