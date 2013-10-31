import os

def get_status(hsmap):
    for k,v in hsmap.iteritems(): 
        host = v[0].host
        svcs = [item.path for item in v]
        cmd = 'supervisorctl -s %s -u %s -p %s status %s' % (host.url, host.user, host.password, ' '.join(svcs))
        output = os.popen(cmd).read().strip()
        descs = output.split('\n')
        for svc, desc in zip(v, descs):
            svc.description = desc

def do_action(service, action_name):
    host = service.host
    cmd = 'supervisorctl -s %s -u %s -p %s %s %s' % (host.url, host.user, host.password, action_name, service.path)
    output = os.popen(cmd).read().strip()

    return output 
