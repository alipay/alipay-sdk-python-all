#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceBillEreceiptApplyModel(object):

    def __init__(self):
        self._pay_fund_order_id = None

    @property
    def pay_fund_order_id(self):
        return self._pay_fund_order_id

    @pay_fund_order_id.setter
    def pay_fund_order_id(self, value):
        self._pay_fund_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.pay_fund_order_id:
            if hasattr(self.pay_fund_order_id, 'to_alipay_dict'):
                params['pay_fund_order_id'] = self.pay_fund_order_id.to_alipay_dict()
            else:
                params['pay_fund_order_id'] = self.pay_fund_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceBillEreceiptApplyModel()
        if 'pay_fund_order_id' in d:
            o.pay_fund_order_id = d['pay_fund_order_id']
        return o


