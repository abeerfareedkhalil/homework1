# السؤال الثالث
file="infile.txt"
def read(path):
    infile=open(path,'r')
    s=infile.read()
    #الأسئلة تفصل بينها وبين الأجوبة ,
    l=s.split(',')
    infile.close()
    #الفهارس الزوجية أسئلة والفردية أجوبة
    questions,asnwers=[],[]
    for i in range(len(l)):
        if i%2==0:
            questions.append(l[i])
        else:
            asnwers.append(l[i])
    return (questions,asnwers)
name=input("enter your name\n")
print("s=hello word\nanswer a questions")
true=0
q,a=read(file)
for i in range(len(q)):
    print(q[i])
    s=input('')
    if s==a[i]:
        true+=1
print(true, "is true")
outfile=open("outfile.txt",'w')
outfile.writelines(name)
outfile.writelines("/n")
outfile.writelines(str(true))
outfile.close()