#!/usr/bin/env python

#  pyftpdlib is released under the MIT license, reproduced below:
#  ======================================================================
#  Copyright (C) 2007-2014 Giampaolo Rodola' <g.rodola@gmail.com>
#
#                         All Rights Reserved
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
#  ======================================================================

"""
A FTP server which handles every connection in a separate process.
Useful if your handler class contains blocking calls or your
filesystem is too slow.

POSIX only; requires python >= 2.6.
"""

from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import MultiprocessFTPServer
from pyftpdlib.authorizers import DummyAuthorizer


def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user('user', '12345', '.')
    handler = FTPHandler
    handler.authorizer = authorizer
    server = MultiprocessFTPServer(('', 2121), handler)
    server.serve_forever()

if __name__ == "__main__":
    main()
