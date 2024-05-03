from parser import parser  # Ensure correct import path

# Class representing a simple "for" loop
class ForLoop:
    def __init__(self, variable, start, end, body):
        self.variable = variable
        self.start = start
        self.end = end
        self.body = body  # Include the body of the loop

    def __repr__(self):
        return f"FOR {self.variable} FROM {self.start} TO {self.end}, BODY: {self.body}"

# Semantic analysis and intermediate code generation
if __name__ == "__main__":
    data = '''
    for i in range(0, 10):
        print(i)
    '''
    parse_result = parser.parse(data)
    if parse_result[0] == 'for_loop':
        _, var, start, end, body = parse_result  # Ensure correct unpacking
        for_loop = ForLoop(var, start, end, body)  # Include body in the representation
        print("Intermediate Representation:", for_loop)


