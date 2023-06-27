def benchmark(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения {end-start}")
        return return_value
    return wrapper

def character_counter_v0(s): # s - строка символов
    for sym in s:
        counter = 0
        for sub_sym in s:
            if sub_sym == sym:
                counter += 1
        print(f'количество "{sym}" = {counter}')
@benchmark
def character_counter_v1(s): # s - строка символов
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sub_sym == sym:
                counter += 1
        print(f'количество "{sym}" = {counter}')
@benchmark
def character_counter_v2(s): # s - строка символов
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    return syms_counter

def print_symbs(d):
    for sym, count in d.items():
        print(f'количество "{sym}" = {count}')


s = ";qejrnljnvljkneorinvweoriviequnvkamdfv;knsdfvnoeirnvweouvriewurviuevriuenrvnretrcybuimoikpl,kmjnhbuvyctrertcfbhnjmkl,qwoieurqwoiuerpoqwiuerpoqwuierpoiquewrpqewuirpoqwuerpoiuqweproiuqewpoiruqpwoieurpqowuierpoquiwerpoiquweporiuqweporuiqwopeiurpqoewuirpoqiuewropiuqwerpoiuqwepruiqwpoerupqewroizxcvnz.,vn.,mcv,snfdvkjsfndvkjfndvjsnfdlvnsjdlfkjvnsldkjvneuwir9384ur39324028350923jf2984fj398jf3nj4kjndfkjdeqwur"
character_counter_v1(s)
d = character_counter_v2(s)
print_symbs(d)