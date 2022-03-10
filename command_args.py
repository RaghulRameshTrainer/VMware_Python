import argparse

def add_nums(x,y):
    return x+y

def sub_nums(x,y):
    return x-y

def prod_nums(x,y):
    return x*y

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--number1",help="first number")
    parser.add_argument("--number2",help="second number")
    parser.add_argument("--operation",help="operation",choices=["add","sub","mul"])
    args=parser.parse_args()

    print(args.number1)
    print(args.number2)
    print(args.operation)

    n1=int(args.number1)
    n2=int(args.number2)

    if args.operation == "add":
        res=add_nums(n1,n2)
        print("Sum of {} and {} is: {}".format(n1,n2,res))
    elif args.operation == "sub":
        print("Subraction of {} and {} is: {}".format(n1,n2,sub_nums(n1,n2)))
    elif args.operation == "mul":
        print("Product of {} and {} is: {}".format(n1,n2,prod_nums(n1,n2)))
    else:
        print("Unsupported operations")
