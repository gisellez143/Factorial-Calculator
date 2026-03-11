"""
Filename: factorial_calculator.py
Author: <Giselle, Zavala>
Created: <3/6/2026>
Instructor: Holtslander
"""

def factorial():
    # Write your code here
    print("Enter a non negative whole number\n")
    num = int(input)
    factorial = 1
    s = ""
    for i in range(num, 0, -1):
        factorial = factorial * s = s + str(i)
    if i != 1:
        s=s + "*"
        
        print(num)
        print(str(num) + "!=" + s)
        print("Factorial =", factorial)

# You should not need to change any code below this point
def main():
    print("This program computes factorials and displays their intermediate calculations.")
    running = "y"
    while running == "y":
        factorial()
        running = input("Do another calculation? (y/N)\n").lower()
    print("Thank you for using this factorial calculator!")

if __name__ == "__main__":
    main()