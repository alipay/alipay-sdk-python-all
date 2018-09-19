#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DishonorOrder(object):

    def __init__(self):
        self._amount = None
        self._dishonor_date = None
        self._fail_reason = None
        self._order_id = None
        self._out_biz_no = None
        self._pay_date = None
        self._payer_account = None
        self._payment_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def dishonor_date(self):
        return self._dishonor_date

    @dishonor_date.setter
    def dishonor_date(self, value):
        self._dishonor_date = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def pay_date(self):
        return self._pay_date

    @pay_date.setter
    def pay_date(self, value):
        self._pay_date = value
    @property
    def payer_account(self):
        return self._payer_account

    @payer_account.setter
    def payer_account(self, value):
        self._payer_account = value
    @property
    def payment_no(self):
        return self._payment_no

    @payment_no.setter
    def payment_no(self, value):
        self._payment_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.dishonor_date:
            if hasattr(self.dishonor_date, 'to_alipay_dict'):
                params['dishonor_date'] = self.dishonor_date.to_alipay_dict()
            else:
                params['dishonor_date'] = self.dishonor_date
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.pay_date:
            if hasattr(self.pay_date, 'to_alipay_dict'):
                params['pay_date'] = self.pay_date.to_alipay_dict()
            else:
                params['pay_date'] = self.pay_date
        if self.payer_account:
            if hasattr(self.payer_account, 'to_alipay_dict'):
                params['payer_account'] = self.payer_account.to_alipay_dict()
            else:
                params['payer_account'] = self.payer_account
        if self.payment_no:
            if hasattr(self.payment_no, 'to_alipay_dict'):
                params['payment_no'] = self.payment_no.to_alipay_dict()
            else:
                params['payment_no'] = self.payment_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DishonorOrder()
        if 'amount' in d:
            o.amount = d['amount']
        if 'dishonor_date' in d:
            o.dishonor_date = d['dishonor_date']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'pay_date' in d:
            o.pay_date = d['pay_date']
        if 'payer_account' in d:
            o.payer_account = d['payer_account']
        if 'payment_no' in d:
            o.payment_no = d['payment_no']
        return o


