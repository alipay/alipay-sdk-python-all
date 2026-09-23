#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PhoneNumberItem(object):

    def __init__(self):
        self._phone_number = None
        self._phone_usage = None

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
    @property
    def phone_usage(self):
        return self._phone_usage

    @phone_usage.setter
    def phone_usage(self, value):
        self._phone_usage = value


    def to_alipay_dict(self):
        params = dict()
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        if self.phone_usage:
            if hasattr(self.phone_usage, 'to_alipay_dict'):
                params['phone_usage'] = self.phone_usage.to_alipay_dict()
            else:
                params['phone_usage'] = self.phone_usage
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PhoneNumberItem()
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'phone_usage' in d:
            o.phone_usage = d['phone_usage']
        return o


