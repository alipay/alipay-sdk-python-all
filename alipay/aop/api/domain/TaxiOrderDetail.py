#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaxiOrderDetail(object):

    def __init__(self):
        self._order_amount = None
        self._risk_control_reason = None
        self._trade_no = None
        self._trade_time = None
        self._triggered_award = None

    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def risk_control_reason(self):
        return self._risk_control_reason

    @risk_control_reason.setter
    def risk_control_reason(self, value):
        self._risk_control_reason = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_time(self):
        return self._trade_time

    @trade_time.setter
    def trade_time(self, value):
        self._trade_time = value
    @property
    def triggered_award(self):
        return self._triggered_award

    @triggered_award.setter
    def triggered_award(self, value):
        self._triggered_award = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.risk_control_reason:
            if hasattr(self.risk_control_reason, 'to_alipay_dict'):
                params['risk_control_reason'] = self.risk_control_reason.to_alipay_dict()
            else:
                params['risk_control_reason'] = self.risk_control_reason
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_time:
            if hasattr(self.trade_time, 'to_alipay_dict'):
                params['trade_time'] = self.trade_time.to_alipay_dict()
            else:
                params['trade_time'] = self.trade_time
        if self.triggered_award:
            if hasattr(self.triggered_award, 'to_alipay_dict'):
                params['triggered_award'] = self.triggered_award.to_alipay_dict()
            else:
                params['triggered_award'] = self.triggered_award
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaxiOrderDetail()
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'risk_control_reason' in d:
            o.risk_control_reason = d['risk_control_reason']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_time' in d:
            o.trade_time = d['trade_time']
        if 'triggered_award' in d:
            o.triggered_award = d['triggered_award']
        return o


