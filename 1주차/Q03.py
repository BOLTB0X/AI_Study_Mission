score = [(100,100),(95,90),(55,60),(75,80),(70,70)]

def get_avg(score):
    idx  = 1;
    for s in score:
        print("%d 번, 평균 : %.1f" %(idx, (s[0]+s[1])/2))
        idx+=1
    return

get_avg(score)