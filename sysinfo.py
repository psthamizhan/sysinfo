import socket, sys, platform

info = """
New stuff info from victim
===========================
Name: %s
IP: %s
FQDN: %s
System Platform: %s
Machine: %s
Node: %s
Platform: %s
Processor: %s
System OS: %s
Release: %s
Version: %s
        """ %(socket.gethostname(),socket.gethostbyname(socket.gethostname()),  socket.getfqdn(), sys.platform,platform.machine(),platform.node(),platform.platform(),platform.processor(),platform.system(),platform.release(),platform.version())
print (info)
