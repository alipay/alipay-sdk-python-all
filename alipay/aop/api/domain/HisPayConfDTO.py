#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HisPayConfDTO(object):

    def __init__(self):
        self._pay_way = None

    @property
    def pay_way(self):
        return self._pay_way

    @pay_way.setter
    def pay_way(self, value):
        self._pay_way = value


    def to_alipay_dict(self):
        params = dict()
        if self.pay_way:
            if hasattr(self.pay_way, 'to_alipay_dict'):
                params['pay_way'] = self.pay_way.to_alipay_dict()
            else:
                params['pay_way'] = self.pay_way
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HisPayConfDTO()
        if 'pay_way' in d:
            o.pay_way = d['pay_way']
        return o


