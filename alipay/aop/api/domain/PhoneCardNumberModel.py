#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PhoneCardNumberModel(object):

    def __init__(self):
        self._check_code = None
        self._phone_number = None

    @property
    def check_code(self):
        return self._check_code

    @check_code.setter
    def check_code(self, value):
        self._check_code = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_code:
            if hasattr(self.check_code, 'to_alipay_dict'):
                params['check_code'] = self.check_code.to_alipay_dict()
            else:
                params['check_code'] = self.check_code
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PhoneCardNumberModel()
        if 'check_code' in d:
            o.check_code = d['check_code']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        return o


