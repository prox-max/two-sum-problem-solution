def step_ans(x):
     l=[1,2,3,4,5,6,7,8,9,10]
     for i in range(0,len(l)):
          for j in range(1,len(l)):
              if l[i] + l[j] == x:
                  print(f"The two numbers are {l[i]} and {l[j]}") 
l=[1,2,3,4,5,6,7,8,9,10]
print(l)
num=int(input("Enter Sum You Want:"))
step_ans(num)
