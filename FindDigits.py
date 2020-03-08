with open('/home/shiyanlou/Code/String.txt') as f:
    s=f.read()
    m=''
    for i in list(s):
        if i in ['1','2','3','4','5','6','7','8','9','0']:
            m=m+i
    print(m)


