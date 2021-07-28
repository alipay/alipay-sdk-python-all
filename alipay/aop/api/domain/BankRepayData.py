#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BankRepayData(object):

    def __init__(self):
        self._original_out_trade_no = None
        self._original_trade_no = None

    @property
    def original_out_trade_no(self):
        return self._original_out_trade_no

    @original_out_trade_no.setter
    def original_out_trade_no(self, value):
        self._original_out_trade_no = value
    @property
    def original_trade_no(self):
        return self._original_trade_no

    @original_trade_no.setter
    def original_trade_no(self, value):
        self._original_trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.original_out_trade_no:
            if hasattr(self.original_out_trade_no, 'to_alipay_dict'):
                params['original_out_trade_no'] = self.original_out_trade_no.to_alipay_dict()
            else:
                params['original_out_trade_no'] = self.original_out_trade_no
        if self.original_trade_no:
            if hasattr(self.original_trade_no, 'to_alipay_dict'):
                params['original_trade_no'] = self.original_trade_no.to_alipay_dict()
            else:
                params['original_trade_no'] = self.original_trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BankRepayData()
        if 'original_out_trade_no' in d:
            o.original_out_trade_no = d['original_out_trade_no']
        if 'original_trade_no' in d:
            o.original_trade_no = d['original_trade_no']
        return o


