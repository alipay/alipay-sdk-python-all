#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QueryProvCityInfo(object):

    def __init__(self):
        self._adcode = None
        self._name = None

    @property
    def adcode(self):
        return self._adcode

    @adcode.setter
    def adcode(self, value):
        self._adcode = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.adcode:
            if hasattr(self.adcode, 'to_alipay_dict'):
                params['adcode'] = self.adcode.to_alipay_dict()
            else:
                params['adcode'] = self.adcode
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QueryProvCityInfo()
        if 'adcode' in d:
            o.adcode = d['adcode']
        if 'name' in d:
            o.name = d['name']
        return o


