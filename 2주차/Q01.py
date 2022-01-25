# test score, mid = 50, final = 75

class Score():
    #클래스 선언시 제일 먼저 초기화
    #사용할 인스턴스는 2개
    def __init__(self, mid, final):
        self.__mid = mid  #private __
        self.__final = final #private __
    
    #private를 걸어나서 데코레이터인 @property를 사용
    @property
    def mid(self):
        return self.__mid
    @property
    def final(self):
        return self.__final
    
score = Score(50, 75)
print((score.mid + score.final) / 2)