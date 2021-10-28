def countingdigits(s):
    d = dict(enumerate([0]*10))
    for k,v in d.items():
        if str(k) in s:
            h = s.count(str(k))
            d[k]+=h
            
    for k,v in d.items():
        print(k,v)

if __name__ == "__main__":
    s = str(input())
    countingdigits(s)