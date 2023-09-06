#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RareNameEncodeInfo(object):

    def __init__(self):
        self._encode = None
        self._name = None

    @property
    def encode(self):
        return self._encode

    @encode.setter
    def encode(self, value):
        self._encode = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.encode:
            if hasattr(self.encode, 'to_alipay_dict'):
                params['encode'] = self.encode.to_alipay_dict()
            else:
                params['encode'] = self.encode
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
        o = RareNameEncodeInfo()
        if 'encode' in d:
            o.encode = d['encode']
        if 'name' in d:
            o.name = d['name']
        return o


