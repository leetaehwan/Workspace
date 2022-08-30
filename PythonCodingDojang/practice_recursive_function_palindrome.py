def is_palindrome(word):
  # if len(word) <2:
  #   return True
  # if word[0] != word[-1]:
  #   return False
  # return is_palindrome(word[1:-1])
  if len(word) >= 3:
    temp = list(map(str, [i for i in word]))
    revTemp = list(map(str, [i for i in word[::-1]]))
    if temp == revTemp:
      return True
    else:
      return False
  else:
    return False

print(is_palindrome('hello'))
print(is_palindrome('level'))