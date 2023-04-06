num_kor_dic = {0:'영',1:'일',2:'이',3:'삼',4:'사',5:'오',6:'육',7:'칠',8:'팔',9:'구'}

def read_single_digit(num):
    if num == 0:
        return '영'
    elif num == 1:
        return '일'
    elif num == 2:
        return '이'
    elif num == 3:
        return '삼'
    elif num == 4:
        return '사'
    elif num == 5:
        return '오'
    elif num == 6:
        return '육'
    elif num == 7:
        return '칠'
    elif num == 8:
        return '팔'
    elif num == 9:
        return '구'

def read_single_digit_upgrade(num):
    match num:
        case 0: return '영'
        case 1: return '일'
        case 2: return '이'
        case 3: return '삼'
        case 4: return '사'
        case 5: return '오'
        case 6: return '육'
        case 7: return '칠'
        case 8: return '팔'
        case 9: return '구'

def read_number(num):
    return f'{read_single_digit(num//100)} {read_single_digit_upgrade((num%100)//10)} {read_number_all(num%10)}'
    
def read_number_all(num):
    num_list = list(str(num))
    result = ''
    for i in num_list:
        result += num_kor_dic[int(i)]
    return result

def main():
    num = int(input("세 자리 정수 입력: "))
    print(read_number(num))

if __name__ == "__main__":
    main()