# Biésów Smãtk

num = None
while num is float or int: #loop until user input numeric literal
    try:
        num = float(input('Wprowadzë lëczbã: '))
    except ValueError: # I can do exceptions YAY!
        print('To nie je lëczba.')
    else:
        print('Môsz wprowadzoné lëczbã', num)
        break