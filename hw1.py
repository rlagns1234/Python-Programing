#메인 함수
def main():
    prompt = '넓이를 구하고자 하는 원의 반지름은? ' #input 메세지
    radius = get_radius(prompt) #반지름을 input으로 받아오는 함수 호출, prompt 메세지 매개변수 전달
    area = get_circle_area(radius) #매개변수로 전달받은 반지름으로 원의 넓이를 구하는 함수 호출
    print('반지름', radius,'인 원의 넓이 = 3.14 x', radius, 'x', radius, '=', area) #원의 넓이 출력

#반지름을 입력받는 함수
def get_radius(prompt):
    r = int(input(prompt)) #입력받은 반지름을 Integer로 형변환 후 저장
    return r #반지름 반환

#원의 넓이를 구하는 함수
def get_circle_area(radius):
    area = 3.14*(radius**2) #원의 넓이 = 3.14 x 반지름^2 
    return area #원의 넓이 반환

#프로그램 실행
try: 
    main()
except Exceptionas as e:
    print(e)