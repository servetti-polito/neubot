# neubot/backend_null.py

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

''' Null backend driver '''

class BackendNull(object):
    ''' Null backend driver '''

    def bittorrent_store(self, message):
        ''' Save result of BitTorrent test '''

    def store_raw(self, message):
        ''' Save result of RAW test '''

    def speedtest_store(self, message):
        ''' Save result of speedtest test '''

    def dash_store(self, message):
        ''' Save result of dash test '''
