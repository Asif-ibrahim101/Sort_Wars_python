import random
import os


##################################################################
# Generating the datasets

# Generating random datasets
def generate_random_dataset(size):
    return [random.randint(100000, 999999) for _ in range(size)]

# generating reversed datasets
def generate_reverse_dataset(size):
    # Generate sorted list of random numbers first
    numbers = generate_random_dataset(size)
    return sorted(numbers, reverse=True)


# Saving the datasets in the datasets foulder
def save_dataset(data, filename):
  
    os.makedirs('datasets', exist_ok=True)
    filepath = os.path.join('datasets', filename)
    
    with open(filepath, 'w') as f:
        for number in data:
            f.write(f"{number}\n")

####################################################################
# implementing algorithms quick_sort and merge_sort

# Merge Sort


def main():
    # Dataset sizes
    sizes = [10000, 100000]
    
    # Generate and save random datasets
    for size in sizes:
        random_data = generate_random_dataset(size)
        save_dataset(random_data, f'random_{size}.txt')
        print(f"Generated random dataset with {size} elements")
        
        reverse_data = generate_reverse_dataset(size)
        save_dataset(reverse_data, f'reverse_{size}.txt')
        print(f"Generated reverse-ordered dataset with {size} elements")

if __name__ == "__main__":
    main()