def add(x, y):
    return x+y;
def divide(x, y):
    if y==0:
        print("Error: cannot divide by zero.")
    else:
        return x/y
    
def main():
    print("더하기를 구현해보자. x와 y에 각각 숫자를 입력하라.")

    x = int(input("x > "))
    y = int(input("y > "))
    
    print("%d + %d = %d" % (x, y, add(x, y)))    

    print("나눗셈을 구현해보자. x와 y에 각각 숫자를 입력하라.")

    x = int(input("x > "))
    y = int(input("y > "))
    
    print("%d / %d = %0.3f" % (x, y, divide(x, y)))    

# TODO: add() 함수 정의


if __name__ == "__main__":
    main()

