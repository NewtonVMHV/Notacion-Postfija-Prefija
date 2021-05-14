class notationConversion():
    def __init__(self, notation):
        self.operators = ['+', '-', '*', '/', '^']
        self.lOrg = ['{', '[', '(']
        self.rOrg = ['}', ']', ')']
        self.isBadNotation = False
        self.notation = self.setFormat(notation)

    def setFormat(self, notation):
        newNotation = []
        for i in notation:
            if i is not ' ':
                newNotation.append(i)
        self.isBadNotation = self.checkNotation(newNotation)
        return newNotation

    def checkNotation(self, notation):
        stackBrackets = []
        for i in notation:
            if i in self.lOrg:
                stackBrackets.append(i)
            elif i in self.rOrg:
                if len(stackBrackets) is not 0:
                    if self.isBracketsClosed(ord(stackBrackets[-1]), ord(i)):
                        stackBrackets.pop()
                    else:
                        # error por si el ultimo valor de la pila no es pareja del Bracket de cierre
                        stackBrackets.append(i)
                else:
                    # error por si alguien mete primero un rOrg
                    stackBrackets.append(i)
        if len(stackBrackets) is 0:
            return False
        else:
            return True

    def isBracketsClosed(self, stackLastCharacter, currentCharacter):
        # {}
        if stackLastCharacter is 123 and currentCharacter is 125:
            return True
        # ()
        elif stackLastCharacter is 40 and currentCharacter is 41:
            return True
        # []
        elif stackLastCharacter is 91 and currentCharacter is 93:
            return True
        else:
            return False

    def rulesOperators(self, op1, op2):
        levelOperatorts = [["+", "-"], ["*", "/"], ["^"]]
        op1 = [op1]
        op2 = [op2]
        for i in range(0, len(levelOperatorts)):
            if op1[0] in levelOperatorts[i]:
                op1.append(i)
            if op2[0] in levelOperatorts[i]:
                op2.append(i)
        if op1[1] == op2[1]:
            return 1
        elif op1[1] > op2[1]:
            return 2
        elif op1[1] < op2[1]:
            return 3

    def infixToPostfix(self):
        stack = []
        postNotation = []
        if self.isBadNotation:
            return "Tu expresion infija esta mal escrita, revisala por favor."
        for token in self.notation:
            # Checamos que no este vacia la pila
            if len(stack) is 0:
                # Checamos que sea un operando
                if not ((token in self.operators) or (token in self.lOrg) or (token in self.rOrg)):
                    postNotation.append(token)
                # Checamos que sea un operador
                elif token in self.operators:
                    stack.append(token)
                # Checamos que sea un parentesis, llave o corcherte izquierdo o de apertura
                elif token in self.lOrg:
                    stack.append(token)
                # Checamos que sea un parentesis, llave o corcherte derecho o de cierre
                elif token in self.rOrg or token in self.operators:
                    return "Tu expresion infija esta mal escrita, revisala por favor."
            else:
                # Si el token es un operando
                if not ((token in self.operators) or (token in self.lOrg) or (token in self.rOrg)):
                    postNotation.append(token)
                # Si el token es un operador
                elif token in self.operators:
                    wasStacked = False
                    while not wasStacked:
                        # Regla 1: operator = last operator in stack
                        # Regla 3: operator < last operator in stack
                        if len(stack) == 0 or stack[-1] in self.lOrg:
                            stack.append(token)
                            wasStacked = True
                        # if 1 == self.rulesOperators(token,stack[-1]) or 3 == self.rulesOperators(token,stack[-1]):
                        elif self.rulesOperators(token, stack[-1]) in (1, 3):
                            # Se saca el ultimo operador de la pila y se agrega a la postija
                            postNotation.append(stack.pop())
                        # Regla 2: operator > last operator in stack
                        elif 2 == self.rulesOperators(token, stack[-1]):
                            stack.append(token)
                            wasStacked = True
                # Si el token es una llave de aperuta
                elif token in self.lOrg:
                    stack.append(token)
                # Si el token es una llave de cierre
                elif token in self.rOrg:
                    bracketFoundIt = False
                    # Crear funcion para buscar el lOrg par del token
                    while not bracketFoundIt:
                        # Sacamos la llave izquierda y cambiamos el valor de bracketFoundIt para salir del while
                        if self.isBracketsClosed(ord(stack[-1]), ord(token)):
                            stack.pop()
                            bracketFoundIt = True
                        # Sacamos el operador que esta hasta arriba de la pila y lo guardamos en expresion postfija
                        else:
                            postNotation.append(stack.pop())
        # Si al final aun hay operadores en la pila los vaciamos en la expresion postfija
        while len(stack) is not 0:
            postNotation.append(stack.pop())
        return postNotation

    def infixToPrefix(self):
        stack = []
        preNotation = []
        if self.isBadNotation:
            return "Tu expresion infija esta mal escrita, revisala por favor."
        for token in self.notation[::-1]:
            # Checamos que no este vacia la pila
            if len(stack) is 0:
                # Checamos que sea un operando
                if not ((token in self.operators) or (token in self.lOrg) or (token in self.rOrg)):
                    preNotation.append(token)
                # Checamos que sea un operador
                elif token in self.operators:
                    stack.append(token)
                # Checamos que sea un parentesis, llave o corcherte derecho o de cierre
                elif token in self.rOrg:
                    stack.append(token)
                # Checamos que sea un parentesis, llave o corcherte izquierdo o de apertura
                elif token in self.lOrg or token in self.operators:
                    return "Tu expresion infija esta mal escrita, revisala por favor."
            else:
                # Si el token es un operando
                if not ((token in self.operators) or (token in self.lOrg) or (token in self.rOrg)):
                    preNotation.append(token)
                # Si el token es un operador
                elif token in self.operators:
                    wasStacked = False
                    while not wasStacked:
                        # Regla 1: operator = last operator in stack
                        # Regla 3: operator < last operator in stack
                        if len(stack) == 0 or stack[-1] in self.rOrg:
                            stack.append(token)
                            wasStacked = True
                        # if 1 == self.rulesOperators(token,stack[-1]) or 3 == self.rulesOperators(token,stack[-1]):
                        elif self.rulesOperators(token, stack[-1]) in (1, 3):
                            # Se saca el ultimo operador de la pila y se agrega a la pretija
                            preNotation.append(stack.pop())
                        # Regla 2: operator > last operator in stack
                        elif 2 == self.rulesOperators(token, stack[-1]):
                            stack.append(token)
                            wasStacked = True
                # Si el token es una llave de cierre
                elif token in self.rOrg:
                    stack.append(token)
                # Si el token es una llave de apertura
                elif token in self.lOrg:
                    bracketFoundIt = False
                    # Crear funcion para buscar el rOrg par del token
                    while not bracketFoundIt:
                        # Sacamos la llave derecha y cambiamos el valor de bracketFoundIt para salir del while
                        if self.isBracketsClosed(ord(token), ord(stack[-1])):
                            stack.pop()
                            bracketFoundIt = True
                        # Sacamos el operador que esta hasta arriba de la pila y lo guardamos en expresion prefija
                        else:
                            preNotation.append(stack.pop())
        # Si al final aun hay operadores en la pila los vaciamos en la expresion prefija
        while len(stack) is not 0:
            preNotation.append(stack.pop())
        return preNotation[::-1]

    def postfixToInfix(self):
        stack = []
        for character in self.notation:
            if character in self.operators:
                aux1 = stack.pop()
                aux2 = stack.pop()
                stack.append("(" + aux2 + character + aux1 + ")")
            else:  # Apilo caracteres
                stack.append(character)
        while len(stack) >= 2:
            aux1 = stack.pop()
            aux2 = stack.pop()
            stack.append("" + aux2 + aux1)
        return stack.pop()

    def postfixToPrefix(self):
        notaInfix = notationConversion(self.postfixToInfix())
        return notaInfix.infixToPrefix()