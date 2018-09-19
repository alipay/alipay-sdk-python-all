#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarTradeRefundModel(object):

    def __init__(self):
        self._isv = None
        self._refund_fee = None
        self._refund_reason = None
        self._trade_no = None

    @property
    def isv(self):
        return self._isv

    @isv.setter
    def isv(self, value):
        self._isv = value
    @property
    def refund_fee(self):
        return self._refund_fee

    @refund_fee.setter
    def refund_fee(self, value):
        self._refund_fee = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv:
            if hasattr(self.isv, 'to_alipay_dict'):
                params['isv'] = self.isv.to_alipay_dict()
            else:
                params['isv'] = self.isv
        if self.refund_fee:
            if hasattr(self.refund_fee, 'to_alipay_dict'):
                params['refund_fee'] = self.refund_fee.to_alipay_dict()
            else:
                params['refund_fee'] = self.refund_fee
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
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
        o = AlipayEcoMycarTradeRefundModel()
        if 'isv' in d:
            o.isv = d['isv']
        if 'refund_fee' in d:
            o.refund_fee = d['refund_fee']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


