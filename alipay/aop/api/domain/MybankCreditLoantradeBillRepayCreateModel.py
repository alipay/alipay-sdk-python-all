#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BillRepayRequest import BillRepayRequest
from alipay.aop.api.domain.UserVo import UserVo


class MybankCreditLoantradeBillRepayCreateModel(object):

    def __init__(self):
        self._bill_no = None
        self._bill_repay_request = None
        self._out_request_no = None
        self._pay_card_no = None
        self._product_code = None
        self._user = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def bill_repay_request(self):
        return self._bill_repay_request

    @bill_repay_request.setter
    def bill_repay_request(self, value):
        if isinstance(value, BillRepayRequest):
            self._bill_repay_request = value
        else:
            self._bill_repay_request = BillRepayRequest.from_alipay_dict(value)
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def pay_card_no(self):
        return self._pay_card_no

    @pay_card_no.setter
    def pay_card_no(self, value):
        self._pay_card_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if isinstance(value, UserVo):
            self._user = value
        else:
            self._user = UserVo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.bill_repay_request:
            if hasattr(self.bill_repay_request, 'to_alipay_dict'):
                params['bill_repay_request'] = self.bill_repay_request.to_alipay_dict()
            else:
                params['bill_repay_request'] = self.bill_repay_request
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.pay_card_no:
            if hasattr(self.pay_card_no, 'to_alipay_dict'):
                params['pay_card_no'] = self.pay_card_no.to_alipay_dict()
            else:
                params['pay_card_no'] = self.pay_card_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.user:
            if hasattr(self.user, 'to_alipay_dict'):
                params['user'] = self.user.to_alipay_dict()
            else:
                params['user'] = self.user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradeBillRepayCreateModel()
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'bill_repay_request' in d:
            o.bill_repay_request = d['bill_repay_request']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'pay_card_no' in d:
            o.pay_card_no = d['pay_card_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'user' in d:
            o.user = d['user']
        return o


