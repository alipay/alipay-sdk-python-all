#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SyncVoiceVO(object):

    def __init__(self):
        self._amount = None
        self._merge_switch = None
        self._money_switch = None
        self._pay_type = None
        self._trade_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def merge_switch(self):
        return self._merge_switch

    @merge_switch.setter
    def merge_switch(self, value):
        self._merge_switch = value
    @property
    def money_switch(self):
        return self._money_switch

    @money_switch.setter
    def money_switch(self, value):
        self._money_switch = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, value):
        self._trade_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.merge_switch:
            if hasattr(self.merge_switch, 'to_alipay_dict'):
                params['merge_switch'] = self.merge_switch.to_alipay_dict()
            else:
                params['merge_switch'] = self.merge_switch
        if self.money_switch:
            if hasattr(self.money_switch, 'to_alipay_dict'):
                params['money_switch'] = self.money_switch.to_alipay_dict()
            else:
                params['money_switch'] = self.money_switch
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.trade_id:
            if hasattr(self.trade_id, 'to_alipay_dict'):
                params['trade_id'] = self.trade_id.to_alipay_dict()
            else:
                params['trade_id'] = self.trade_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SyncVoiceVO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'merge_switch' in d:
            o.merge_switch = d['merge_switch']
        if 'money_switch' in d:
            o.money_switch = d['money_switch']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'trade_id' in d:
            o.trade_id = d['trade_id']
        return o


