#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PhoneStructVO(object):

    def __init__(self):
        self._phone_number = None
        self._phone_type = None

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
    @property
    def phone_type(self):
        return self._phone_type

    @phone_type.setter
    def phone_type(self, value):
        self._phone_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        if self.phone_type:
            if hasattr(self.phone_type, 'to_alipay_dict'):
                params['phone_type'] = self.phone_type.to_alipay_dict()
            else:
                params['phone_type'] = self.phone_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PhoneStructVO()
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'phone_type' in d:
            o.phone_type = d['phone_type']
        return o


