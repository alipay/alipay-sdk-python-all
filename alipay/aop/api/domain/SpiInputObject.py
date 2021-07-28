#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpiInputObject(object):

    def __init__(self):
        self._age = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpiInputObject()
        if 'age' in d:
            o.age = d['age']
        return o


