#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InterTradeFileInfoVO(object):

    def __init__(self):
        self._file_name = None
        self._file_source = None
        self._file_type = None
        self._file_url = None

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def file_source(self):
        return self._file_source

    @file_source.setter
    def file_source(self, value):
        self._file_source = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.file_source:
            if hasattr(self.file_source, 'to_alipay_dict'):
                params['file_source'] = self.file_source.to_alipay_dict()
            else:
                params['file_source'] = self.file_source
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.file_url:
            if hasattr(self.file_url, 'to_alipay_dict'):
                params['file_url'] = self.file_url.to_alipay_dict()
            else:
                params['file_url'] = self.file_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InterTradeFileInfoVO()
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'file_source' in d:
            o.file_source = d['file_source']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'file_url' in d:
            o.file_url = d['file_url']
        return o


