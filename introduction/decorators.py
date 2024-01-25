##not decorators but useful knowledge about **kwargs


def get_user_name(name: str = "", **kwargs):
    print(name)

user = {"nme":"Diego"}

get_user_name(**user)    #If we have a key in the dict we unpack with the same name as the parameter it will be assigned
                        # if there's no key anything will happen , i't wont brake

