running = True

while running:
  condition = int(input("""
1을 입력하면 3,5,7,9단의 구구단을 출력
2를 입력하면 2,4,6,8단의 구구단을 출력
3을 입력하면 종료
그외의 숫자를 입력하면 처음부터 다시 입력

원하는 숫자를 입력해주세요 : """))
  if condition in [1,2]:
    for i in range(((condition%2) +2),10,2):
      print(f"\n{i}단")
      for k in range(1,10):
        print(f"{i} * {k} = {i*k}")
  elif condition == 3:
    print("프로그램을 종료합니다.")
    running = False