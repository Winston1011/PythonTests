# # customized object
#
# class VOW(object):
#     def __init__(self, text):
#         self.text = text
#     def __enter__(self):
#         self.text = "I say: " + self.text    # add prefix
#         return self                          # note: return an object
#     def __exit__(self,exc_type,exc_value,traceback):
#         self.text = self.text + "!"          # add suffix
#
#
# with VOW("I'm fine") as myvow:
#     print(myvow.text)
#
# print(myvow.text)

class num(object):
    def __init__(self, value):
        self.value = value
    def getNeg(self):
        return -self.value
    def setNeg(self, value):
        self.value = -value
    def delNeg(self):
        print("value also deleted")
        del self.value
    neg = property(getNeg, setNeg, delNeg, "I'm negative")

x = num(1.1)
print(x.neg)
x.neg = -22
print(x.value)
print(num.neg.__doc__)
del x.neg