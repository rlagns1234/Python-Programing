def multiplication_tables(s, e):
    loop = (e-s+1)/4
    loop += 1 if((e-s+1)%4 != 0) else 0
    mt_s = s
    for i in range(int(loop)):
        for j in range(1,10):
            for k in range(mt_s, mt_s+4):
                if k <= e:
                    print(f'{k} x {j} = {k*j}\t', end='')
            print('\n')
        mt_s += 4
        print('\n'*2)

def main():
    multiplication_tables(2, 9)

if __name__ == "__main__":
    main()