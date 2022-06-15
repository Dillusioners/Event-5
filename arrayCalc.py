from scipy import stats

limit = int(input("Enter the amount of numbers you need in  your array"))
num_list = []
#x = [1,2,3,4,5,6]
x = 0
y = 0
for i in range(limit):
    num = int(input("Enter your number"))
    num_list.append(num)

def mean(c,div):
    div = int(len(num_list))
    for n in range(len(num_list)):
        c = c + num_list[n]
    result = c // div
    print(result, "is  your result")

def median(n):
    if len(num_list) % 2 !=0:
        n = (len(num_list)-1)/2
        print("Your median number in the array is:", num_list[n])
    else:
        n = (len(num_list))/2
        print("Your median value is:", num_list[n], "&",num_list[n+1])

def mode(lst):
     lst = stats.mode(num_list)
     print("mode value is ",lst)

mean()
median()
mode()