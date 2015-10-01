#!/usr/local/bin/python
import argparse
import os

from mohawk import Sender
import requests


class Formatter(argparse.RawDescriptionHelpFormatter,
                argparse.ArgumentDefaultsHelpFormatter):
    """
    A formatter that shows defaults in the help description.
    """


def main():
    p = argparse.ArgumentParser(description='Upload with Hawk',
                                formatter_class=Formatter)
    p.add_argument('--server', default='http://192.168.59.103:8000',
                   help='base URL of the server')
    args = p.parse_args()

    url = '{}/upload/with-hawk/'.format(args.server)
    request_content_type = 'application/zip'

    filename = 'jetpack-1.14.xpi'
    with open(os.path.join(os.path.dirname(__file__),
                           'files', 'jetpack-1.14.xpi'), 'rb') as f:
        data = f.read()
    files = {
        'file': (filename, data, request_content_type)
    }

    sender = Sender({'id': 'script-user',
                     'key': 'secret-key',
                     'algorithm': 'sha256'},
                    url, 'POST',
                    content=data,
                    content_type=request_content_type)

    headers = {'Authorization': sender.request_header,
               'Content-Type': request_content_type}

    res = requests.post(url, files=files, headers=headers)

    print '-- response --'
    print res
    print res.content


if __name__ == '__main__':
    main()
