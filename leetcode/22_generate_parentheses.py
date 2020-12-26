class Sol(object):
    def generateParenthesis(self, n):
        result = []
        self.generate([], n, n, result)
        return result


    def generate(self, prefix, left, right, result):
        if left == 0 and right == 0:
            result.append("".join(prefix))
        if left != 0:
            self.generate(prefix + ['('], left-1, right, result)
        if right > left:
            self.generate(prefix + [')'], left, right-1, result)


s = Sol()
print("n = 0 ->", s.generateParenthesis(0))
print("n = 1 ->", s.generateParenthesis(1))
print("n = 3 ->", s.generateParenthesis(3))
print("n = 5 ->", s.generateParenthesis(5))