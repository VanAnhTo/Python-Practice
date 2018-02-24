import pyautogui


#Controlling Mouse Movement
'''
print(pyautogui.size())

width, height = pyautogui.size()

print(width)
'''

#Moving the Mouse
#Integer values for the x- and y-coordinates make up the function’s first and second arguments, respectively
#Each movement takes a quarter of a second, as specified by the duration=0.25 keyword argument
'''
for i in range(10):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)
'''
'''
for i in range(10):
    pyautogui.moveRel(100, 0, duration=0.25)
    pyautogui.moveRel(0, 100, duration=0.25)
    pyautogui.moveRel(-100, 0, duration=0.25)
    pyautogui.moveRel(0, -100, duration=0.25)
'''

#Getting the Mouse Position

#Controlling Mouse Interaction
#Clicking the Mouse

pyautogui.click(10, 5)

pyautogui.click(100, 150, button='left')
#will click the left mouse button at the coordinates (100, 150)

