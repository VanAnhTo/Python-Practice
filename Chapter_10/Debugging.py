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

#Don’t Debug with print()

#Logging Levels
#logging.debug(): The lowest level. Used for small details. Usually you care about these messages only when diagnosing problems.
#logging.info(): Used to record information on general events in your program
                # or confirm that things are working at their point in the program.
#logging.warning(): Used to indicate a potential problem that doesn’t prevent
                # the program from working but might do so in the future.
#logging.error(): Used to record an error that caused the program to fail to do something.
#logging.critical(): The highest level.
                # Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely.
'''
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')
'''

#***The benefit of logging levels is that you can change what priority of logging message you want to see

#Disabling Logging
#**logging.disable() a logging level
#So if you want to disable logging entirely, just add logging.disable(logging.CRITICAL) to your program
'''
logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.critical('Critical error! Critical error!')
logging.disable(logging.CRITICAL)
logging.critical('Critical error! Critical error!')
logging.error('Error! Error!')
'''
#***logging.disable() will disable all messages after it

#Logging to a File

logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')



