#Exception Handling
def divide(x,y):
    return x/y
print(divide(5,0))

def divide(x,y):
    return x/y
print(divide(5,'0'))


def divide(x,y):
    try:
        # return x/y
        result = x/y
    except ZeroDivisionError:
        print("Zero Division error occured: ")

    except TypeError:
        print("Value Error occured")

    except Exception as e:
        print(f"Exception occured: {e}")
    
    else:
        print(f"Result = {result}")

    finally:
        print("Execution Completed")
    
# print(divide(5,'0'))
# print(divide(5,2))
# print(divide(5,0))
divide(2,0)

Reading, writing and Opening file
file = open("sample.txt" , "r")
content = file.read()
content = file.readline()
print(content)
print(content.strip())

file = open("sample.txt" , "r")
print(file.readline())
print(file.readline())
print(file.readlines())
file.close()
print(file)

with open('sample.txt') as file:
    print(file.read())
    print(file.readline())

    for line in file:
        print(line)

    for i, line in enumerate(file):
        print(f"{i} ---- {line}")

print(file)