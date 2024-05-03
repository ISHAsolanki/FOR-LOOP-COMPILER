import ply.yacc as yacc
import ply.yacc as yacc
from lexer import tokens  # Ensure the lexer tokens are correct

# Define the 'for' loop rule that includes a block of statements
def p_for_loop(p):
    'for_loop : FOR IDENTIFIER IN RANGE LPAREN NUMBER COMMA NUMBER RPAREN COLON statements'
    p[0] = ('for_loop', p[2], p[6], p[8], p[10])

# Define a rule for a block of statements
def p_statements(p):
    'statements : statement'
    p[0] = [p[1]]

def p_statements_more(p):
    'statements : statements statement'
    p[0] = p[1] + [p[2]]

# Define a rule for function call statements (like 'print(i)')
def p_statement_function_call(p):
    'statement : IDENTIFIER LPAREN IDENTIFIER RPAREN'
    p[0] = ('function_call', p[1], p[3])

# Error handling in the parser
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' on line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Test the parser with a 'for' loop and a print statement
if __name__ == "__main__":
    data = '''
    for i in range(0, 10):
        print(i)
    '''
    result = parser.parse(data)
    print("Parse Result:", result)



