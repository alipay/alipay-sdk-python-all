#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeOrderSettleQueryModel(object):

    def __init__(self):
        self._out_request_no = None
        self._settle_no = None
        self._trade_no = None

    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def settle_no(self):
        return self._settle_no

    @settle_no.setter
    def settle_no(self, value):
        self._settle_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.settle_no:
            if hasattr(self.settle_no, 'to_alipay_dict'):
                params['settle_no'] = self.settle_no.to_alipay_dict()
            else:
                params['settle_no'] = self.settle_no
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
        o = AlipayTradeOrderSettleQueryModel()
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'settle_no' in d:
            o.settle_no = d['settle_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


