#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MccInfo(object):

    def __init__(self):
        self._mcc_code = None
        self._mcc_name = None

    @property
    def mcc_code(self):
        return self._mcc_code

    @mcc_code.setter
    def mcc_code(self, value):
        self._mcc_code = value
    @property
    def mcc_name(self):
        return self._mcc_name

    @mcc_name.setter
    def mcc_name(self, value):
        self._mcc_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.mcc_code:
            if hasattr(self.mcc_code, 'to_alipay_dict'):
                params['mcc_code'] = self.mcc_code.to_alipay_dict()
            else:
                params['mcc_code'] = self.mcc_code
        if self.mcc_name:
            if hasattr(self.mcc_name, 'to_alipay_dict'):
                params['mcc_name'] = self.mcc_name.to_alipay_dict()
            else:
                params['mcc_name'] = self.mcc_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MccInfo()
        if 'mcc_code' in d:
            o.mcc_code = d['mcc_code']
        if 'mcc_name' in d:
            o.mcc_name = d['mcc_name']
        return o


