import traceback
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

#Raising Exceptions
#a raise statement consists of :
    #1. The raise keyword
    #2. A call to the Exception() function
    #3.A string with a helpful error message passed to the Exception() function
'''
raise Exception('This is the error message.-----')
'''
#Using the try and except statements,
# you can handle errors more gracefully instead of letting the entire program crash.

#Getting the Traceback as a String
'''
try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')
'''

#Assertions
#an assert statement consists of :
    #1.The assert keyword
    #2.A condition (that is, an expression that evaluates to True or False)
    #3.A comma
    #4.A string to display when the condition is False
'''
podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
'''
#“I assert that this condition holds true, and if not, there is a bug somewhere in the program.”


#Using an Assertion in a Traffic Light Simulation
'''
market_2nd = {'ns': 'green', 'ew': 'red'} #Market Street and 2nd Street,
mission_16th = {'ns': 'red', 'ew': 'green'} #Mission Street and 16th Street

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)

switchLights(market_2nd)
'''

#Disabling Assertions
#Assertions are for development, not the final product.

#Logging
#Using the logging Module



