def validate_credentials(c):
    
    if type(c) is not dict:
        return False
    if c['host'] == 'invalid':
        return False
    
    try:
        room = int(c['room'])
        return True
    except Exception, e:
        print e
        return False
    