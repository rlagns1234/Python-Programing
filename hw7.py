def purchase():
    result = {}
    print('[구입]')
    while True:
        name = input('상품명? ')
        if name == '':
            break
        quantity = int(input('수량은? '))
        result[name] = str(quantity)
        print(f'장바구니에 {name} {quantity}개가 담겼습니다.\n')
    return result

def search(p_list):
    while True:
        key = input('장바구니에서 확인하고자 하는 상품은? ')
        if key == '':
            break
        if key in p_list:
            print(f'{key}은(는) {p_list[key]}개 담겨있습니다.\n')
        else:
            print(f'{key}은(는) {0}개 담겨있습니다.\n')

def main():
    product_list = purchase()
    print(f'>>> 장바구니 보기:{product_list}\n')
    search(product_list)

if __name__ == '__main__':
    main()