import random 

def generate_numbers(number_of_numbers_to_generate):
    return random.sample(range(1,100),number_of_numbers_to_generate)

def Average(lst):
    return sum(lst) / len(lst)

generated_numbers_array = generate_numbers(3)
print("Numbers: ",generated_numbers_array)
print("Average: ",Average(generated_numbers_array))