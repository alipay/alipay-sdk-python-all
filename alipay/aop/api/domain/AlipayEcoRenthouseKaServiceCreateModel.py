#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoRenthouseKaServiceCreateModel(object):

    def __init__(self):
        self._address = None
        self._ka_code = None
        self._type = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def ka_code(self):
        return self._ka_code

    @ka_code.setter
    def ka_code(self, value):
        self._ka_code = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.ka_code:
            if hasattr(self.ka_code, 'to_alipay_dict'):
                params['ka_code'] = self.ka_code.to_alipay_dict()
            else:
                params['ka_code'] = self.ka_code
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoRenthouseKaServiceCreateModel()
        if 'address' in d:
            o.address = d['address']
        if 'ka_code' in d:
            o.ka_code = d['ka_code']
        if 'type' in d:
            o.type = d['type']
        return o


