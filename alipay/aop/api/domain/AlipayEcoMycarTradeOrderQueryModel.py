#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarTradeOrderQueryModel(object):

    def __init__(self):
        self._biz_trade_no = None
        self._out_biz_trade_no = None
        self._trade_no = None

    @property
    def biz_trade_no(self):
        return self._biz_trade_no

    @biz_trade_no.setter
    def biz_trade_no(self, value):
        self._biz_trade_no = value
    @property
    def out_biz_trade_no(self):
        return self._out_biz_trade_no

    @out_biz_trade_no.setter
    def out_biz_trade_no(self, value):
        self._out_biz_trade_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_trade_no:
            if hasattr(self.biz_trade_no, 'to_alipay_dict'):
                params['biz_trade_no'] = self.biz_trade_no.to_alipay_dict()
            else:
                params['biz_trade_no'] = self.biz_trade_no
        if self.out_biz_trade_no:
            if hasattr(self.out_biz_trade_no, 'to_alipay_dict'):
                params['out_biz_trade_no'] = self.out_biz_trade_no.to_alipay_dict()
            else:
                params['out_biz_trade_no'] = self.out_biz_trade_no
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
        o = AlipayEcoMycarTradeOrderQueryModel()
        if 'biz_trade_no' in d:
            o.biz_trade_no = d['biz_trade_no']
        if 'out_biz_trade_no' in d:
            o.out_biz_trade_no = d['out_biz_trade_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


