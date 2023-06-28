#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WalletOperation(object):

    def __init__(self):
        self._biz_type = None
        self._trans_dt = None
        self._trans_order = None
        self._wallet_trans_amount = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def trans_dt(self):
        return self._trans_dt

    @trans_dt.setter
    def trans_dt(self, value):
        self._trans_dt = value
    @property
    def trans_order(self):
        return self._trans_order

    @trans_order.setter
    def trans_order(self, value):
        if isinstance(value, list):
            self._trans_order = list()
            for i in value:
                self._trans_order.append(i)
    @property
    def wallet_trans_amount(self):
        return self._wallet_trans_amount

    @wallet_trans_amount.setter
    def wallet_trans_amount(self, value):
        self._wallet_trans_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.trans_dt:
            if hasattr(self.trans_dt, 'to_alipay_dict'):
                params['trans_dt'] = self.trans_dt.to_alipay_dict()
            else:
                params['trans_dt'] = self.trans_dt
        if self.trans_order:
            if isinstance(self.trans_order, list):
                for i in range(0, len(self.trans_order)):
                    element = self.trans_order[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trans_order[i] = element.to_alipay_dict()
            if hasattr(self.trans_order, 'to_alipay_dict'):
                params['trans_order'] = self.trans_order.to_alipay_dict()
            else:
                params['trans_order'] = self.trans_order
        if self.wallet_trans_amount:
            if hasattr(self.wallet_trans_amount, 'to_alipay_dict'):
                params['wallet_trans_amount'] = self.wallet_trans_amount.to_alipay_dict()
            else:
                params['wallet_trans_amount'] = self.wallet_trans_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WalletOperation()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'trans_dt' in d:
            o.trans_dt = d['trans_dt']
        if 'trans_order' in d:
            o.trans_order = d['trans_order']
        if 'wallet_trans_amount' in d:
            o.wallet_trans_amount = d['wallet_trans_amount']
        return o


