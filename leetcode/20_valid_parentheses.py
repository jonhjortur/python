class Solution(object):
    def is_valid(self, s) -> object:
        stack = []
        paren_lookup = {")": "(", "}": "{", "]": "["}

        for p in s:
            if p in paren_lookup.values():
                stack.append(p)
            elif stack and paren_lookup[p] == stack[-1]:
                stack.pop()
            else:
                return False

        return stack == []


sol = Solution()
test_strings = {"good_1": "", "good_2": "[]", "good_3": "({[]()}{}[{}])",
                "bad_1": "((", "bad_2": "({)}", "bad_3": '({[)}]'}

for key in test_strings:
    print(f"{key}: {test_strings[key]} == {sol.is_valid(test_strings[key])}")
