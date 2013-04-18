# neubot/buff.py

#
# Copyright (c) 2012 Simone Basso <bassosimone@gmail.com>,
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

''' Input buffer '''

# Python3-ready: yes

from collections import deque
from neubot import six

NEWLINE = six.b('\n')
EMPTY = six.b('')

if six.PY3:
    BYTES = bytes
else:
    BYTES = str

class Buff(object):

    ''' Input buffer '''

    def __init__(self):
        self.buff = deque()
        self.total = 0

    def bufferise(self, octets):
        ''' Bufferise incoming data '''
        self.buff.append(octets)
        self.total += len(octets)

    def skip(self, length):
        ''' Skip up to lenght bytes from buff '''
        if self.total >= length:
            while length > 0:
                bucket = self.buff.popleft()
                if len(bucket) > length:
                    self.buff.appendleft(six.buff(bucket, length))
                    self.total -= length
                    return 0
                length -= len(bucket)
                self.total -= len(bucket)
        return length

    def pullup(self, length):
        ''' Pullup length bytes from buff '''
        retval = []
        if self.total >= length:
            while length > 0:
                bucket = self.buff.popleft()
                if len(bucket) > length:
                    self.buff.appendleft(six.buff(bucket, length))
                    bucket = six.buff(bucket, 0, length)
                retval.append(BYTES(bucket))
                self.total -= len(bucket)
                length -= len(bucket)
        return EMPTY.join(retval)

    def getvalue(self):
        ''' Read the whole content of the buff '''
        return self.pullup(self.total)

    def getline(self, maxline):
        ''' Read line from buff '''
        tmp = self.pullup(min(maxline, self.total))
        index = tmp.find(NEWLINE)
        if index >= 0:
            line = tmp[:index + 1]
            remainder = tmp[index + 1:]
            if remainder:
                self.buff.appendleft(remainder)
                self.total += len(remainder)
            return line
        if len(tmp) >= maxline:
            raise RuntimeError('buff: line too long')
        self.buff.appendleft(tmp)
        self.total += len(tmp)
        return EMPTY
