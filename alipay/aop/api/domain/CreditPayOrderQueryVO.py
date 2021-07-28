#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditPayOrderQueryVO(object):

    def __init__(self):
        self._acc_amt = None
        self._pay_amt = None
        self._pay_order_no = None
        self._refund_af_acc_amt = None
        self._refund_bef_acc_amt = None
        self._repay_amt = None

    @property
    def acc_amt(self):
        return self._acc_amt

    @acc_amt.setter
    def acc_amt(self, value):
        self._acc_amt = value
    @property
    def pay_amt(self):
        return self._pay_amt

    @pay_amt.setter
    def pay_amt(self, value):
        self._pay_amt = value
    @property
    def pay_order_no(self):
        return self._pay_order_no

    @pay_order_no.setter
    def pay_order_no(self, value):
        self._pay_order_no = value
    @property
    def refund_af_acc_amt(self):
        return self._refund_af_acc_amt

    @refund_af_acc_amt.setter
    def refund_af_acc_amt(self, value):
        self._refund_af_acc_amt = value
    @property
    def refund_bef_acc_amt(self):
        return self._refund_bef_acc_amt

    @refund_bef_acc_amt.setter
    def refund_bef_acc_amt(self, value):
        self._refund_bef_acc_amt = value
    @property
    def repay_amt(self):
        return self._repay_amt

    @repay_amt.setter
    def repay_amt(self, value):
        self._repay_amt = value


    def to_alipay_dict(self):
        params = dict()
        if self.acc_amt:
            if hasattr(self.acc_amt, 'to_alipay_dict'):
                params['acc_amt'] = self.acc_amt.to_alipay_dict()
            else:
                params['acc_amt'] = self.acc_amt
        if self.pay_amt:
            if hasattr(self.pay_amt, 'to_alipay_dict'):
                params['pay_amt'] = self.pay_amt.to_alipay_dict()
            else:
                params['pay_amt'] = self.pay_amt
        if self.pay_order_no:
            if hasattr(self.pay_order_no, 'to_alipay_dict'):
                params['pay_order_no'] = self.pay_order_no.to_alipay_dict()
            else:
                params['pay_order_no'] = self.pay_order_no
        if self.refund_af_acc_amt:
            if hasattr(self.refund_af_acc_amt, 'to_alipay_dict'):
                params['refund_af_acc_amt'] = self.refund_af_acc_amt.to_alipay_dict()
            else:
                params['refund_af_acc_amt'] = self.refund_af_acc_amt
        if self.refund_bef_acc_amt:
            if hasattr(self.refund_bef_acc_amt, 'to_alipay_dict'):
                params['refund_bef_acc_amt'] = self.refund_bef_acc_amt.to_alipay_dict()
            else:
                params['refund_bef_acc_amt'] = self.refund_bef_acc_amt
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
        o = CreditPayOrderQueryVO()
        if 'acc_amt' in d:
            o.acc_amt = d['acc_amt']
        if 'pay_amt' in d:
            o.pay_amt = d['pay_amt']
        if 'pay_order_no' in d:
            o.pay_order_no = d['pay_order_no']
        if 'refund_af_acc_amt' in d:
            o.refund_af_acc_amt = d['refund_af_acc_amt']
        if 'refund_bef_acc_amt' in d:
            o.refund_bef_acc_amt = d['refund_bef_acc_amt']
        if 'repay_amt' in d:
            o.repay_amt = d['repay_amt']
        return o


