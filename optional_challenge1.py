
# This is a program with two compilation errors, a runtime error and a logical error

# This program displays the details of my pet dog


pet_name = "Hush"
pet_food = ['water','meat','bones','eggs','tuna'] 
age = 60            # LogicalError Dogs can't live for 60 years
pet_home = "kennel  # SyntaxError unterminated string literal it occurs due to the quotation missing
my_pet = f" {pet_name} is {age} and it lives in {pet_home} eats {pet_food[5]}"  # RuntimeError as IndexError: list index out of range,it occurs we called index 5 which is not in the list
print my_pet        # SyntaxError print statement missing parenthesis
