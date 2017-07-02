class NumString:

    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __mul__(self, other):
            if "." in self.value:
                return float(self.value) * float(other)
            else:
                return int(self.value) * int(other)

    def __rmul__(self, other):
        if "." in self.value:
            return float(self.value) * float(other)
        else:
            return int(self.value) * int(other)


value = NumString(5)

print(2 * value)