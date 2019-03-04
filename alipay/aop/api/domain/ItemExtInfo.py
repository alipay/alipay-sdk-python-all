#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemExtInfo(object):

    def __init__(self):
        self._ext_key = None
        self._ext_value = None

    @property
    def ext_key(self):
        return self._ext_key

    @ext_key.setter
    def ext_key(self, value):
        self._ext_key = value
    @property
    def ext_value(self):
        return self._ext_value

    @ext_value.setter
    def ext_value(self, value):
        self._ext_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_key:
            if hasattr(self.ext_key, 'to_alipay_dict'):
                params['ext_key'] = self.ext_key.to_alipay_dict()
            else:
                params['ext_key'] = self.ext_key
        if self.ext_value:
            if hasattr(self.ext_value, 'to_alipay_dict'):
                params['ext_value'] = self.ext_value.to_alipay_dict()
            else:
                params['ext_value'] = self.ext_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemExtInfo()
        if 'ext_key' in d:
            o.ext_key = d['ext_key']
        if 'ext_value' in d:
            o.ext_value = d['ext_value']
        return o


