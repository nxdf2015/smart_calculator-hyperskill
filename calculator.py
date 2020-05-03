from re import match,compile


variables={}


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

       while cmd and cmd[0] in "+-":
           temp.append(cmd[0])
           cmd=cmd[1:]

       if temp:
           items.append("".join(temp))
           temp=[]

       while cmd and not cmd[0] in "+-":
            temp.append(cmd[0])
            cmd=cmd[1:]
       items.append("".join(temp))
   return items


def eval_expression(cmd):
    """
    evaluate expression45

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

def is_valid_assignment(line):
    pattern=r"(\+|-)?\s*((\d+|([a-zA-Z]+)|((\d+|[a-zA-Z]+)\s*[+-]+\s?)+\s*(\d+|[a-zA-Z]+)))$"
    return match(pattern,line)




def set_variable(identifier,assignment):
    variables[identifier]=eval_expression(assignment)

def calculator():
    expression = compile(r"(\+|-)?\s*(\d+|(\d+\s*[+-]+\s?)+\s*\d+)$")
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

        elif is_valid_assignment(cmd):
            try:
                result=eval_expression(cmd)
                print(get_number(result))
            except:
                print("Unknown variable")

        else:
            print("Invalid expression")

    print("Bye!")

calculator()

