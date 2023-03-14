#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntSignFileRequest(object):

    def __init__(self):
        self._file_http_url = None
        self._file_id = None
        self._file_key = None
        self._file_name = None
        self._file_type = None

    @property
    def file_http_url(self):
        return self._file_http_url

    @file_http_url.setter
    def file_http_url(self, value):
        self._file_http_url = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def file_key(self):
        return self._file_key

    @file_key.setter
    def file_key(self, value):
        self._file_key = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_http_url:
            if hasattr(self.file_http_url, 'to_alipay_dict'):
                params['file_http_url'] = self.file_http_url.to_alipay_dict()
            else:
                params['file_http_url'] = self.file_http_url
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.file_key:
            if hasattr(self.file_key, 'to_alipay_dict'):
                params['file_key'] = self.file_key.to_alipay_dict()
            else:
                params['file_key'] = self.file_key
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntSignFileRequest()
        if 'file_http_url' in d:
            o.file_http_url = d['file_http_url']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'file_key' in d:
            o.file_key = d['file_key']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'file_type' in d:
            o.file_type = d['file_type']
        return o


