def init_modules(environ):
    import json, imp, os
    global modules
    try:
        cur_path = os.path.dirname(os.path.abspath(__file__))
        print cur_path
        modules = json.loads(open('modules.json').read())
        for i in modules:
            s = imp.load_source(i[2:], os.path.join(cur_path, modules[i]))
            exec('import '+i[2:], environ)
            # print i[2:]
            
    except IOError, e:
       
        print e
    except ValueError, e:
    	print e
    