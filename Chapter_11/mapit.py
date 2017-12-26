
import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    #Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

#address: 870 Valencia St, San Francisco, CA 94110
# to run, open cmd on this folder and type: mapit 870 Valencia St, San Francisco, CA 94110'

