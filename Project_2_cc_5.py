class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __str__(self):
        rest_str = ""
        counter = 0
        for regex in self.pattern:
            if regex == ".":
                if counter != len(self.pattern)-1:
                    rest_str += "dot-"
                else:
                    rest_str += "dot"
            elif regex == "_":
                if counter != len(self.pattern)-1:
                    rest_str += "dash-"
            else:
                rest_str += "dash"
            counter += 1

        return rest_str


class S(Letter):
    def __init__(self):
        pattern = ['.', '_', '.']
        super().__init__(pattern)

print(str(S()))