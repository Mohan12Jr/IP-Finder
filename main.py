import socket as s
hostname = s.gethostname()
mypip = s.gethostbyname(hostname)
print("My IP address is:"+mypip)