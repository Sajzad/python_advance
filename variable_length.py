def var_len(*args, **kwargs):
    for key,value in kwargs.items():
        print(key, value)

    for item in args:
        print(item)
    return [args,kwargs]

print(var_len(3,a=2, b=3))