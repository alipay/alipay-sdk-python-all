#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Member import Member


class MybankCreditSupplychainPrepaymentApplyModel(object):

    def __init__(self):
        self._buyer = None
        self._ext_data = None
        self._loan_pay_amount = None
        self._out_order_no = None
        self._request_id = None
        self._self_pay_amount = None

    @property
    def buyer(self):
        return self._buyer

    @buyer.setter
    def buyer(self, value):
        if isinstance(value, Member):
            self._buyer = value
        else:
            self._buyer = Member.from_alipay_dict(value)
    @property
    def ext_data(self):
        return self._ext_data

    @ext_data.setter
    def ext_data(self, value):
        self._ext_data = value
    @property
    def loan_pay_amount(self):
        return self._loan_pay_amount

    @loan_pay_amount.setter
    def loan_pay_amount(self, value):
        self._loan_pay_amount = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def self_pay_amount(self):
        return self._self_pay_amount

    @self_pay_amount.setter
    def self_pay_amount(self, value):
        self._self_pay_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer:
            if hasattr(self.buyer, 'to_alipay_dict'):
                params['buyer'] = self.buyer.to_alipay_dict()
            else:
                params['buyer'] = self.buyer
        if self.ext_data:
            if hasattr(self.ext_data, 'to_alipay_dict'):
                params['ext_data'] = self.ext_data.to_alipay_dict()
            else:
                params['ext_data'] = self.ext_data
        if self.loan_pay_amount:
            if hasattr(self.loan_pay_amount, 'to_alipay_dict'):
                params['loan_pay_amount'] = self.loan_pay_amount.to_alipay_dict()
            else:
                params['loan_pay_amount'] = self.loan_pay_amount
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.self_pay_amount:
            if hasattr(self.self_pay_amount, 'to_alipay_dict'):
                params['self_pay_amount'] = self.self_pay_amount.to_alipay_dict()
            else:
                params['self_pay_amount'] = self.self_pay_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSupplychainPrepaymentApplyModel()
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'ext_data' in d:
            o.ext_data = d['ext_data']
        if 'loan_pay_amount' in d:
            o.loan_pay_amount = d['loan_pay_amount']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'self_pay_amount' in d:
            o.self_pay_amount = d['self_pay_amount']
        return o


