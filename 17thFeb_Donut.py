def donuts(count):
    """
    This is test

    >>> donuts(3))
    '3'
    >>> donuts(15)
    'Many'
    
    """
    if(count>10):
        return 'Number of Donuts : Many'
    return 'Number of Donuts :' + str(count)


print(donuts(3))
print(donuts(15))