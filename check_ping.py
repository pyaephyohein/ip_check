from email import message
import os

from sympy import public #example


def ping(ping_ip):

    response = os.system("ping -c 2 " + ping_ip)

    #and then check the response...
    if response == 0:
        message = "is UP"
        return ping_ip, message
    else:
        message = "is Down"
        return ping_ip, message