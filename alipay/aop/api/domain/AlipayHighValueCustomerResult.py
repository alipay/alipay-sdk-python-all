#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayHighValueCustomerResult(object):

    def __init__(self):
        self._level = None

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value


    def to_alipay_dict(self):
        params = dict()
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayHighValueCustomerResult()
        if 'level' in d:
            o.level = d['level']
        return o


