# Terrance Davis
# (TASK 5) The purpose of this section is to check if two files are identical or different and print out the differences in Errors
import pandas as pd 

# Load the Excel file for clarity 


# Define your text files
fn1 = r"C:/Users/Teejay\Desktop/P2 Project Excel/The Lion Goes to War.txt"
fn2 = r"C:/Users/Teejay\Desktop/P2 Project Excel/The Lion Goes to War.txt"
def same(fn1, fn2="TextOutput.txt"):
    # Function that will be used to check if the two files are identical/different
    
    # Open and read both text files to compare them 
    with open(fn1, 'r') as file1:
        data1 = file1.read()  # Read entire file content as a string

    with open(fn2, 'r') as file2:
        data2 = file2.read()  # Read entire file content as a string

    differences = []
    
    # Compare the lengths of the files
    if len(data1) != len(data2): 
        differences.append(f"Different number of characters: {fn1} has {len(data1)} characters, {fn2} has {len(data2)} characters")

    # Compare the characters one by one
    mini_length = min(len(data1), len(data2))  # Find the length of the shorter file
    for i in range(mini_length):
        if data1[i] != data2[i]:  # Compare individual characters
            differences.append(f"The difference at position {i + 1}: '{data1[i]}' != '{data2[i]}'")  # Formatted output

    # Output results
    if not differences:
        print("Identical Files")  
    else: 
        print("Different Files")  

        # Write to Errors.txt pointing out differences
        with open("Errors.txt", "w") as error_file:
            error_file.write("\n".join(differences))  # Write differences to Errors.txt

# Call the function with the defined text files
same(fn1, fn2)
