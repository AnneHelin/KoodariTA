# MAIN APPLICATION 

# Ask user name
firstName = 'Anne'
likeCats = input('Pidätkö kissoista? (k/e)')
print('Morjensta', firstName)

if likeCats == 'k':
    print('Olet kissaihminen')
    
def nameLength(name):
    """Calculates lenght of the name

    Args:
        name (str): name of the person

    Returns:
        int: lenght of the name
    """
    lenght = len(name)
    return lenght  

# Calculate name lenght
length = nameLength(firstName)
print(firstName, 'sanassa on', length, 'kirjainta')
