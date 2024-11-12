#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayInfoResponse(object):

    def __init__(self):
        self._no_pay_close_time = None
        self._trade_no = None

    @property
    def no_pay_close_time(self):
        return self._no_pay_close_time

    @no_pay_close_time.setter
    def no_pay_close_time(self, value):
        self._no_pay_close_time = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.no_pay_close_time:
            if hasattr(self.no_pay_close_time, 'to_alipay_dict'):
                params['no_pay_close_time'] = self.no_pay_close_time.to_alipay_dict()
            else:
                params['no_pay_close_time'] = self.no_pay_close_time
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
        o = PayInfoResponse()
        if 'no_pay_close_time' in d:
            o.no_pay_close_time = d['no_pay_close_time']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


