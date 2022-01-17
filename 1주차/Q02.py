sentence = "way a is there will a is there Where"

def reverse_sentence(sentence):
    ret = ""
    tmp = []
    #공백 기준 분리
    tmp = list(sentence.split(" "))
    
    #문자열 슬라이딩 이용
    for t in tmp[::-1]:
        ret += t
        ret += ' '
    
    return ret

print(reverse_sentence(sentence)) #Where there is a will there is a way