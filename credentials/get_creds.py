def open(file,mode='r',buffering=-1):
    import __builtin__    #use import builtins for Python 3.x
    import os.path
    filePath = os.path.join(os.path.dirname(__file__),file)
    return __builtin__.open(filePath,mode,buffering)


def get_credentials():
    import os
    res = {}
    print "SETUP OPTIONS FOR PRIME"
    if 'ChatExchangeU' in os.environ:
        res['user'] = os.environ['ChatExchangeU']
    else: 
        res['user'] = raw_input('Enter your Stack Overflow email ID: ')
    
    if 'ChatExchangeP' in os.environ:
        res['pass'] = os.environ['ChatExchangeP']
    else:
        res['pass'] = (raw_input('Enter your Stack Overflow password: '))
        
    if 'RoomID' in os.environ:
        res['room'] = (os.environ['RoomID'])
    else:
        res['room'] = (raw_input('Enter the ID of the room you wish to enter: '))
                   
    if 'HostSite' in os.environ:
        res['host'] = (os.environ['HostSite'])
    else:
        import json
        hosts = json.loads(open('hosts.json').read())
        for i in range(1, len(hosts)+1):
            print i, hosts[str(i)]
        try:
            res['host'] = hosts[raw_input("Enter the host site for Prime: ").strip()]

        except KeyError:
            res['host'] = "invalid" 
    return res


