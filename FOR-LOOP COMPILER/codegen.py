# Ensure proper import of ForLoop from semantic_ir
from semantic_ir import ForLoop

# Function to generate Python code for a given "FOR" loop
def generate_code(for_loop):
    # Initialize an empty list to store lines of code
    code = []
    # Create the "FOR" loop line
    code.append(f"for {for_loop.variable} in range({for_loop.start}, {for_loop.end}):")
    # Add the loop body (assumed to be a simple print statement in this case)
    code.append(f"    print({for_loop.variable})")
    # Return the generated code as a single string with newline separators
    return "\n".join(code)

# Test code generation with a sample "FOR" loop
if __name__ == "__main__":
    # Create a ForLoop object with variable 'i', start 0, end 10
    for_loop = ForLoop('i', 0, 10, [("function_call", "print", "i")])
    # Generate Python code for this loop
    generated_code = generate_code(for_loop)
    # Output the generated code to the console
    print("Generated Code:")
    print(generated_code)
