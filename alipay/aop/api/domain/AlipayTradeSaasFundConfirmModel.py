#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeSaasFundConfirmModel(object):

    def __init__(self):
        self._action = None
        self._claim_amount = None
        self._claim_request_no = None
        self._fund_no = None
        self._order_no = None
        self._trade_no = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def claim_amount(self):
        return self._claim_amount

    @claim_amount.setter
    def claim_amount(self, value):
        self._claim_amount = value
    @property
    def claim_request_no(self):
        return self._claim_request_no

    @claim_request_no.setter
    def claim_request_no(self, value):
        self._claim_request_no = value
    @property
    def fund_no(self):
        return self._fund_no

    @fund_no.setter
    def fund_no(self, value):
        self._fund_no = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.claim_amount:
            if hasattr(self.claim_amount, 'to_alipay_dict'):
                params['claim_amount'] = self.claim_amount.to_alipay_dict()
            else:
                params['claim_amount'] = self.claim_amount
        if self.claim_request_no:
            if hasattr(self.claim_request_no, 'to_alipay_dict'):
                params['claim_request_no'] = self.claim_request_no.to_alipay_dict()
            else:
                params['claim_request_no'] = self.claim_request_no
        if self.fund_no:
            if hasattr(self.fund_no, 'to_alipay_dict'):
                params['fund_no'] = self.fund_no.to_alipay_dict()
            else:
                params['fund_no'] = self.fund_no
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
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
        o = AlipayTradeSaasFundConfirmModel()
        if 'action' in d:
            o.action = d['action']
        if 'claim_amount' in d:
            o.claim_amount = d['claim_amount']
        if 'claim_request_no' in d:
            o.claim_request_no = d['claim_request_no']
        if 'fund_no' in d:
            o.fund_no = d['fund_no']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


