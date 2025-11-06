#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubOrderVO(object):

    def __init__(self):
        self._premium = None
        self._sub_order_no = None
        self._total_premium = None

    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value
    @property
    def sub_order_no(self):
        return self._sub_order_no

    @sub_order_no.setter
    def sub_order_no(self, value):
        self._sub_order_no = value
    @property
    def total_premium(self):
        return self._total_premium

    @total_premium.setter
    def total_premium(self, value):
        self._total_premium = value


    def to_alipay_dict(self):
        params = dict()
        if self.premium:
            if hasattr(self.premium, 'to_alipay_dict'):
                params['premium'] = self.premium.to_alipay_dict()
            else:
                params['premium'] = self.premium
        if self.sub_order_no:
            if hasattr(self.sub_order_no, 'to_alipay_dict'):
                params['sub_order_no'] = self.sub_order_no.to_alipay_dict()
            else:
                params['sub_order_no'] = self.sub_order_no
        if self.total_premium:
            if hasattr(self.total_premium, 'to_alipay_dict'):
                params['total_premium'] = self.total_premium.to_alipay_dict()
            else:
                params['total_premium'] = self.total_premium
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubOrderVO()
        if 'premium' in d:
            o.premium = d['premium']
        if 'sub_order_no' in d:
            o.sub_order_no = d['sub_order_no']
        if 'total_premium' in d:
            o.total_premium = d['total_premium']
        return o


