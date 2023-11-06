def Hello(name :str) -> str :
    ret = f'Hello Nice to mee u, {name}'
    print(ret)
    return ret


if __name__ == '__main__':
    a = 1
    print(type(a))
    Hello(1)