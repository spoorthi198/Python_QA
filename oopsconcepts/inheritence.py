class A:

    def __init__(self):
        print('i am in class A ')

class B(A):


    def __init__(self):
        super().__init__()
        print('i am in class B ')


class C(B):

    def __init__(self):
        super().__init__()
        print('i am in class C ')


objc = C()