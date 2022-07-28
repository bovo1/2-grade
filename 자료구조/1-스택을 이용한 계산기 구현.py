class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0

def get_token_list(expr):
	expr = expr.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').replace('^', ' ^ '). replace('(', ' ( ').replace(')', ' ) ').replace('  ', ' ').strip()
	expr = expr.split()
		
	return expr
	
	
def infix_to_postfix(token_list):    
          
    opstack = Stack()
    outstack = []
        
        # 연산자의 우선순위 설정
    prec = {}
    prec['('] = 0
    prec['+'] = 1
    prec['-'] = 1
    prec['*'] = 2
    prec['/'] = 2
    prec['^'] = 3

    for token in token_list:
        if token == '(':
            opstack.push(token)
            
        elif token == ')':
            while opstack.top() != '(':
                outstack.append(opstack.pop())
            opstack.pop()

        elif token in '+-/*^':
            if opstack.isEmpty() == True:
                opstack.push(token)
            elif prec[token] > prec[opstack.top()]:
                opstack.push(token)
            else:
                while prec[opstack.top()] >= prec[token]:
                    outstack.append(opstack.pop())
                    if opstack.isEmpty() == True: break
                opstack.push(token)
                
        else: # operand일 때
            outstack.append(token)

    # opstack 에 남은 모든 연산자를 pop 후 outstack에 append
    while opstack.isEmpty() == False:
        outstack.append(opstack.pop())
    return outstack


def compute_postfix(token_list):
	S = Stack()
	
	for token in token_list:
		if token in '+-/*^':
			a = float(S.pop())
			b = float(S.pop())
			
			if(token == '+'):
				S.push(b+a)
			elif(token == '-'):
				S.push(b-a)
			elif(token == '*'):
				S.push(b*a)
			elif(token == '/'):
				S.push(b/a)
			else:
				S.push(b**a)
		else:
			S.push(token)
	
	return float(S.top())
	
	
# 아래 세 줄은 수정하지 말 것!
expr = input()
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)
