# -*- coding: utf-8 -*-
'''
Created on 2017-12-20

@author: liuqun
'''
import json
import os

import itertools

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.CommonConstants import *

try:
    import httplib
except ImportError:
    import http.client as httplib
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse
try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus
import mimetypes

from alipay.aop.api.exception.Exception import *


class MultiPartForm(object):
    """Accumulate the data to be used when posting a form."""

    def __init__(self, charset='utf-8'):
        self.charset = charset
        self.form_fields = []
        self.files = []
        self.boundary = "ALIPAY_SDK_PYTHON_BOUNDARY"
        return

    def get_content_type(self):
        return 'multipart/form-data; boundary=%s' % self.boundary

    def add_field(self, name, value):
        """Add a simple field to the form data."""
        if not isinstance(value, str):
            value = json.dumps(value, ensure_ascii=False)
        self.form_fields.append((name, value))
        return

    def add_file(self, field_name, file_name, file_content, mimetype=None):
        """Add a file to be uploaded."""
        if mimetype is None:
            mimetype = mimetypes.guess_type(file_name)[0] or 'application/octet-stream'
        self.files.append((field_name, file_name, mimetype, file_content))
        return

    def build_body(self):
        """Return a string representing the form data, including attached files."""
        # Build a list of lists, each containing "lines" of the
        # request.  Each part is separated by a boundary string.
        # Once the list is built, return a string where each
        # line is separated by '\r\n'.
        parts = []
        part_boundary = '--' + self.boundary

        # Add the form fields
        parts.extend(
            [bytes(part_boundary.encode(self.charset)),
             bytes(('Content-Disposition: form-data; name="%s"' % name).encode(self.charset))
                if PYTHON_VERSION_3 else ('Content-Disposition: form-data; name="%s"' % name),
             bytes(('Content-Type: text/plain; charset=%s' % self.charset).encode(self.charset)),
             bytes(''.encode(self.charset)),
             bytes(value.encode(self.charset)) if PYTHON_VERSION_3 else value
            ]
            for name, value in self.form_fields
        )

        # Add the files to upload
        parts.extend(
            [bytes(part_boundary.encode(self.charset)),
             bytes(('Content-Disposition: form-data; name="%s"; filename="%s"' %
                    (field_name, filename)).encode(self.charset)) if PYTHON_VERSION_3 else
                    ('Content-Disposition: form-data; name="%s"; filename="%s"' % (field_name, filename)),
             bytes(('Content-Type: %s' % content_type).encode(self.charset)),
             bytes('Content-Transfer-Encoding: binary'.encode(self.charset)),
             bytes(''.encode(self.charset)),
             body,
            ]
            for field_name, filename, content_type, body in self.files
        )

        # Flatten the list and add closing boundary marker,
        # then return CR+LF separated data
        flattened = list(itertools.chain(*parts))
        flattened.append(bytes(('--' + self.boundary + '--').encode(self.charset)))
        flattened.append(bytes(''.encode(self.charset)))
        return bytes('\r\n'.encode(self.charset)).join(flattened)


def url_encode(params, charset):
    query_string = ""
    for (k, v) in params.items():
        value = v
        if not isinstance(value, str):
            value = json.dumps(value, ensure_ascii=False)
        if PYTHON_VERSION_3:
            value = quote_plus(value, encoding=charset)
        else:
            value = quote_plus(value)
        query_string += ("&" + k + "=" + value)
    query_string = query_string[1:]
    return query_string


def get_http_connection(url, query_string, timeout):
    url_parse_result = urlparse.urlparse(url)
    host = url_parse_result.hostname
    port = 80
    connection = httplib.HTTPConnection(host=host, port=port, timeout=timeout)
    if url.find("https") == 0:
        port = 443
        connection = httplib.HTTPSConnection(host=host, port=port, timeout=timeout)
    url = url_parse_result.scheme + "://" + url_parse_result.hostname
    if url_parse_result.port:
        url += url_parse_result.port
    url += url_parse_result.path
    url += ('?' + query_string)
    return url, connection


def do_post(url, query_string=None, headers=None, params=None, charset='utf-8', timeout=15):
    url, connection = get_http_connection(url, query_string, timeout)

    try:
        connection.connect()
    except Exception as e:
        raise RequestException('[' + THREAD_LOCAL.uuid + ']post connect failed. ' + str(e))
    body = None
    if params:
        body = url_encode(params, charset)
    try:
        connection.request("POST", url, body=body, headers=headers)
    except Exception as e:
        raise RequestException('[' + THREAD_LOCAL.uuid + ']post request failed. ' + str(e))
    response = connection.getresponse()
    if response.status is not 200:
        raise ResponseException('[' + THREAD_LOCAL.uuid + ']invalid http status ' + str(response.status) + \
                               ',detail body:' + response.read())
    result = response.read()
    try:
        response.close()
        connection.close()
    except Exception:
        pass
    return result


def do_multipart_post(url, query_string=None, headers=None, params=None, multipart_params=None, charset='utf-8', timeout=30):
    url, connection = get_http_connection(url, query_string, timeout)

    try:
        connection.connect()
    except Exception as e:
        raise RequestException('[' + THREAD_LOCAL.uuid + ']post connect failed. ' + str(e))

    form = MultiPartForm(charset)
    for key, value in params.items():
        form.add_field(key, value)
    for key, value in multipart_params.items():
        file_item = value
        if file_item and isinstance(file_item, FileItem):
            form.add_file(field_name=key, file_name=file_item.get_file_name(),
                          file_content=file_item.get_file_content(), mimetype=file_item.get_mime_type())
    body = form.build_body()
    if not headers:
        headers = {}
    headers['Content-type'] = form.get_content_type()

    try:
        connection.request("POST", url, body=body, headers=headers)
    except Exception as e:
        raise RequestException('[' + THREAD_LOCAL.uuid + ']post request failed. ' + str(e))
    response = connection.getresponse()
    if response.status is not 200:
        raise ResponseException('[' + THREAD_LOCAL.uuid + ']invalid http status ' + str(response.status) + \
                                ',detail body:' + response.read())
    result = response.read()
    try:
        response.close()
        connection.close()
    except Exception:
        pass
    return result
