#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherExpressInfo(object):

    def __init__(self):
        self._pay_express = None

    @property
    def pay_express(self):
        return self._pay_express

    @pay_express.setter
    def pay_express(self, value):
        self._pay_express = value


    def to_alipay_dict(self):
        params = dict()
        if self.pay_express:
            if hasattr(self.pay_express, 'to_alipay_dict'):
                params['pay_express'] = self.pay_express.to_alipay_dict()
            else:
                params['pay_express'] = self.pay_express
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherExpressInfo()
        if 'pay_express' in d:
            o.pay_express = d['pay_express']
        return o


