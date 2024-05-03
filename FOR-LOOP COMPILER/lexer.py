import ply.lex as lex

# Define reserved keywords and their token types
reserved = {
    'for': 'FOR',
    'in': 'IN',
    'range': 'RANGE'
}

# List of token names
tokens = [
    'FOR',
    'IN',
    'RANGE',
    'IDENTIFIER',
    'NUMBER',
    'COLON',
    'LPAREN',
    'RPAREN',
    'COMMA'
]

# Token definitions  #used to identify a specific token type
t_COLON = r':'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_NUMBER = r'\d+'

# Ignored characters (spaces and tabs)
t_ignore = ' \t'

# Function to handle identifiers and keywords
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*' #a letter or underscore, followed by letters, digits, or underscores.

    # If the identifier matches a reserved keyword, return the keyword's token type
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

# Handling newlines
# track newlines in the input
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)  # Track line numbers

# Error handling in the lexer
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Build the lexer
#lexer object from the defined token patterns and functions.
lexer = lex.lex()

# Test the lexer to ensure it outputs the correct tokens
if __name__ == "__main__":
    data = '''
    for i in range(0, 10):
        print(i)
    '''
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)  # Ensure correct tokenization



