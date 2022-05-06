#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FileInfoDTO(object):

    def __init__(self):
        self._encode_type = None
        self._file_name = None
        self._file_size = None
        self._url = None

    @property
    def encode_type(self):
        return self._encode_type

    @encode_type.setter
    def encode_type(self, value):
        self._encode_type = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, value):
        self._file_size = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.encode_type:
            if hasattr(self.encode_type, 'to_alipay_dict'):
                params['encode_type'] = self.encode_type.to_alipay_dict()
            else:
                params['encode_type'] = self.encode_type
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.file_size:
            if hasattr(self.file_size, 'to_alipay_dict'):
                params['file_size'] = self.file_size.to_alipay_dict()
            else:
                params['file_size'] = self.file_size
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FileInfoDTO()
        if 'encode_type' in d:
            o.encode_type = d['encode_type']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'file_size' in d:
            o.file_size = d['file_size']
        if 'url' in d:
            o.url = d['url']
        return o


