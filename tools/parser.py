# Copyright (c) 2017 Montini Cristian
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import nmap
from config import *
from random import randint
import os
from tools.voice import Voicer

def parser(query):
    """
        This function take a query and select
        the operation searching for /<command> in a text
        message.
        @:param: query
    """
    # Da vedere per pdf, per ora stampa le porte aperte
    if "scan" in query:
        try:
            query = query.split("scan")
            query = (str(query[1].split()).strip("[]")).strip("''")
            result = nmap.PortScanner()
            if query.isalpha() or "<" in query:
                return "Type: /scan <ipaddress>"
            print(query)
            result.scan(query, "20-443")
            ports = ""
            for port in result[query]['tcp']:
                ports += "\n" + str(port)

            return ports

            # pdf = canvas.Canvas("scan.pdf")
            # pdf.drawString(5, 800, "Nmap scan: " + query)
            # pdf.save()

        except Exception as e:
            return str(e)

    if "/help" in query:
        return HELP

    if "/rand" in query:
        import math
        try:
            query = query.split("/rand")
            query = query[1].split(" ")
            one = int(query[1])
            two = int(query[2])

            return randint(one, two)
        except:
            return "Usage: /rand <min> <max>"

    if "/xcommandx" in query:
        try:
            query = query.strip("/command")
            print(query)
            os.system(query)
            return "Executing " + str(query)
        except Exception as e:
            return str(e)

    if "/voice" in query:
        query = query[6:3000]
        if query == "":
            return "Usage: /voice 'some_text'"
        return Voicer(query)

    if "/contacts" in query:
        return CONTACTS

    else:
        return None
