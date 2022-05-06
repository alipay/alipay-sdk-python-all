#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DataFile(object):

    def __init__(self):
        self._access_url = None
        self._data_type = None

    @property
    def access_url(self):
        return self._access_url

    @access_url.setter
    def access_url(self, value):
        self._access_url = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_url:
            if hasattr(self.access_url, 'to_alipay_dict'):
                params['access_url'] = self.access_url.to_alipay_dict()
            else:
                params['access_url'] = self.access_url
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DataFile()
        if 'access_url' in d:
            o.access_url = d['access_url']
        if 'data_type' in d:
            o.data_type = d['data_type']
        return o


