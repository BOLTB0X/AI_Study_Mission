file_path = "C:\VScode\코칭스터디\data-01-test-score.csv"

#클래스 선언
class Readcsv():
    def __init__(self, fpath):
        self.fpath = fpath
        self.rfile = self.read_file()
        
    def read_file(self):
        f = open(self.fpath, encoding= "utf-8")
        datas = f.readlines()
    
        arr= []
        for data in datas:
            data = data.strip()
            d = data.split(",")
            #쪼갠 set을 list로
            tmp = []
            for sp_d in d:
                tmp.append(int(sp_d))
            arr.append(tmp)
        
        f.close()
    
        return arr

    def merge_list(self):
        merge_arr = []
        for data in self.rfile:
            merge_arr.append(sum(data))
        
        return merge_arr.sort()
    
read_csv = Readcsv(file_path)
print(read_csv.read_file())
print(read_csv.merge_list())