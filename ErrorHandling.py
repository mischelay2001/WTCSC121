##User enters input
Length = input('ASK USER FOR INPUT')

##Learn what type of date the user entered

##Input is made up of only letters; aVariable is alpha - True or False
aVariableAlpha = Length.isalpha()
print('aVariableAlpha:', aVariableAlpha)
##Input is made up of only numbers; aVariable is digit - True or False
aVariableDigit = Length.isdigit()
print('aVariableDigit:', aVariableDigit)
##Input is made up numbers and letters; aVariable is alphanumber - True or False
aVariableAlphaNumberic = Length.isalnum()
print('aVariableAlphaNumberic', aVariableAlphaNumberic)
Length = float(Length)
print('Length ', Length)
aVariableFloat = Length>=0
print('aVariableFloat', aVariableFloat)

#Handle invalid user input
#while REQUIRED INPUT DOES NOT MEET NEEDS == False:
while aVariableDigit == False:
            print('ERROR MESSAGE.')
            try:
                Length = input('ASK USER FOR VALID INPUT')
                #Reset Boolean test
                aVariableDigit = Length.isdigit()
            #Program fails if input is alpha or alphanumberic
            #Except if the user's input breaks the code
            except:
                pass

def validate():
    # Validate if user input is an R, P, or S
    raw_data = ""
    boolean_valid_entry = False
    while boolean_valid_entry is False:
        # Initial user input and test
        try:
            raw_data = input('Ask for Raw Data input: ')
            # a_player1 = a_player1.upper()
            if raw_data == "R" or a_player1 == "P" or a_player1 == "S":
                boolean_valid_entry = True
        # Initial input not valid
        # Error message
        except:
            # pass
            print('\nError Message')
