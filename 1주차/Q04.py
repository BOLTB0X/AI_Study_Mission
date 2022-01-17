from collections import Counter
dict_first = {'사과':30, '배':15, '감':10, '포도':10}
dict_second = {'사과':5, '감':25, '배':15, '귤': 25}

def merge_dict(dict_first, dict_second):
    f_tmp = Counter(dict_first)
    s_tmp = Counter(dict_second)
    
    tot = f_tmp + s_tmp
    ret = dict(tot)
    s_ret = sorted(ret.items())
    return dict(s_ret);

print(merge_dict(dict_first, dict_second))