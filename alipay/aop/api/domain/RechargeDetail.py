#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RechargeDetail(object):

    def __init__(self):
        self._amount = None
        self._assetamount = None
        self._orderno = None
        self._outorderno = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def assetamount(self):
        return self._assetamount

    @assetamount.setter
    def assetamount(self, value):
        self._assetamount = value
    @property
    def orderno(self):
        return self._orderno

    @orderno.setter
    def orderno(self, value):
        self._orderno = value
    @property
    def outorderno(self):
        return self._outorderno

    @outorderno.setter
    def outorderno(self, value):
        self._outorderno = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.assetamount:
            if hasattr(self.assetamount, 'to_alipay_dict'):
                params['assetamount'] = self.assetamount.to_alipay_dict()
            else:
                params['assetamount'] = self.assetamount
        if self.orderno:
            if hasattr(self.orderno, 'to_alipay_dict'):
                params['orderno'] = self.orderno.to_alipay_dict()
            else:
                params['orderno'] = self.orderno
        if self.outorderno:
            if hasattr(self.outorderno, 'to_alipay_dict'):
                params['outorderno'] = self.outorderno.to_alipay_dict()
            else:
                params['outorderno'] = self.outorderno
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RechargeDetail()
        if 'amount' in d:
            o.amount = d['amount']
        if 'assetamount' in d:
            o.assetamount = d['assetamount']
        if 'orderno' in d:
            o.orderno = d['orderno']
        if 'outorderno' in d:
            o.outorderno = d['outorderno']
        return o


