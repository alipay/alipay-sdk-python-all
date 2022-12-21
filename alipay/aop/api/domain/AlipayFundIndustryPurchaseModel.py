#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundIndustryPurchaseModel(object):

    def __init__(self):
        self._agreement_no = None
        self._amount = None
        self._gmt_pay = None
        self._open_id = None
        self._openid = None
        self._order_timeout = None
        self._out_request_no = None
        self._user_id = None

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
    def gmt_pay(self):
        return self._gmt_pay

    @gmt_pay.setter
    def gmt_pay(self, value):
        self._gmt_pay = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def openid(self):
        return self._openid

    @openid.setter
    def openid(self, value):
        self._openid = value
    @property
    def order_timeout(self):
        return self._order_timeout

    @order_timeout.setter
    def order_timeout(self, value):
        self._order_timeout = value
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
        if self.gmt_pay:
            if hasattr(self.gmt_pay, 'to_alipay_dict'):
                params['gmt_pay'] = self.gmt_pay.to_alipay_dict()
            else:
                params['gmt_pay'] = self.gmt_pay
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.openid:
            if hasattr(self.openid, 'to_alipay_dict'):
                params['openid'] = self.openid.to_alipay_dict()
            else:
                params['openid'] = self.openid
        if self.order_timeout:
            if hasattr(self.order_timeout, 'to_alipay_dict'):
                params['order_timeout'] = self.order_timeout.to_alipay_dict()
            else:
                params['order_timeout'] = self.order_timeout
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
        o = AlipayFundIndustryPurchaseModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'amount' in d:
            o.amount = d['amount']
        if 'gmt_pay' in d:
            o.gmt_pay = d['gmt_pay']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'openid' in d:
            o.openid = d['openid']
        if 'order_timeout' in d:
            o.order_timeout = d['order_timeout']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


