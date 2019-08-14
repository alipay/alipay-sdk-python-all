#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AddressDTO(object):

    def __init__(self):
        self._poi_code = None
        self._poi_url = None

    @property
    def poi_code(self):
        return self._poi_code

    @poi_code.setter
    def poi_code(self, value):
        self._poi_code = value
    @property
    def poi_url(self):
        return self._poi_url

    @poi_url.setter
    def poi_url(self, value):
        self._poi_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.poi_code:
            if hasattr(self.poi_code, 'to_alipay_dict'):
                params['poi_code'] = self.poi_code.to_alipay_dict()
            else:
                params['poi_code'] = self.poi_code
        if self.poi_url:
            if hasattr(self.poi_url, 'to_alipay_dict'):
                params['poi_url'] = self.poi_url.to_alipay_dict()
            else:
                params['poi_url'] = self.poi_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AddressDTO()
        if 'poi_code' in d:
            o.poi_code = d['poi_code']
        if 'poi_url' in d:
            o.poi_url = d['poi_url']
        return o


