#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Member import Member


class MybankCreditSupplychainTradePayConfirmModel(object):

    def __init__(self):
        self._buyer = None
        self._out_order_no = None
        self._prepay_order_no = None
        self._request_id = None

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
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def prepay_order_no(self):
        return self._prepay_order_no

    @prepay_order_no.setter
    def prepay_order_no(self, value):
        self._prepay_order_no = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer:
            if hasattr(self.buyer, 'to_alipay_dict'):
                params['buyer'] = self.buyer.to_alipay_dict()
            else:
                params['buyer'] = self.buyer
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.prepay_order_no:
            if hasattr(self.prepay_order_no, 'to_alipay_dict'):
                params['prepay_order_no'] = self.prepay_order_no.to_alipay_dict()
            else:
                params['prepay_order_no'] = self.prepay_order_no
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSupplychainTradePayConfirmModel()
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'prepay_order_no' in d:
            o.prepay_order_no = d['prepay_order_no']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


