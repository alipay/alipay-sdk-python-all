#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeRepaybillBillinConfirmModel(object):

    def __init__(self):
        self._amount = None
        self._bill_product = None
        self._biz_debts_out_amount = None
        self._biz_no = None
        self._out_bill_no = None
        self._out_request_no = None
        self._user_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def bill_product(self):
        return self._bill_product

    @bill_product.setter
    def bill_product(self, value):
        self._bill_product = value
    @property
    def biz_debts_out_amount(self):
        return self._biz_debts_out_amount

    @biz_debts_out_amount.setter
    def biz_debts_out_amount(self, value):
        self._biz_debts_out_amount = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def out_bill_no(self):
        return self._out_bill_no

    @out_bill_no.setter
    def out_bill_no(self, value):
        self._out_bill_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.bill_product:
            if hasattr(self.bill_product, 'to_alipay_dict'):
                params['bill_product'] = self.bill_product.to_alipay_dict()
            else:
                params['bill_product'] = self.bill_product
        if self.biz_debts_out_amount:
            if hasattr(self.biz_debts_out_amount, 'to_alipay_dict'):
                params['biz_debts_out_amount'] = self.biz_debts_out_amount.to_alipay_dict()
            else:
                params['biz_debts_out_amount'] = self.biz_debts_out_amount
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.out_bill_no:
            if hasattr(self.out_bill_no, 'to_alipay_dict'):
                params['out_bill_no'] = self.out_bill_no.to_alipay_dict()
            else:
                params['out_bill_no'] = self.out_bill_no
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeRepaybillBillinConfirmModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'bill_product' in d:
            o.bill_product = d['bill_product']
        if 'biz_debts_out_amount' in d:
            o.biz_debts_out_amount = d['biz_debts_out_amount']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'out_bill_no' in d:
            o.out_bill_no = d['out_bill_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


