#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IvrItem(object):

    def __init__(self):
        self._ivr_code = None
        self._name = None

    @property
    def ivr_code(self):
        return self._ivr_code

    @ivr_code.setter
    def ivr_code(self, value):
        self._ivr_code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.ivr_code:
            if hasattr(self.ivr_code, 'to_alipay_dict'):
                params['ivr_code'] = self.ivr_code.to_alipay_dict()
            else:
                params['ivr_code'] = self.ivr_code
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
        o = IvrItem()
        if 'ivr_code' in d:
            o.ivr_code = d['ivr_code']
        if 'name' in d:
            o.name = d['name']
        return o


