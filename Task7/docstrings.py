def my_function():
    '''Demonstrates docstrings.'''
   
    return None
  
print(my_function.__doc__)
  
 
def my_function(arg1):
    """
    multiple lins.
  
      description of function.
  
    Parameters:
    arg1
  
    Returns:
    int
  
    """
  
    return arg1
  
print(my_function.__doc__)