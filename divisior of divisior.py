def check(x):
    count=0
    if x % 3==0 :
        count=count+1
    return  count



for _ in range(int(input())):
    n = int(input())
    count1=0

    for i in range(1,n+1):
        if n % i==0:
            count1=count1+check(i)

    print(count1)
if __name__ == '__main__':
    pass





