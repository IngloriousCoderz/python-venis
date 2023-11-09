class E:
    e = 5


class D:
    d = 4

    def f(self):
        self.d


class C:
    c = 3


class B:
    b = 2

    c = C()
    d = D()


class A:
    a = 1

    b = B()
    e = E()


# class A:
#     def __init__(provider):
#     provider.do_service()

# b = B()
# a = A(b)
