import operator;
class Evaluate:
  """This class validates and evaluate postfix expression.
  Attributes:
      top: An integer which denotes the index of the element at the top of the stack currently.
      size_of_stack: An integer which represents the size of stack.
      stack: A List which acts as a Stack.
  """
    # Write your code here


  def __init__(self, size):
    """Inits Evaluate with top, size_of_stack and stack.
    Arguments:
      size_of_stack: An integer to set the size of stack.
    """
    self.top = -1
    self.size_of_stack = size
    self.stack = []


  def isEmpty(self):
    """
    Check whether the stack is empty.
    Returns:
      True if it is empty, else returns False.
    """
      # Write your code here
      if self.top == -1:
        return True


  def _pop(self):
    """
    Do pop operation if the stack is not empty.
    Returns:
      The data which is popped out if the stack is not empty.
    """
    # Write your code here
    self.stack.pop()
    self.top-=1
    


  def push(self, operand):
    """
    Push the operand to stack if the stack is not full.
    Arguments:
      operand: The operand to be pushed.
    """
    # Write your code here
    self.operand = operand
    if self.top == self.size_of_stack - 1:
      self.stack.append(self.operand)
      self.top+=1


  def validate_postfix_expression(self, expression):
    """
    Check whether the expression is a valid postfix expression.
    Arguments:
      expression: A String which represents the expression to be validated.
    Returns:
      True if the expression is valid, else returns False.
    """
    # Write your code here
    self.expression = expression
     for i in self.expression:
      if x=="+" or x=="-" or x== "/" or x=="*" or x=="%" or x=="**":
        value1 = self._pop()
        value2 = self._pop()
        dict = {"+" : operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv, "%": operator.mod, "**": operator.pow}
        self.push(dict[x](value2,value1))
      else:
        self.push(int(x))
        
        
    


  def evaluate_postfix_expression(self, expression):
    """
    Evaluate the postfix expression
    Arguments:
      expression: A String which represents the the expression to be evaluated
    Returns:
      The result of evaluated postfix expression.
    """
    # Write your code here
    for i in self.expression:
      if x=="+" or x=="-" or x== "/" or x=="*" or x=="%" or x=="**":
        value1 = self._pop()
        value2 = self._pop()
        dict = {"+" : operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv, "%": operator.mod, "**": operator.pow}
        self.push(dict[x](value2,value1))
      else:
        self.push(int(x))
    return self.stack[0]        


# Do not change the following code
postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')
