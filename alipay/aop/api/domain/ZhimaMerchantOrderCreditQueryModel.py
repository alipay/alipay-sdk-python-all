#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaMerchantOrderCreditQueryModel(object):

    def __init__(self):
        self._out_order_no = None
        self._zm_order_no = None

    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def zm_order_no(self):
        return self._zm_order_no

    @zm_order_no.setter
    def zm_order_no(self, value):
        self._zm_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.zm_order_no:
            if hasattr(self.zm_order_no, 'to_alipay_dict'):
                params['zm_order_no'] = self.zm_order_no.to_alipay_dict()
            else:
                params['zm_order_no'] = self.zm_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantOrderCreditQueryModel()
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'zm_order_no' in d:
            o.zm_order_no = d['zm_order_no']
        return o


