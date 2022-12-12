alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # alphabet array

input_value = input() # get input, e.g. A,B,C,$
input_value = input_value.split(",") # turn input string into array
input_value.pop() # remove dollar sign

output = [] # output array

# iterate through each letter in the input
for l in input_value:
    i = alphabet.index(l) + 1 # numerical value of letter
    c = 0 # initialize number of letters to count 
    
    if l in "ABCDE":
        c = i * 2 # Multiply by 2
    elif l in "FGHIJ":
        c = i % 3 * 5 # Divide by 3, multiply the remainder by 5
    elif l in "KLMNO":
        c = int(i / 4) * 8 # Divide by 4, multiply the integer part of the quotient by 8
    elif l in "PQRST":
        # Take the sum of the digits and multiply by 10
        str_i = str(i) # Convert numerical value to string e.g. 12 -> "12"
        sum_var = sum([int(x) for x in str_i]) # convert each member of str_i to an integer, then sum the integers
        c = sum_var * 10 # Multiply by 10
    else:
        # U-Z, find the largest integer factor of numerical value < the value itself and multiply by 12
        # Use a loop to find the largest factor
        lf = 0 # initialize largest factor variable
        for j in range(i - 1, 0, -1):
            if (i % j == 0):
                lf = j
                break
        c = lf * 12
    
    if len(output) == 0: # First letter
        output.append(alphabet[c]) # Count up c letters from A, add it to output
    else: # After first letter
        prev_l = output[-1] # Previously added letter in output array
        prev_i = alphabet.index(prev_l) # index of prev letter
        output.append(alphabet[(prev_i + c) % 26]) # Count up c letters from prev letter, add to output
        # Note the % 26 to wrap around to A if we pass Z
    
output = " ".join(output) # convert output array to string
print(output) # print the output
