
def parse(cmd):
    try:
        return list(map(float,cmd.split(" ")))
    except:
        return False


while True:
    cmd=input()
    if cmd=="":
        continue
    numbers=parse(cmd)

    if not numbers or cmd=="/exit":
        break
    value = sum(numbers)

    if round(value) == value:
        print(int(value))
    else:
        print(value)
print("Bye!")

