#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WithholdTradeDTO(object):

    def __init__(self):
        self._bill_no = None
        self._deduct = None
        self._deduct_amount = None
        self._gmt_pay = None
        self._status = None
        self._trade_no = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def deduct(self):
        return self._deduct

    @deduct.setter
    def deduct(self, value):
        self._deduct = value
    @property
    def deduct_amount(self):
        return self._deduct_amount

    @deduct_amount.setter
    def deduct_amount(self, value):
        self._deduct_amount = value
    @property
    def gmt_pay(self):
        return self._gmt_pay

    @gmt_pay.setter
    def gmt_pay(self, value):
        self._gmt_pay = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.deduct:
            if hasattr(self.deduct, 'to_alipay_dict'):
                params['deduct'] = self.deduct.to_alipay_dict()
            else:
                params['deduct'] = self.deduct
        if self.deduct_amount:
            if hasattr(self.deduct_amount, 'to_alipay_dict'):
                params['deduct_amount'] = self.deduct_amount.to_alipay_dict()
            else:
                params['deduct_amount'] = self.deduct_amount
        if self.gmt_pay:
            if hasattr(self.gmt_pay, 'to_alipay_dict'):
                params['gmt_pay'] = self.gmt_pay.to_alipay_dict()
            else:
                params['gmt_pay'] = self.gmt_pay
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WithholdTradeDTO()
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'deduct' in d:
            o.deduct = d['deduct']
        if 'deduct_amount' in d:
            o.deduct_amount = d['deduct_amount']
        if 'gmt_pay' in d:
            o.gmt_pay = d['gmt_pay']
        if 'status' in d:
            o.status = d['status']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


