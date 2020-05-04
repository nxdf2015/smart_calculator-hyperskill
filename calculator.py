from re import match,compile


variables={}

class InvalidExpression(Exception):
    pass

class UnknownVariableException(Exception):
    pass



def parse(cmd):
    """
    if cmd is a number return number
    else raise exception
    """
    try:
        return list(map(float,cmd.split(" ")))
    except:
        return False

def get_result(operator ,x ,y ):
    """
    x,y : number
    operator : string
    return result of x + (operator) + y
    """
    if operator=="+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator=="*":
        return x * y
    elif operator=="/":
        return x / y


def get_number(item):
    x = float(item)
    if round(x) == x:
        return int(x)
    else:
        return x

def get_operator(item):
    """
    return "+" or "-"
    """
    return "+" if item.count("-") % 2 == 0 else "-"


def get_items(cmd):
   """
   return a list of string , example : "+25-9" -> ["+","25","-","9"]
   """
   i = 0
   items=[]
   cmd=cmd.replace(" ","")
   while len(cmd) > 0:
       temp=[]


       while cmd and cmd[0] in "*+-/":
           temp.append(cmd[0])
           cmd=cmd[1:]

       if temp:
           items.append("".join(temp))
           temp=[]


       while cmd and not cmd[0] in "+-*/":
            temp.append(cmd[0])
            cmd=cmd[1:]

       items.append("".join(temp))

   return items


def eval_expression(cmd):
    """
    evaluate expression

    """
    operator= "+"
    result=0
    for item in get_items(cmd):
            if not item in "+-":
                if is_valid_identifier(item):
                    if item in variables :
                        n = variables[item]
                    else:

                        raise Exception()

                elif match(r"\d+",item):
                    n = get_number(item)

                result =  result=get_result(operator,result,n)
            else:
                operator=get_operator(item)

    return result


def is_assignment(cmd):
    return match("^([^=]+)\s*?=\s*?([^=]+)$",cmd)

def is_valid_identifier(line):
    return match("[a-zA-Z]+$",line)

def is_number(line):
    try:
        float(line)
        return True
    except :
        return False

def is_valid_assignment(line):
    """
    return true if line is a valid expression without parenthesis (stage 3 )
    """
    pattern=r"(\+|-|\*|/)?\s*((\d+|([a-zA-Z]+)|((\d+|[a-zA-Z]+)\s*[+\-\*/]+\s?)+\s*(\d+|[a-zA-Z]+)))$"
    return match(pattern,line) or to_postfix(line)


def set_variable(identifier,assignment):
    variables[identifier]=eval_expression(assignment)

def calculator():
    while True:
        cmd=input().replace(" ","")

        if cmd=="":
            continue

        if cmd.startswith("/"):
            if cmd[1:] == "exit":
                break
            else:
                print("Unknown command")

        elif is_assignment(cmd) :
            identifier,assignement=cmd.split("=")

            if not is_valid_identifier(identifier):
                print("Invalid identifier")
            elif not  is_valid_assignment(assignement):
                print("Invalid assignment")
            else:
                set_variable(identifier,assignement)

        elif cmd.count("=") > 1:
            print("Invalid assignment")

        else:
            try:
                result=eval_infix(cmd)
                print(get_number(result))
            except UnknownVariableException:
                print("Unknown variable")
            except InvalidExpression:
                print("Invalid expression")

    print("Bye!")


def is_value(line):
    return is_valid_identifier(line) or is_number(line)

def is_operator(line):
    return line in ["+","-","*","/"]

def compare_precedence(op1,op2):
    """
    op1 op2 arihmetic operator
    return True if op1  has  highter precedence than op2
        else return False

    """
    if op1 in "*/":
        return True
    else:
        return False


def eval_postfix(expression):
    stack=[]

    for item in expression.strip().split(" "):

        if is_value(item.strip()):
            if item in variables:
                value=variables[item]
            else:
                try:
                    value=int(item)
                except:
                    raise UnknownVariableException()
            stack.append(value)

        elif is_operator(item):
            *head ,x,y = stack
            stack=head
            head.append(get_result(item,x,y))

    return stack.pop()



def to_postfix(expression):
    result=""
    stack=[]

    for item in expression:

        if is_value(item):
            result+=item

        elif item=="(":
            stack.append(item)

        elif item==")":
            valid=False

            if not "(" in stack:
                raise InvalidExpression()
            while len(stack)>0:
                v = stack.pop()
                if v == "(":
                    valid=True
                    break
                else:
                    result+=" "+v+" "

            if not valid:
                raise InvalidExpression()

        elif   is_operator(item):

            result+=" "
            if not stack:
                stack.append(item)
            elif stack[-1]=="(":
                stack.append(item)
            elif compare_precedence(item,stack[-1]):
                stack.append(item)
            else:
                while stack and not (stack[-1] == "(" or  compare_precedence(item,stack[-1])):
                    v=stack.pop()
                    result+=" "+v+" "
                stack.append(item)

    if "("in stack:
        raise InvalidExpression()
    while stack:
        result+= " "+stack.pop()
    return  result

def reduce_expression(expression):
    """
    return a reduce valid expression : 1++++2--3+-4  -> 1 + 2 + 3 - 4
    """
    operator=compile("[\+\-]+")
    items=get_items(expression)

    for i,item in enumerate(get_items(expression)):
        if operator.match(item):
            items[i]= "+" if item.count("-") % 2 == 0 else "-"

    return "".join(items)



def eval_infix(expression):
    """
    evaluate aithmetic expression with parenthesis
    """
    postfix_expression=to_postfix(reduce_expression(expression))
    return eval_postfix(postfix_expression)

calculator()
