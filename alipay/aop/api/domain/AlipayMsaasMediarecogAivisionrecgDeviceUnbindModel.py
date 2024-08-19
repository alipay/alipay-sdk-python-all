#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMsaasMediarecogAivisionrecgDeviceUnbindModel(object):

    def __init__(self):
        self._activation_code = None
        self._isv_id = None

    @property
    def activation_code(self):
        return self._activation_code

    @activation_code.setter
    def activation_code(self, value):
        self._activation_code = value
    @property
    def isv_id(self):
        return self._isv_id

    @isv_id.setter
    def isv_id(self, value):
        self._isv_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activation_code:
            if hasattr(self.activation_code, 'to_alipay_dict'):
                params['activation_code'] = self.activation_code.to_alipay_dict()
            else:
                params['activation_code'] = self.activation_code
        if self.isv_id:
            if hasattr(self.isv_id, 'to_alipay_dict'):
                params['isv_id'] = self.isv_id.to_alipay_dict()
            else:
                params['isv_id'] = self.isv_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogAivisionrecgDeviceUnbindModel()
        if 'activation_code' in d:
            o.activation_code = d['activation_code']
        if 'isv_id' in d:
            o.isv_id = d['isv_id']
        return o


