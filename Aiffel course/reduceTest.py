from functools import reduce
# reduce() executes funcs and accumulates results
# By contrast, map() executes funcs and make each result.
print(reduce(lambda x,y: x+y, [0,1,2,3,4]))
# result : ( 0+1+2+3+4 = ) 10