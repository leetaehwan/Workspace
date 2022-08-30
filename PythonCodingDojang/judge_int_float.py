# 숫자를 입력할 때 그 숫자가 정수인지 소수인지 구별하는 프로그램을 만들고
# 만약에 문자를 입력했으면 숫자가 아니므로 “ 잘못된 입력입니다” 출력하는 함수를 만드세요

# 숫자 입력
def inputNum():
  try:
    number = int(input())
  except:
    print("잘못된 입력입니다.")
  return number

# 소수 판별
def judgePrimeNum(number):
  count = 0
  if number == 0:
    print(f"정수 {number}을 입력하셨습니다.")
  for i in range(1,number):
    if number % i == 0:
      count += 1
  if count ==0:
    print(f'정수 {number}을 입력하셨습니다.')
  elif count == 1:
    print(f'소수 {number}을 입력하셨습니다.')
  elif type(number) == int:
    print(f'정수 {number}을 입력하셨습니다.')

# 실행코드
judgePrimeNum(inputNum())