def show_help():
    print """
    LocationByIP  version 1.0.0
        usage: python run.py <IP_ADDR>

    _____________________________________________________________________

    Visit: https://github.com/alkhachatryan/locationbyip
    """


def get_data(ip):
    response = json.loads(urllib2.urlopen('http://ip-api.com/json/' + ip).read())
    response_fields = [
        ('as', 'AS'),
        ('city', 'City'),
        ('country', 'Country'),
        ('countryCode', 'Country Code'),
        ('isp', 'ISP'),
        ('lat', 'Latitude'),
        ('lon', 'Longitude'),
        ('org', 'Organisation (Provider)'),
        ('region', 'Region Code'),
        ('regionName', 'Region Name'),
        ('timezone', 'Timezone'),
        ('zip', 'ZIP'),
        ('status', 'Status')
    ]

    for field, title in response_fields:
        print format_row(title, response[field])

    print format_row('Gmap URL', get_gmap_url(response['lat'], response['lon']))

def get_gmap_url(lat, lon):
    return 'https://www.google.com/maps/@%s,%s,15z' % (lat, lon)

def show_error_msg():
    print 'Something went wrong. Try: python run.py --help'

def format_row(title, value):
    return '%s%s: %s%s' % (bcolors.OKGREEN, title, bcolors.ENDC, value)

def validate_ip(addr):
    try:  # IPv4
        socket.inet_aton(addr)
        return True
    except socket.error: pass
    try:  # IPv6
        socket.inet_pton(socket.AF_INET6, addr)
        return True
    except socket.error: pass

    return False