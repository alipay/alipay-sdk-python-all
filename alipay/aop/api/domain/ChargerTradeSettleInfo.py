#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChargerTradeSettleInfo(object):

    def __init__(self):
        self._advance_pay_status = None
        self._gmt_payment = None
        self._pay_amount = None

    @property
    def advance_pay_status(self):
        return self._advance_pay_status

    @advance_pay_status.setter
    def advance_pay_status(self, value):
        self._advance_pay_status = value
    @property
    def gmt_payment(self):
        return self._gmt_payment

    @gmt_payment.setter
    def gmt_payment(self, value):
        self._gmt_payment = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.advance_pay_status:
            if hasattr(self.advance_pay_status, 'to_alipay_dict'):
                params['advance_pay_status'] = self.advance_pay_status.to_alipay_dict()
            else:
                params['advance_pay_status'] = self.advance_pay_status
        if self.gmt_payment:
            if hasattr(self.gmt_payment, 'to_alipay_dict'):
                params['gmt_payment'] = self.gmt_payment.to_alipay_dict()
            else:
                params['gmt_payment'] = self.gmt_payment
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChargerTradeSettleInfo()
        if 'advance_pay_status' in d:
            o.advance_pay_status = d['advance_pay_status']
        if 'gmt_payment' in d:
            o.gmt_payment = d['gmt_payment']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        return o


