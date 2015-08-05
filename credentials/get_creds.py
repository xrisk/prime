def open(file,mode='r',buffering=-1):
    import __builtin__    #use import builtins for Python 3.x
    import os.path
    filePath = os.path.join(os.path.dirname(__file__),file)
    return __builtin__.open(filePath,mode,buffering)


def get_credentials():
    import os
    res = {}
    
    if 'ChatExchangeU' in os.environ:
        res['user'] = os.environ['ChatExchangeU']
    else: 
        res['user'] = raw_input('Enter your Stack Overflow email ID:')
    
    if 'ChatExchangeP' in os.environ:
        res['pass'] = os.environ['ChatExchangeP']
    else:
        res['pass'] = (raw_input('Enter your Stack Overflow password:'))
        
    if 'RoomID' in os.environ:
        res['room'] = (os.environ['RoomID'])
    else:
        res['room'] = (raw_input('Enter the ID of the Room which you wish to enter:'))
                   
    if 'HostSite' in os.environ:
        res['host'] = (os.environ['HostSite'])
    else:
        import json
        hosts = json.loads(open('hosts.json').read())
        print "Welcome Bot Host Site Options"
        for i in range(1, len(hosts)+1):
            print i, hosts[str(i)]
        print "What will be your Welcome Bot's host site?"
        try:
            res['host'] = hosts[raw_input().strip()]

        except KeyError:
            res['host'] = "invalid" 
    return res


