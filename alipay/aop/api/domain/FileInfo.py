#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FileInfo(object):

    def __init__(self):
        self._data_type = None
        self._file_biz_type = None
        self._file_url = None

    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def file_biz_type(self):
        return self._file_biz_type

    @file_biz_type.setter
    def file_biz_type(self, value):
        self._file_biz_type = value
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.file_biz_type:
            if hasattr(self.file_biz_type, 'to_alipay_dict'):
                params['file_biz_type'] = self.file_biz_type.to_alipay_dict()
            else:
                params['file_biz_type'] = self.file_biz_type
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
        o = FileInfo()
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'file_biz_type' in d:
            o.file_biz_type = d['file_biz_type']
        if 'file_url' in d:
            o.file_url = d['file_url']
        return o


