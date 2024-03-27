#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditWithdrawApplyInfo(object):

    def __init__(self):
        self._alipay_pay_no = None
        self._amount = None
        self._out_biz_no = None

    @property
    def alipay_pay_no(self):
        return self._alipay_pay_no

    @alipay_pay_no.setter
    def alipay_pay_no(self, value):
        self._alipay_pay_no = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_pay_no:
            if hasattr(self.alipay_pay_no, 'to_alipay_dict'):
                params['alipay_pay_no'] = self.alipay_pay_no.to_alipay_dict()
            else:
                params['alipay_pay_no'] = self.alipay_pay_no
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditWithdrawApplyInfo()
        if 'alipay_pay_no' in d:
            o.alipay_pay_no = d['alipay_pay_no']
        if 'amount' in d:
            o.amount = d['amount']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


