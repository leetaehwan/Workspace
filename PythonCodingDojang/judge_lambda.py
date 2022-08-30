# input 
# 1.jpg 10.png 11.png 2.jpg 3.png


files = input().split()

print(list(map(lambda x : "{0:0>3}".format(x.split('.')[0])+'.'+x.split('.')[1], files)))