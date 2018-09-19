#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsAutoFeeReceiveConfirmModel(object):

    def __init__(self):
        self._out_biz_no = None
        self._trade_amount = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def trade_amount(self):
        return self._trade_amount

    @trade_amount.setter
    def trade_amount(self, value):
        self._trade_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.trade_amount:
            if hasattr(self.trade_amount, 'to_alipay_dict'):
                params['trade_amount'] = self.trade_amount.to_alipay_dict()
            else:
                params['trade_amount'] = self.trade_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsAutoFeeReceiveConfirmModel()
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'trade_amount' in d:
            o.trade_amount = d['trade_amount']
        return o


