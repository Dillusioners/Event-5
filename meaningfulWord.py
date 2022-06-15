#array containing random words
word_list = ["Air", "Well", "Marker", "Beautiful", "Beat", "Belle Deplhine", "Kill", "star", "Man",
           "Jerk", "Pond", "Beast", "Eminem", "Young", "Mojang", "Technical", "Rose",
           "Aesthetic", "Tired", "Game ", "Crawl", "Never", "Disrupt", "Level", "Base"]
#taking any 3 strings from the user
x = input("Enter your random first string")
y = input("Enter your random second string")
z = input("Enter your random third string")
#Shortening strings down to just the first character
x = x[0]
y = y[0]
z = z[0]
i = 0

for i in range(len(word_list)):
    if x in word_list[i] and y in word_list[i] and z in word_list[i]:
        print("Your word is...", word_list[i])
    else:
        print("Sed:( couldnt find a meaningful word for you maybe try giving a new set of strings??")
