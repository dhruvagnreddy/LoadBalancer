import httplib
import time

conn = httplib.HTTPConnection("127.0.0.1",8887)
conn.request("GET", "/")
r1 = conn.getresponse()
print r1.status, r1.reason
conn.close()
time.sleep(10)

conn = httplib.HTTPConnection("127.0.0.1",8887)
conn.request("GET", "/")
r2 = conn.getresponse()
print r2.status, r2.reason
conn.close()
time.sleep(10)

conn = httplib.HTTPConnection("127.0.0.1",8887)
conn.request("GET", "/")
r3 = conn.getresponse()
print r3.status, r3.reason
conn.close()
time.sleep(10)

conn = httplib.HTTPConnection("127.0.0.1",8887)
conn.request("GET", "/")
r4 = conn.getresponse()
print r4.status, r4.reason
conn.close()
time.sleep(10)

conn = httplib.HTTPConnection("127.0.0.1",8887)
conn.request("GET", "/")
r5 = conn.getresponse()
print r5.status, r5.reason
conn.close()
