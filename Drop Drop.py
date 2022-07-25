'''docstring'''
def main():
    """func doc"""
    num = float(input())
    if num < 1.00:
        print("I'm so sad.")
    elif num < 2.00:
        grade = 4-num
        print("%.2f" %grade)
    else:
        print("I'm so happy.")
main()
