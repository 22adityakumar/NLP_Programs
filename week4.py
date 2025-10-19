def is_operator(token):
  """Check if the token is a mathematical operator or parenthesis."""
  return token in ['+', '-', '*', '/', '^', '=', '(', ')']

def is_operand(token):
  """Check if the token is a number (possibly decimal) or alphabet (variable)."""
  return token.replace('.', '', 1).isdigit() or token.isalpha()

def tokenize(text):
  """Convert the sentence into individual tokens (operands and operators)."""
  tokens = []
  current = ''
  for ch in text:
    if ch in '+-*/^=()':
      if current:
        tokens.append(current.strip())
        current = ''
        tokens.append(ch)
      elif ch.isalnum() or ch == '.':
        current += ch
      else:
        if current:
          tokens.append(current.strip())
          current = ''
          # Ignoring punctuation/space as a token
    if current:
      tokens.append(current.strip())
  return tokens

def extract_math_expressions(tokens):
  """Extract valid mathematical expressions with at least 3 components (e.g., a=b*c)."""
  expressions = []
  current_expression = []
  
  for token in tokens:
    if is_operand(token) or is_operator(token):
      current_expression.append(token)
    else:
      # End current expression if we hit non-math token
      if len(current_expression) >= 3:
        expressions.append(''.join(current_expression))
        current_expression = []
        if len(current_expression) >= 3:
          expressions.append(''.join(current_expression))
  return expressions

def find_math_expressions(sentence):
  tokens = tokenize(sentence)
  expressions = extract_math_expressions(tokens)
  return expressions

# Example Usage
sentence = "In physics, force is calculated using F=m*a and energy is given by E=m*c^2."
math_expressions = find_math_expressions(sentence)

print("Sentence:", sentence)
print("\nMathematical Expressions found:")
if math_expressions:
  for expr in math_expressions:
    print(expr)
else:
  print("No mathematical expressions found.")







def is_valid_email(email):
  email = email.strip()
  if ' ' in email:
    return False, "Email contains whitespace"
  if email.count('@') != 1:
    return False, "Email must contain exactly one '@' symbol"
  local_part, domain_part = email.split('@')
  if not local_part:
    return False, "Local part is missing"
  if local_part.startswith('.'):
    return False, "Local part cannot start with a dot"
  if '.' not in domain_part:
    return False, "Domain must contain at least one dot (e.g., gmail.com)"
  if domain_part.startswith('.'):
    return False, "Domain cannot start with a dot"
  return True, "Valid email address"

def extract_email_components(email):
  local_part, domain_part = email.split('@')
  domain_parts = domain_part.split('.')
  
  mail_server = domain_parts[0]
  tld = '.'.join(domain_parts[1:])
  return {
    'Local part (Username)': local_part,
    'Mail server': mail_server,
    'Top level domain (TLD)': tld,
    'Full domain': domain_part
    }

#  Main Program
email = input("Enter an email address: ").strip()

valid, message = is_valid_email(email)

if valid:
  print("\n", message)
  components = extract_email_components(email)
  print("Extracted Components:")
  for key, value in components.items():
    print(f"{key}: {value}")
else:
  print("\n Invalid Email:", message)
