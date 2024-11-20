from typing import List

MAX_ELEMENTS = 100

def get_valid_count() -> int:
   """Get a valid number of elements from user input."""
   try:
      count = int(input("Enter the number of elements (1-100): "))
      if not 1 <= count <= MAX_ELEMENTS:
         raise ValueError("Number must be between 1 and 100")
      return count
   except ValueError as e:
      print(f"Invalid input: {e}")
      exit(1)

def get_numbers(count: int) -> List[int]:
   """Get specified number of integers from user input."""
   numbers = []
   print(f"Enter {count} integers:")
   
   for i in range(count):
      try:
         number = int(input())
         numbers.append(number)
      except ValueError:
         print("Invalid input. Please enter valid integers.")
         exit(1)
   return numbers

def calculate_sum(numbers: List[int]) -> int:
   """Calculate sum of numbers in list."""
   return sum(numbers)

def main() -> None:
   """Main program execution."""
   try:
      count = get_valid_count()
      numbers = get_numbers(count)
      total = calculate_sum(numbers)
      print("Sum of the numbers:", total)
   except KeyboardInterrupt:
      print("\nProgram terminated by user.")
      exit(1)

if __name__ == "__main__":
   main()
