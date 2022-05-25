class User:
    def __init__(self, name):
        # two attributes when class is called
        self.name = name
        self.is_logged_in = False


# add unlimited positional and keyword arguments in decorator function
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):     # user is argument at position 0
    print(f"This is {user.name}'s new blog post.")


user0 = User('Hoyt')
user0.is_logged_in = True
create_blog_post(user0)
