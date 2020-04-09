import random

class foodie:
    my_updated_list = []

    def _init_(self, first_n, last_n):
        self.first = first_n
        self.last = last_n
        print("you are welcome to this portal")


    def full_names(self):
        return self.first + "  " + self.last

    def email(self):
        return self.full_names() + '@gmail.com'

    def mummy(self):
        return self.first[:2] + self.last[-2:]

    def passed(self):
        self.my_list = ["ijequay", "wisdom", "ekanah"]
        return self.mummy() + random.choice(self.my_list)

    def user(self):
        self.user = input("Are you okay with the password:")
        if self.user == 'yes':
            print(self.passed())
        else:
            self.user = input("please type in your preferrable password:")
            for i in range(len(self.user)):
                if i >= 7:
                    print(self.user)
                    break
            else:
                self.user = input("please input a longer password:")
            print("Thank you your password has been accepted")

    def containeer(self):
        for i in self.user:
            if i not in foodie.my_updated_list:
                foodie.my_updated_list.append(i)
                return foodie.my_updated_list
        print("Thank you for your time")




f = foodie("ijequay", "wisdom")
print(f.full_names())
print(f.email())
print(f.first)
print(f.last)
print(f.mummy())
print(f.passed())
print(f.user())
print(f.containeer())
