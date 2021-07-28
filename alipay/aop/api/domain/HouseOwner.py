#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HouseOwner(object):

    def __init__(self):
        self._house_cert_no = None
        self._house_cert_type = None
        self._name = None

    @property
    def house_cert_no(self):
        return self._house_cert_no

    @house_cert_no.setter
    def house_cert_no(self, value):
        self._house_cert_no = value
    @property
    def house_cert_type(self):
        return self._house_cert_type

    @house_cert_type.setter
    def house_cert_type(self, value):
        self._house_cert_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.house_cert_no:
            if hasattr(self.house_cert_no, 'to_alipay_dict'):
                params['house_cert_no'] = self.house_cert_no.to_alipay_dict()
            else:
                params['house_cert_no'] = self.house_cert_no
        if self.house_cert_type:
            if hasattr(self.house_cert_type, 'to_alipay_dict'):
                params['house_cert_type'] = self.house_cert_type.to_alipay_dict()
            else:
                params['house_cert_type'] = self.house_cert_type
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
        o = HouseOwner()
        if 'house_cert_no' in d:
            o.house_cert_no = d['house_cert_no']
        if 'house_cert_type' in d:
            o.house_cert_type = d['house_cert_type']
        if 'name' in d:
            o.name = d['name']
        return o


