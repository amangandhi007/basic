def calculate_square_area(side):
    return side ** 2

def calculate_rectangle_area(length, width):
    return length * width

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def print_formulas():
    print("1. Formula for Area of Square:")
    print("   Area = side^2\n")
    
    print("2. Formula for Area of Rectangle:")
    print("   Area = length * width\n")
    
    print("3. Formula for Area of Triangle:")
    print("   Area = 1/2 * base * height\n")

def main():
    print_formulas()
    
    # Ask the user for their choice
    choice = int(input("Choose a shape (1 for Square, 2 for Rectangle, 3 for Triangle): "))
    
    if choice == 1:
        side = float(input("Enter the side length of the square: "))
        area = calculate_square_area(side)
        print(f"The area of the square is: {area}")
        
    elif choice == 2:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = calculate_rectangle_area(length, width)
        print(f"The area of the rectangle is: {area}")
        
    elif choice == 3:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = calculate_triangle_area(base, height)
        print(f"The area of the triangle is: {area}")
        
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()