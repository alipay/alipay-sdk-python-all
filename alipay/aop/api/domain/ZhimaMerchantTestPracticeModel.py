#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.XXXXsdasdasd import XXXXsdasdasd


class ZhimaMerchantTestPracticeModel(object):

    def __init__(self):
        self._add = None
        self._xxxx = None

    @property
    def add(self):
        return self._add

    @add.setter
    def add(self, value):
        if isinstance(value, list):
            self._add = list()
            for i in value:
                self._add.append(i)
    @property
    def xxxx(self):
        return self._xxxx

    @xxxx.setter
    def xxxx(self, value):
        if isinstance(value, XXXXsdasdasd):
            self._xxxx = value
        else:
            self._xxxx = XXXXsdasdasd.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.add:
            if isinstance(self.add, list):
                for i in range(0, len(self.add)):
                    element = self.add[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.add[i] = element.to_alipay_dict()
            if hasattr(self.add, 'to_alipay_dict'):
                params['add'] = self.add.to_alipay_dict()
            else:
                params['add'] = self.add
        if self.xxxx:
            if hasattr(self.xxxx, 'to_alipay_dict'):
                params['xxxx'] = self.xxxx.to_alipay_dict()
            else:
                params['xxxx'] = self.xxxx
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantTestPracticeModel()
        if 'add' in d:
            o.add = d['add']
        if 'xxxx' in d:
            o.xxxx = d['xxxx']
        return o


