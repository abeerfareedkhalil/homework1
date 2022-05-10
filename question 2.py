# السؤال الثاني
num=int(input('enter a decimal  '))
l=[]
while True:
    l.append(num%2)
    num//=2
    if not num:
        break
l.reverse()
for i in range(len(l)):
    l[i]=str(l[i])
binary=''.join(l)
print(binary)
