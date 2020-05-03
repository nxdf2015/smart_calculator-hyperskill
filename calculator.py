
def parse(cmd):
    try:
        return list(map(float,cmd.split(" ")))
    except:
        return False

def get_result(operator,x,y):
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
    return "+" if item.count("-") % 2 == 0 else "-"


def get_items(cmd):
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






def parse_numbers(cmd):

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
    while True:
        cmd=input()
        if cmd=="":
            continue
        elif cmd=="/exit":
            break
        result=parse_numbers(cmd)
        print(get_number(result))

    print("Bye!")


calculator()
