def checker(function, *args, **kwargs):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f" we hjave a bolhoy prablema - {exc}")
        else:
            print(f" NO PROBLEMS - {result}")

    return checker


@checker
def calculate(expression):
    return eval(expression)


calculate("2+2")