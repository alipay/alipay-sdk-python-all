#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntSignFileResult(object):

    def __init__(self):
        self._file_id = None
        self._file_key = None
        self._file_name = None
        self._http_file_url = None

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
    def http_file_url(self):
        return self._http_file_url

    @http_file_url.setter
    def http_file_url(self, value):
        self._http_file_url = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.http_file_url:
            if hasattr(self.http_file_url, 'to_alipay_dict'):
                params['http_file_url'] = self.http_file_url.to_alipay_dict()
            else:
                params['http_file_url'] = self.http_file_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntSignFileResult()
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'file_key' in d:
            o.file_key = d['file_key']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'http_file_url' in d:
            o.http_file_url = d['http_file_url']
        return o


