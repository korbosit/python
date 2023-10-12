# while True:
#     num_one = int(input("Enter first number: "))
#     num_two = int(input("Enter second number: "))
#     res = num_one / num_two
#     print(f"The result of dividing the first number by the second: {res}")
#     question = input("Do you want to continue?: ")
#     if question == "yes":
#         continue
#     break

#  ========================================================================================================================================================

while True:
    try:
        num_one = float(input("Please enter number one: "))
        num_two = float(input("Please enter number two: "))
    except ValueError as e:
        print(e)
        print("You must enter numbers!")
        continue

    print(num_one / num_two)

    answer = input("Do you want to continue? (yes/no): ")
    if answer == 'no':
        break
