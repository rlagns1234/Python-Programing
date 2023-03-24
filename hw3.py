#할인율을 받아오는 함수
def get_discount_rate():
    dr = int(input('할인율은? '))
    return dr

#할인된 가격 -> 정가로 계산 함수
def get_fixed_price(dp):
    global discountRate #할인율
    price = int(100*dp/(100-discountRate))  #정가 계산
    return price

discountRate = get_discount_rate()  #할인율 입력

#상품 A,B 할인가 입력
discount_A = int(input('A 상품의 할인된 가격은? '))
discount_B = int(input('B 상품의 할인된 가격은? '))

#정가 계산 함수 호출
fixed_A = get_fixed_price(discount_A)
fixed_B = get_fixed_price(discount_B)

#정가 출력
print('A 상품의 정가는 ',fixed_A,'원')
print('B 상품의 정가는 ',fixed_B,'원')