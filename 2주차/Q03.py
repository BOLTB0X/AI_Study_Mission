file_path = "C:\VScode\코칭스터디\data-01-test-score.csv"

#메소드
def read_file(fpath):
    f = open(fpath, encoding= "utf-8")
    datas = f.readlines()
    
    arr= []
    for data in datas:
        data = data.strip()
        d = data.split(",")
        arr.append(d)
        
    f.close()
    
    return arr