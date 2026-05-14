#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationCreditphoneOnlineadvanceresultNotifyModel(object):

    def __init__(self):
        self._alipay_online_advance_pay_order_no = None
        self._inst_pay_order_no = None
        self._out_trade_no = None
        self._trade_amount = None
        self._trade_finish_time = None
        self._trade_no = None

    @property
    def alipay_online_advance_pay_order_no(self):
        return self._alipay_online_advance_pay_order_no

    @alipay_online_advance_pay_order_no.setter
    def alipay_online_advance_pay_order_no(self, value):
        self._alipay_online_advance_pay_order_no = value
    @property
    def inst_pay_order_no(self):
        return self._inst_pay_order_no

    @inst_pay_order_no.setter
    def inst_pay_order_no(self, value):
        self._inst_pay_order_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def trade_amount(self):
        return self._trade_amount

    @trade_amount.setter
    def trade_amount(self, value):
        self._trade_amount = value
    @property
    def trade_finish_time(self):
        return self._trade_finish_time

    @trade_finish_time.setter
    def trade_finish_time(self, value):
        self._trade_finish_time = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_online_advance_pay_order_no:
            if hasattr(self.alipay_online_advance_pay_order_no, 'to_alipay_dict'):
                params['alipay_online_advance_pay_order_no'] = self.alipay_online_advance_pay_order_no.to_alipay_dict()
            else:
                params['alipay_online_advance_pay_order_no'] = self.alipay_online_advance_pay_order_no
        if self.inst_pay_order_no:
            if hasattr(self.inst_pay_order_no, 'to_alipay_dict'):
                params['inst_pay_order_no'] = self.inst_pay_order_no.to_alipay_dict()
            else:
                params['inst_pay_order_no'] = self.inst_pay_order_no
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.trade_amount:
            if hasattr(self.trade_amount, 'to_alipay_dict'):
                params['trade_amount'] = self.trade_amount.to_alipay_dict()
            else:
                params['trade_amount'] = self.trade_amount
        if self.trade_finish_time:
            if hasattr(self.trade_finish_time, 'to_alipay_dict'):
                params['trade_finish_time'] = self.trade_finish_time.to_alipay_dict()
            else:
                params['trade_finish_time'] = self.trade_finish_time
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
        o = AlipayCommerceAcommunicationCreditphoneOnlineadvanceresultNotifyModel()
        if 'alipay_online_advance_pay_order_no' in d:
            o.alipay_online_advance_pay_order_no = d['alipay_online_advance_pay_order_no']
        if 'inst_pay_order_no' in d:
            o.inst_pay_order_no = d['inst_pay_order_no']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'trade_amount' in d:
            o.trade_amount = d['trade_amount']
        if 'trade_finish_time' in d:
            o.trade_finish_time = d['trade_finish_time']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


