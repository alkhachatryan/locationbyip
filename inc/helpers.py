def show_help():
    print """
    LocationByIP  version 1.0.0
        usage: python run.py <IP_ADDR> 
    
    _____________________________________________________________________
    
    Visit: https://github.com/alkhachatryan/locationbyip
    """


def get_data(ip):
    response = json.loads(urllib2.urlopen('http://ip-api.com/json/' + ip).read())

    print bcolors.OKGREEN + "AS: " + bcolors.ENDC + response['as']
    print bcolors.OKGREEN + "City: " + bcolors.ENDC + response['city']
    print bcolors.OKGREEN + "Country: " + bcolors.ENDC + response['country']
    print bcolors.OKGREEN + "Country Code: " + bcolors.ENDC + response['countryCode']
    print bcolors.OKGREEN + "ISP: " + bcolors.ENDC + response['isp']
    print bcolors.OKGREEN + "Latitude: " + bcolors.ENDC + str(response['lat'])
    print bcolors.OKGREEN + "Longitude: " + bcolors.ENDC + str(response['lon'])
    print bcolors.OKGREEN + "Organisation (Provider): " + bcolors.ENDC + response['org']
    print bcolors.OKGREEN + "Region Code: " + bcolors.ENDC + response['region']
    print bcolors.OKGREEN + "Region Name: " + bcolors.ENDC + response['regionName']
    print bcolors.OKGREEN + "Timezone: " + bcolors.ENDC + response['timezone']
    print bcolors.OKGREEN + "ZIP: " + bcolors.ENDC + str(response['zip'])
    print bcolors.OKGREEN + "Status: " + bcolors.ENDC + response['status']
    print bcolors.OKGREEN + "Gmap URL:" + bcolors.ENDC + " https://www.google.com/maps/@" + \
          str(response['lat']) + "," + str(response['lon']) + ",15z \n"


def show_error_msg():
    print 'Something went wrong. Try: python run.py --help'


def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True
