# neubot/http/messages.py

#
# Copyright (c) 2010 Simone Basso <bassosimone@gmail.com>,
#  NEXA Center for Internet & Society at Politecnico di Torino
#
# This file is part of Neubot <http://www.neubot.org/>.
#
# Neubot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Neubot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Neubot.  If not, see <http://www.gnu.org/licenses/>.
#

import StringIO
import types
import socket
import os

from neubot.http.utils import urlsplit
from neubot.utils import safe_seek
from neubot.http.utils import date


class Message(object):

    """Represents an HTTP message."""

    def __init__(self, method="", uri="", code="", reason="", protocol=""):
        self.method = method
        self.uri = uri
        self.code = code
        self.reason = reason
        self.protocol = protocol
        self.headers = {}
        self.body = StringIO.StringIO("")
        self.scheme = ""
        self.address = ""
        self.port = ""
        self.pathquery = ""
        self.family = socket.AF_UNSPEC
        self.length = 0
        self.response = None

    #
    # The client code saves the whole uri in self.uri and then
    # splits the URI in pieces and, after that, self.pathquery
    # contains path+query.  The server code, instead, saves in
    # self.uri the URI and does not split it.  So we must con-
    # sider both self.pathquery and self.uri, and we must give
    # precedence to self.pathquery--or we will send requests
    # that some web servers do not accept.
    #

    def serialize_headers(self):
        lst = []

        if self.method:
            lst.append(self.method)
            lst.append(" ")
            if self.pathquery:
                lst.append(self.pathquery)
            elif self.uri:
                lst.append(self.uri)
            else:
                lst.append("/")
            lst.append(" ")
            lst.append(self.protocol)
        else:
            lst.append(self.protocol)
            lst.append(" ")
            lst.append(self.code)
            lst.append(" ")
            lst.append(self.reason)
        lst.append("\r\n")

        for key, value in self.headers.items():
            lst.append(key)
            lst.append(": ")
            lst.append(value)
            lst.append("\r\n")
        lst.append("\r\n")

        octets = "".join(lst)
        return StringIO.StringIO(octets)

    def serialize_body(self):
        return self.body

    #
    # RFC2616 section 4.2 says that "Each header field consists
    # of a name followed by a colon (":") and the field value. Field
    # names are case-insensitive."  So, for simplicity, we use all-
    # lowercase header names.
    #

    def __getitem__(self, key):
        if type(key) != types.StringType:
            raise TypeError("key should be a string")
        key = key.lower()
        if self.headers.has_key(key):
            return self.headers[key]
        return ""

    def __setitem__(self, key, value):
        if type(key) != types.StringType:
            raise TypeError("key should be a string")
        key = key.lower()
        if self.headers.has_key(key):
            value = self.headers[key] + ", " + value
        self.headers[key] = value

    def __delitem__(self, key):
        if type(key) != types.StringType:
            raise TypeError("key should be a string")
        key = key.lower()
        if self.headers.has_key(key):
            del self.headers[key]

    #
    # Note that compose() is meant for composing request messages
    # from client-side and response messages from server-side.
    # If the body is not present we explicitly set Content-Length at
    # zero.  It costs nothing and the gain is that the browser does
    # not guess that there is an unbounded response when we send a
    # "200 Ok" response with no attached body.
    #

    def compose(self, **kwargs):
        self.method = kwargs.get("method", "")

        if kwargs.get("uri", ""):
            self.uri = kwargs.get("uri", "")
            (self.scheme, self.address,
             self.port, self.pathquery) = urlsplit(self.uri)
            self["host"] = self.address + ":" + self.port
        else:
            self.scheme = kwargs.get("scheme", "")
            self.address = kwargs.get("address", "")
            self.port = kwargs.get("port", "")
            self.pathquery = kwargs.get("pathquery", "")

        self.code = kwargs.get("code", "")
        self.reason = kwargs.get("reason", "")
        self.protocol = kwargs.get("protocol", "HTTP/1.1")

        if kwargs.get("nocache", True):
            if self.method:
                self["pragma"] = "no-cache"
            self["cache-control"] = "no-cache"

        if kwargs.get("date", True):
            self["date"] = date()

        if not kwargs.get("keepalive", True):
            self["connection"] = "close"

        if kwargs.get("body", None):
            self.body = kwargs.get("body", None)
            safe_seek(self.body, 0, os.SEEK_END)
            self.length = self.body.tell()
            safe_seek(self.body, 0, os.SEEK_SET)
            self["content-length"] = str(self.length)
            if kwargs.get("mimetype", ""):
                self["content-type"] = kwargs.get("mimetype", "")
        else:
            self["content-length"] = "0"

        self.family = kwargs.get("family", socket.AF_INET)


# for compat
def compose(m, **kwargs):
    m.compose(**kwargs)
