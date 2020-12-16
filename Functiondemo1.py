# usage of *args and **kwargs

# *args => results in tuple

def print_name(*args):
    print(args)

print_name("spoorthi","raj","jnanika")

def get_sum(*args):
    print(sum(args))

get_sum(20,45,67,78)

def get_min(*args):
    print(min(args))
get_min(23,5,87,9,12)


def get_max(*args):
    print(max(args))
get_max(23,4,768,876,345)

# *kwargs => results in dictionary

def get_names(**kwargs):
    print(kwargs)

get_names(name = "spoorthi",address="bangalore",phone= 5997)

def hello_world(*args,**kwargs):
    print(args)
    print((kwargs))
    print(kwargs["address"])

hello_world(10,23,46,name="spoorthi",address="bangalore",phone=835098)