#
# Example file for working with classes
#
class my_class():
    def method1(self):
        print("my class method 1")

    def method2(self, string):
        print("my class method21" + string)


def main():
    c = my_class()
    c.method1()
    c.method2("This is a string")




if __name__ == "__main__":
    main()
