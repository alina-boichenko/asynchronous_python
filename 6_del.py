def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


class NewException(Exception):
    pass


def subgen():  # reading generator
    while True:
        try:
            message = yield
        except StopIteration:
            break
        else:
            print("----------", message)

    return "Returned from subgen()"


@coroutine
def delegator(g):  # translator, delegating generator
    result = yield from g
    print(result)
