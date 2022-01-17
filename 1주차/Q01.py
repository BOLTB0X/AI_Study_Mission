num_list = [1,5,7,15,16,22,28,29]

def get_odd_num(num_list):
    ret = []
    for num in num_list:
        #홀수 인 경우
        if (num % 2 != 0):
            ret.append(num)
    
    return ret

print(get_odd_num(num_list)) # [1, 5, 7, 15, 29]