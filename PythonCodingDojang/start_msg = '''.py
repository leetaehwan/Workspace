start_msg = '''
구구단 프로그램을 실행합니다.
1. 홀수 구구단
2. 짝수 구구단
3. 종료

숫자를 입력 하세요: '''


class Input:
    def __init__(self, n):
        if n == 1:
            self.odd()
        elif n == 2:
            self.even()
        else:
            print('잘못 입력하셨습니다. 1 ~ 3번 숫자를 입력 하세요.')
    
    def odd(self):
        for i in list(range(3, 10, 2)):
            print('\n%d단' % i)
            for j in range(1, 10):
                print('{0} * {1} = {2}'.format(i, j, i*j))
        
    def even(self):
        for i in list(range(2, 10, 2)):
            print('\n%d단' % i)
            for j in range(1, 10):
                print('{0} * {1} = {2}'.format(i, j, i*j))

while True:
    n = int(input(start_msg))
    
    if n == 3:
        print('프로그램을 종료 합니다.')
        break
    else:
        Input(n)