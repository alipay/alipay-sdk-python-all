#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMerchantcardAftersalesConfirmModel(object):

    def __init__(self):
        self._aftersales_id = None
        self._damages_cash = None
        self._refund_cash = None

    @property
    def aftersales_id(self):
        return self._aftersales_id

    @aftersales_id.setter
    def aftersales_id(self, value):
        self._aftersales_id = value
    @property
    def damages_cash(self):
        return self._damages_cash

    @damages_cash.setter
    def damages_cash(self, value):
        self._damages_cash = value
    @property
    def refund_cash(self):
        return self._refund_cash

    @refund_cash.setter
    def refund_cash(self, value):
        self._refund_cash = value


    def to_alipay_dict(self):
        params = dict()
        if self.aftersales_id:
            if hasattr(self.aftersales_id, 'to_alipay_dict'):
                params['aftersales_id'] = self.aftersales_id.to_alipay_dict()
            else:
                params['aftersales_id'] = self.aftersales_id
        if self.damages_cash:
            if hasattr(self.damages_cash, 'to_alipay_dict'):
                params['damages_cash'] = self.damages_cash.to_alipay_dict()
            else:
                params['damages_cash'] = self.damages_cash
        if self.refund_cash:
            if hasattr(self.refund_cash, 'to_alipay_dict'):
                params['refund_cash'] = self.refund_cash.to_alipay_dict()
            else:
                params['refund_cash'] = self.refund_cash
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardAftersalesConfirmModel()
        if 'aftersales_id' in d:
            o.aftersales_id = d['aftersales_id']
        if 'damages_cash' in d:
            o.damages_cash = d['damages_cash']
        if 'refund_cash' in d:
            o.refund_cash = d['refund_cash']
        return o


