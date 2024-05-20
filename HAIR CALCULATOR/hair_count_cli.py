import math
import time

def total_hair_in_scalp(circumference, hair_density):
    radius = circumference / (2 * math.pi)
    surface_area = 2 * math.pi * radius**2
    total_hairs = surface_area * hair_density
    return total_hairs

# Function to print text with animation
def print_with_animation(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Main function to get user input and call the calculation function
def main():
    print("Enter the circumference of the scalp (in cm): ", end='', flush=True)
    circumference = float(input())
    print("Enter the total hair in 1 cm square area: ", end='', flush=True)
    hair_density = int(input())

    # Display the entire process in an arranged format with animation
    print("\nEntire Process:")
    print_with_animation("1. Calculate the radius:")
    time.sleep(0.3)
    print_with_animation("\tRadius = Circumference / (2 * π)")
    time.sleep(0.3)
    print_with_animation("\tRadius = {:.2f} / (2 * π)".format(circumference))
    time.sleep(0.3)
    print_with_animation("\tRadius ≈ {:.2f} cm".format(circumference / (2 * math.pi)))
    time.sleep(0.3)

    print_with_animation("\n2. Calculate the surface area of the scalp (hemisphere):")
    time.sleep(0.3)
    print_with_animation("\tSurface Area = 2 * π * Radius^2")
    time.sleep(0.3)
    radius = circumference / (2 * math.pi)
    surface_area = 2 * math.pi * radius**2
    print_with_animation("\tSurface Area = 2 * π * {:.2f}^2".format(radius))
    time.sleep(0.3)
    print_with_animation("\tSurface Area ≈ {:.2f} cm²".format(surface_area))
    time.sleep(0.3)

    print_with_animation("\n3. Calculate the total number of hairs:")
    time.sleep(0.3)
    print_with_animation("\tTotal Hairs = Surface Area * Hair Density")
    time.sleep(0.3)
    total_hairs = surface_area * hair_density
    print_with_animation("\tTotal Hairs ≈ {:.0f} hairs".format(total_hairs))
    time.sleep(0.3)

    # Display the result
    print("\nTotal number of hairs in the scalp: {:.0f} hairs".format(total_hairs))

if __name__ == "__main__":
    main()
