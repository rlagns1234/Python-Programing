#메시지에 넣을 이름 입력 함수
def get_name():
    return input('Input his/her name: ')    #이름 입력

#'-' 기호로 줄 만드는 함수
def rep_char_return(c, n):
    return c*n  #'-'를 n개 리턴

#이름을 매개변수로 받아 메세지에 넣어 출력하는 함수
def welcome_message(name):
    msg = 'Hello '+str(name)+',\nWelcome to Seaul.'    #매개변수 이름을 결합하여 메세지 생성

    #첫줄과 두번째 줄 중 더 긴 줄로 '-' 박스를 생성, 메세지 출력
    print('{0}\n{1}\n{0}'.format(rep_char_return('-',max(msg.find('\n'), msg[::-1].find('\n'))), msg))

#메인함수
def main():
    welcome_message(get_name())

#메인으로 호출되었을때 실행
if __name__ == '__main__':
    main()