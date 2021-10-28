class NoParenthesesException(Exception):
    pass 

class ParenthesesChecker:
    """ Checks if a string contains a balanced parentheses """
    def __init__(self):
        self.p_stack = []
        self.stack_size = 0
        self.parentheses_map = {'{':'}', '(':')', '[':']'}
    
    def is_valid_parentheses(self, char):
        return char in '{([])}'

    def check_validity(self, text):
        for char in text:
            if self.is_valid_parentheses(char):
                if char in self.parentheses_map:
                    # Push to the stack if it is a left parentheses
                    self.p_stack.append(char)   
                else:
                    popped = self.p_stack.pop()
                    if self.parentheses_map[popped] != char:
                        return False 
        return True


if __name__ == '__main__':
    p = ParenthesesChecker()
    print(p.check_validity('(p + {q*a})'))
    print(p.check_validity('[p+(q-a])'))
    print(p.check_validity('(((((((((((((((((((((((((((())))))))))))))))))))))))))))'))
    print(p.check_validity('()[]{}'))