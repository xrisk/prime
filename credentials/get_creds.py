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
        try:
            hosts = json.loads(open('hosts.json').read())
        except:
            return None
        print "Welcome Bot Host Site Options"
        for i in hosts:
            print i, hosts[i]
        print "What will be your Welcome Bot's host site?"
        try:
            res['host'] = hosts[raw_input().strip()]

        except KeyError:
            res['host'] = "invalid" 
    return res

