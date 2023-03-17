#동전 종류별 교환 개수 구하는 함수
def exchange(amount):
    coin = [500, 100, 50, 10]   #500원, 100원, 50원, 10원 동전 리스트
    for i in coin:  #리스트에서 하나씩 동전 종류 빼오기
        print(i, '원 동전의 개수:', amount//i)  #필요한 동전 개수 출력
        amount%=i   #나머지 저장

#값 입력받는 함수
def get_integer(prompt):
    return int(input(prompt))

#프로그램 실행
prompt = '동전으로 교환하고자 하는 금액은? '
exchange(get_integer(prompt))