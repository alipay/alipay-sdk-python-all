#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundBailOperationDepositCreateModel(object):

    def __init__(self):
        self._agreement_no = None
        self._amount = None
        self._extra_param = None
        self._operation_title = None
        self._out_request_no = None
        self._pay_timeout = None
        self._product_code = None
        self._remark = None
        self._user_nick = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def extra_param(self):
        return self._extra_param

    @extra_param.setter
    def extra_param(self, value):
        self._extra_param = value
    @property
    def operation_title(self):
        return self._operation_title

    @operation_title.setter
    def operation_title(self, value):
        self._operation_title = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def pay_timeout(self):
        return self._pay_timeout

    @pay_timeout.setter
    def pay_timeout(self, value):
        self._pay_timeout = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def user_nick(self):
        return self._user_nick

    @user_nick.setter
    def user_nick(self, value):
        self._user_nick = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.extra_param:
            if hasattr(self.extra_param, 'to_alipay_dict'):
                params['extra_param'] = self.extra_param.to_alipay_dict()
            else:
                params['extra_param'] = self.extra_param
        if self.operation_title:
            if hasattr(self.operation_title, 'to_alipay_dict'):
                params['operation_title'] = self.operation_title.to_alipay_dict()
            else:
                params['operation_title'] = self.operation_title
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.pay_timeout:
            if hasattr(self.pay_timeout, 'to_alipay_dict'):
                params['pay_timeout'] = self.pay_timeout.to_alipay_dict()
            else:
                params['pay_timeout'] = self.pay_timeout
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.user_nick:
            if hasattr(self.user_nick, 'to_alipay_dict'):
                params['user_nick'] = self.user_nick.to_alipay_dict()
            else:
                params['user_nick'] = self.user_nick
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundBailOperationDepositCreateModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'amount' in d:
            o.amount = d['amount']
        if 'extra_param' in d:
            o.extra_param = d['extra_param']
        if 'operation_title' in d:
            o.operation_title = d['operation_title']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'pay_timeout' in d:
            o.pay_timeout = d['pay_timeout']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'remark' in d:
            o.remark = d['remark']
        if 'user_nick' in d:
            o.user_nick = d['user_nick']
        return o


