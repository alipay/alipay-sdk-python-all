#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyVO import MultiCurrencyMoneyVO


class BillRepayRequest(object):

    def __init__(self):
        self._repay_amt = None

    @property
    def repay_amt(self):
        return self._repay_amt

    @repay_amt.setter
    def repay_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyVO):
            self._repay_amt = value
        else:
            self._repay_amt = MultiCurrencyMoneyVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.repay_amt:
            if hasattr(self.repay_amt, 'to_alipay_dict'):
                params['repay_amt'] = self.repay_amt.to_alipay_dict()
            else:
                params['repay_amt'] = self.repay_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BillRepayRequest()
        if 'repay_amt' in d:
            o.repay_amt = d['repay_amt']
        return o


