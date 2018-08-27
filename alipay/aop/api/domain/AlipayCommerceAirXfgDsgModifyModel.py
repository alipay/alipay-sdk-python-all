#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAirXfgDsgModifyModel(object):

    def __init__(self):
        self._age = None
        self._nam = None
        self._sex = None
        self._xbw = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def nam(self):
        return self._nam

    @nam.setter
    def nam(self, value):
        self._nam = value
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value
    @property
    def xbw(self):
        return self._xbw

    @xbw.setter
    def xbw(self, value):
        self._xbw = value


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.nam:
            if hasattr(self.nam, 'to_alipay_dict'):
                params['nam'] = self.nam.to_alipay_dict()
            else:
                params['nam'] = self.nam
        if self.sex:
            if hasattr(self.sex, 'to_alipay_dict'):
                params['sex'] = self.sex.to_alipay_dict()
            else:
                params['sex'] = self.sex
        if self.xbw:
            if hasattr(self.xbw, 'to_alipay_dict'):
                params['xbw'] = self.xbw.to_alipay_dict()
            else:
                params['xbw'] = self.xbw
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAirXfgDsgModifyModel()
        if 'age' in d:
            o.age = d['age']
        if 'nam' in d:
            o.nam = d['nam']
        if 'sex' in d:
            o.sex = d['sex']
        if 'xbw' in d:
            o.xbw = d['xbw']
        return o


