switch = {
    '+': lambda x, y: x + y,    # 람다 표현식으로 실행할 코드를 작성
    '*': lambda x, y: x * y
    }
 
x = '+'
try:
    print(switch[x](10, 20))    # 딕셔너리에 키를 지정하는 방식
except KeyError:
    print('default')            # 딕셔너리에 키가 없을 때는 기본값