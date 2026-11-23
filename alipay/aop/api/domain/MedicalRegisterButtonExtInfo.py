#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalRegisterButtonExtInfo(object):

    def __init__(self):
        self._phone_number = None

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        if isinstance(value, list):
            self._phone_number = list()
            for i in value:
                self._phone_number.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.phone_number:
            if isinstance(self.phone_number, list):
                for i in range(0, len(self.phone_number)):
                    element = self.phone_number[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.phone_number[i] = element.to_alipay_dict()
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalRegisterButtonExtInfo()
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        return o


