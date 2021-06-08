# Write a program, in any language (incl pseudocode) that iterates the numbers from 1 to 100.
# For any value divisible by 4, the program should print "Go".
# For any value divisible by 5, the program should print "Figure".
# For any value divisible by 4 and 5, the program should print "GoFigure".



def iterates_numbers():
    for value in range(1, 101):
        if value % 4 == 0 and value % 5 == 0:
            print("GoFigure")
        elif value % 4 == 0:
            print("GO")
        elif value % 5 == 0:
            print("Figure")
if __name__ == '__main__':
    iterates_numbers()



