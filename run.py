import sys
import urllib2
import json
import socket

execfile('inc/bcolors.py')
execfile('inc/helpers.py')


print bcolors.OKBLUE + """ 

     _                    _   _               ____          ___ ____  
    | |    ___   ___ __ _| |_(_) ___  _ __   | __ ) _   _  |_ _|  _ \ 
    | |   / _ \ / __/ _` | __| |/ _ \| '_ \  |  _ \| | | |  | || |_) |
    | |__| (_) | (_| (_| | |_| | (_) | | | | | |_) | |_| |  | ||  __/ 
    |_____\___/ \___\__,_|\__|_|\___/|_| |_| |____/ \__, | |___|_|    
                                                    |___/             

    _____________________________________________________________________
    """ + bcolors.ENDC


# Getting the arguments
arguments = sys.argv

if arguments[1] == '--help':
    show_help()
else:
    ip_address = arguments[1]

    # If valid IP - get information
    if validate_ip(ip_address):
        get_data(ip_address)
    else:
        show_error_msg()
