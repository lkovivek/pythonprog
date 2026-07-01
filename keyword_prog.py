# *args and **kwargs in python
# *args example
def fun_sum(*args):
    return sum(args)

# **kwargs example
def fun_1(**kwargs):
    for k,val in kwargs.items():
        print(k,val)
