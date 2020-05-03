from re import match,compile

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
    evaluate expression
    """
    operator= "+"
    result=0
    for item in get_items(cmd):
        try:
            n = get_number(item)

            result = get_result(operator,result,n)
            operator = None
        except:
            operator=get_operator(item)

    return result







def calculator():
    expression = compile(r"(\+|-)?\s*(\d+|(\d+\s*[+-]+\s?)+\s*\d+)$")
    while True:
        cmd=input()

        if cmd=="":
            continue

        if cmd.startswith("/"):
            if cmd[1:] == "exit":
                break
            else:
                print("Unknown command")


        elif expression.match(cmd):
            result=eval_expression(cmd)
            print(get_number(result))
        else:
            print("Invalid expression")

    print("Bye!")


calculator()
