from datetime import datetime
import hashlib


# 1
def decor(old_function):
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open('data.txt', 'a', encoding='utf-8') as f:
            f.write(f'Имя функции - {old_function.__name__}, '
                    f'дата и время вызова функции - {datetime.now()}, '
                    f'аргументы функции - {args}, {kwargs}, '
                    f'возвращаемое значение - {result}\n')
        return result
    return new_function


@decor
def foo(x):
    x += 10
    return x


if __name__ == '__main__':
    foo(10)


# 2
def path_to_logs(path):
    def decor(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open('data.txt', 'a', encoding='utf-8') as f:
                f.write(f'Имя функции - {old_function.__name__}, '
                        f'дата и время вызова функции - {datetime.now()}, '
                        f'аргументы функции - {args}, {kwargs}, '
                        f'возвращаемое значение - {result}\n')
            return result
        return new_function
    return decor


@path_to_logs('data.txt')
def foo2(x):
    x -= 2
    return x


if __name__ == '__main__':
    foo2(10)


# 3
@path_to_logs('data.txt')
def md5_hash(path):
    with open(path, encoding='utf-8') as f:
        for line in f:
            yield hashlib.md5(line.strip().encode('utf-8')).hexdigest()


for i in md5_hash('data.txt'):
    print(i)
