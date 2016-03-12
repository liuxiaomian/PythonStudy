#装饰器 decorator
def log(text=None):
    def first(fun):
        def decorator(*args,**kw):
            if text is None:
                print("begin")
            else:
                print("begin",text)
            return fun(*args,**kw)
        print("over")
        return decorator
    return first;


@log("world")
def func(a):
    print("16-3-12",a)
    return

func('hello')