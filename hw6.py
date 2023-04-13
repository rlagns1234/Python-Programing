#구구단 테이블 생성 함수 s:시작 숫자, e:끝나는 숫자, n:열의 개수, n2:곱할 숫자의 범위
def multiplication_tables(s, e, n, n2):
    loop = (e-s+1)//n   #출력할 구구단의 단의 개수 / 열의 개수 = 출력할 구구단 행의 수
    loop += 1 if((e-s+1)%n != 0) else 0 #구구단 단 개수가 n으로 나누어떨어지지 않는다면 구구단 행의 수를 하나 더 추가
    mt_s = s    #구구단 행을 바꿀때 첫번째 열에 출력할 단의 단위 저장 변수

    #츌력할 구구단 행의 수 만큼 반복
    for i in range(loop):
        #k(단)x1 ~ k(단)xn2 까지 출력하기 위해 1~n2까지 n2번반복
        for j in range(1,n2+1):
            #첫번째 열의 단부터 총 n개의 단을 하나의 행에 출력. n번 반복
            for k in range(mt_s, mt_s+n):
                if k <= e:  #출력할 단의 범위가 지정해준 범위(e)를 벗어나지 않았을때 실행. 벗어나면 그냥 넘어감
                    print(f'{k} x {j} = {k*j}\t', end='')   #구구단 출력
            print('\n') #줄바꿈
        mt_s += n   #첫번째 열에 출력한 단을 업데이트
        print('\n'*2)   #행바꿈

def main():
    multiplication_tables(2, 9, 4, 9)   #2단부터 9단까지 4개열로 1~9까지 곱한 값 출력

if __name__ == "__main__":
    main()