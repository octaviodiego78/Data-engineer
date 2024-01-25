##not decorators but useful knowledge about **kwargs


def get_user_name(name: str = "", **kwargs):
    print(name)

user = {"nme":"Diego"}

get_user_name(**user)    #If we have a key in the dict we unpack with the same name as the parameter it will be assigned
                        # if there's no key anything will happen , i't wont brake




#NOW DECORATORS

def decorator(fun): #recieves a function

    def wrapper(*args, **kwargs):   
        return fun(*args, **kwargs) + 1  #does something to the function
    
    return wrapper

@decorator
def add_nums(num1: int, num2: int) -> int:
    return num1 + num2

print(add_nums(5,5))
# print(decorator(add_nums)(5,5)) This is the same as what happen when you use @decorator