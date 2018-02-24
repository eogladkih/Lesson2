
#1-2
names=["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

def find_person(name):

    while names:
        if names.pop() == name:
            print(name +" нашелся.")

find_person("name")


#3 
def ask_user():
    while True:
        answer=input("Как дела?")
        if answer=="Хорошо":
            break
ask_user()

#4
#не поняна суть задания