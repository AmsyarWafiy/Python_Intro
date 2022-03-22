class Parent:  # Parent class
    def func1(self):
        print("This function is in parent class.")


# Derived class
class Child(Parent):  # Child class
    def func2(self):
        print("This function is in child class.")


# Driver's code
object = Child()
object.func1()  # Reuse parent class func1()
object.func2()  # Call func2() in child class