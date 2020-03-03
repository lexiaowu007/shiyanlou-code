n=input('enter students:')
i=1
data={}
while i <=int(n):
    data.setdefault('name',[]).append(input('Please enter name:'))
    data.setdefault('Physics',[]).append(input('Please enter PG:'))
    data.setdefault('Math',[]).append(input('Please enter MG:'))
    data.setdefault('History',[]).append(input('Please enter HG:'))
    if int(data['Physics'][i-1])+int(data['Math'][i-1])+int(data['History'][i-1])<120:
        data.setdefault('Result',[]).append('failed')
    else:
        data.setdefault('Result',[]).append('passed')
    i+=1
i=0
while i<int(n):
    print(data['name'][i],data['Physics'][i],data['Math'][i],data['History'][i],data['Result'][i])
    i+=1
