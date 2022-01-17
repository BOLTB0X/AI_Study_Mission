inputs = "cat32dog16cow5"

def find_string(input):
    str_list = []
    tmp = ""
    for i in range(len(input)):
        if input[i].isdigit():
            if len(tmp)!=0:
                str_list.append(tmp)
            tmp = ""
            continue
        else:
            tmp += input[i]
            
    if len(tmp) != 0:
        str_list.append(tmp)
    
    return str_list

string_list = find_string(inputs)
print(string_list)