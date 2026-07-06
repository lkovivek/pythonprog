def scope_test():
    def do_local():
        spam="local spam"
        print(f'memory location of local_spam {id(spam)}')
    
    def do_nonlocal():
        nonlocal spam
        spam="nonlocal spam"
        print(f'memory location of nolocal_spam {id(spam)}')

    def do_global():
        global spam
        spam="global spam"
        print(f'memory location of global_spam {id(spam)}')
    
    spam="test spam"
    do_local()
    print(f'After local assignment: {spam} and memory location of spam is {id(spam)}')
    do_nonlocal()
    print(f'After nonlocal assignment: {spam} and memory location of spam is {id(spam)})')
    do_global()
    print(f'After global assignment: {spam} and memory location of spam is {id(spam)}')

scope_test()
print(f'In global scope: {spam}')