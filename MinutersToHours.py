import sys
def Hours():
    try :
        a=int(sys.argv[1])
        if a<0:
            raise ValueError
        print(a//60,' H,',a%60,' M')
    except ValueError:
        print('Parameter Error')
Hours()

