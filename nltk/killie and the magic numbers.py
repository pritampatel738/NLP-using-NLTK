fact=[]
fibo=[]

for i in range(2000007):
    fact.append(0)
    fibo.append(0)
fact[1]=1
fibo[0]=fibo[1]=1
for i in range(2,2000007):
    fibo[i]=fibo[i-1]+fibo[i-2]
    fact[i]=fact[i-1]*i

print(fact[100])
print(fibo[100])
