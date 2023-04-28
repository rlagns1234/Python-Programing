def purchase():
    result = {}
    bk = False
    print('[구입]')
    name = input('상품명? ')
    if name == '':
        bk = True
    else:
        quantity = int(input('수량은? '))
        result[name] = str(quantity)
        print(f'장바구니에 {name} {quantity}개가 담겼습니다.\n')
    
    if bk == True:
        pass
    else:
        result.update(purchase())
    return result

def search(p_list):
    key = input('장바구니에서 확인하고자 하는 상품은? ')
    bk = False
    if key == '':
        bk = True
    else:
        if key in p_list:
            print(f'{key}은(는) {p_list[key]}개 담겨있습니다.\n')
        else:
            print(f'{key}은(는) {0}개 담겨있습니다.\n')
    
    if bk == True:
        pass
    else:
        search(p_list)

def main():
    product_list = purchase()
    print(f'>>> 장바구니 보기:{product_list}\n')
    search(product_list)

if __name__ == '__main__':
    main()