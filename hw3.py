def get_discount_rate():
    dr = int(input('할인율은? '))
    return dr

def get_fixed_price(dp):
    global discountRate
    price = int(100*dp/(100-discountRate))
    return price

discountRate = get_discount_rate()
discount_A = int(input('A 상품의 할인된 가격은? '))
discount_B = int(input('B 상품의 할인된 가격은? '))
fixed_A = get_fixed_price(discount_A)
fixed_B = get_fixed_price(discount_B)
print('A 상품의 정가는 ',fixed_A,'원')
print('B 상품의 정가는 ',fixed_B,'원')