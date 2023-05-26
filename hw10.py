import sys, os, pickle

class Scores_save_load:
    def __init__(self):
        if os.path.exists('score.bin'):
            with open('score.bin', 'rb') as file:
                print('[파일 읽기]\n')
                print('[점수 출력]')
                list = pickle.load(file)
                avearge = pickle.load(file)
                print(f'개인점수:', end=' ')
                for i in list:
                    print(f'{i}', end=' ')
                print(f'\n평균: {avearge:.1f}')
        else:
            list = Scores_save_load.input_scores()
            avearge = Scores_save_load.get_average(list)
            Scores_save_load.show_scores(list)
            with open('score.bin', 'wb') as file:
                pickle.dump(list, file)
                pickle.dump(avearge, file)

    def input_scores():
        scores_list = []
        trigger = True
        n = 0
        print('[점수 입력]')
        while trigger:
            n +=1
            score = int(input(f'#{n}? '))
            if(score >= 0):
                scores_list.append(score)
            else:
                trigger = False
        return scores_list

    def get_average(list):
        sum = 0
        n = 0
        for i in list:
            sum += i
            n += 1
        average = sum/n
        return average
    
    def show_scores(list):
        print('\n[점수 출력]')
        print('개인점수:', end=' ')
        for i in list:
            print(f'{i}', end=' ')

        average = Scores_save_load.get_average(list)
        print(f'\n평균: {average:.1f}')

if __name__ == '__main__':
    s = Scores_save_load()