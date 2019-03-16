import socket
import struct
import sys
import time

"""
Some of public RFC868 servers
time.inrim.it (193.204.114.105)
time-c.nist.gov (129.6.15.30)
utcnist.colorado.edu (128.138.140.44)
"""

# reference time (in seconds since 1900-01-01 00:00:00)
TIME1970 = 2208988800  # 1970-01-01 00:00:00


def get_time(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    t = s.recv(4)
    s.close()
    t = struct.unpack("!I", t)[0]
    return int(t - TIME1970)


if __name__ == "__main__":
    if sys.argv[1:]:
        host = sys.argv[1]
        port = 37
    else:
        host = "127.0.0.1"
        port = 8037
    t = get_time(host, port)
    print("Server time is", time.ctime(t))
