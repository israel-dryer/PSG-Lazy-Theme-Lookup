import PySimpleGUI as sg

# def change_look_and_feel(theme):
#     values = [item.lower() for item in sg.list_of_look_and_feel_values()]
#     theme = theme.replace(' ', '').lower()
#     ix = values.index(theme)
#     selection = sg.list_of_look_and_feel_values()[ix]
#     print(selection)

# change_look_and_feel('tan blue')


def change_look_and_feel(theme):
    # normalize available l&f values
    lf_values = [item.lower() for item in sg.list_of_look_and_feel_values()]

    # option 1
    opt1 = theme.replace(' ','').lower()
    
    # option 2 (reverse lookup)
    optx = theme.lower().split(' ')
    optx.reverse()
    opt2 = ''.join(optx)
    
    # search for valid l&f name
    if opt1 in lf_values:
        ix = lf_values.index(opt1)
        selection = sg.list_of_look_and_feel_values()[ix]
        print('You have selected', selection) # replace with --> sg.change_look_and_feel(selection)
    elif opt2 in lf_values:
        ix = lf_values.index(opt2)
        selection = sg.list_of_look_and_feel_values()[ix]
        print('You have selected', selection) # replace with --> sg.change_look_and_feel(selection)
    else:
        print('That is not a valid look and feel selection')

change_look_and_feel('tan blue')