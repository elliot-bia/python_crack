
#C:\Users\Elliot\Desktop\python_req_crack\top10W.txt

f = open("C:/Users/Elliot/Desktop/python_req_crack/simple.txt","r")
get = f.readline()
print(get)



for line in f.readlines():
    print(line.strip())

