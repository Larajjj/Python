# Use of Funtion
def thing():
    print('hello')
    print('fun')
thing()
print('zip')
thing()

# Parameter and arguements
def greet(lang):
    if lang== 'es':
       print('Hola')
    if lang== 'fr':
       print('Bonjour')
    else:
       print('Hello')     


# Return statements
  def greet(lang):
    if lang== 'es':
       return'Hola'
    if lang== 'fr':
       return'Bonjour'
    else:
       return'Hello'   

  
# Multiple parameters/ arguments
def addtwo(a,b):
    added= a+b
    return added
x=addtwo(3.5,4)
print(x)
