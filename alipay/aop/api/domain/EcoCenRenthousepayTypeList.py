#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EcoRenthouseOtherAmount import EcoRenthouseOtherAmount


class EcoCenRenthousepayTypeList(object):

    def __init__(self):
        self._foregift_amount = None
        self._max_amount = None
        self._max_deposit_amount = None
        self._other_amount = None
        self._pay_type = None
        self._room_amount = None

    @property
    def foregift_amount(self):
        return self._foregift_amount

    @foregift_amount.setter
    def foregift_amount(self, value):
        self._foregift_amount = value
    @property
    def max_amount(self):
        return self._max_amount

    @max_amount.setter
    def max_amount(self, value):
        self._max_amount = value
    @property
    def max_deposit_amount(self):
        return self._max_deposit_amount

    @max_deposit_amount.setter
    def max_deposit_amount(self, value):
        self._max_deposit_amount = value
    @property
    def other_amount(self):
        return self._other_amount

    @other_amount.setter
    def other_amount(self, value):
        if isinstance(value, list):
            self._other_amount = list()
            for i in value:
                if isinstance(i, EcoRenthouseOtherAmount):
                    self._other_amount.append(i)
                else:
                    self._other_amount.append(EcoRenthouseOtherAmount.from_alipay_dict(i))
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def room_amount(self):
        return self._room_amount

    @room_amount.setter
    def room_amount(self, value):
        self._room_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.foregift_amount:
            if hasattr(self.foregift_amount, 'to_alipay_dict'):
                params['foregift_amount'] = self.foregift_amount.to_alipay_dict()
            else:
                params['foregift_amount'] = self.foregift_amount
        if self.max_amount:
            if hasattr(self.max_amount, 'to_alipay_dict'):
                params['max_amount'] = self.max_amount.to_alipay_dict()
            else:
                params['max_amount'] = self.max_amount
        if self.max_deposit_amount:
            if hasattr(self.max_deposit_amount, 'to_alipay_dict'):
                params['max_deposit_amount'] = self.max_deposit_amount.to_alipay_dict()
            else:
                params['max_deposit_amount'] = self.max_deposit_amount
        if self.other_amount:
            if isinstance(self.other_amount, list):
                for i in range(0, len(self.other_amount)):
                    element = self.other_amount[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_amount[i] = element.to_alipay_dict()
            if hasattr(self.other_amount, 'to_alipay_dict'):
                params['other_amount'] = self.other_amount.to_alipay_dict()
            else:
                params['other_amount'] = self.other_amount
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.room_amount:
            if hasattr(self.room_amount, 'to_alipay_dict'):
                params['room_amount'] = self.room_amount.to_alipay_dict()
            else:
                params['room_amount'] = self.room_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcoCenRenthousepayTypeList()
        if 'foregift_amount' in d:
            o.foregift_amount = d['foregift_amount']
        if 'max_amount' in d:
            o.max_amount = d['max_amount']
        if 'max_deposit_amount' in d:
            o.max_deposit_amount = d['max_deposit_amount']
        if 'other_amount' in d:
            o.other_amount = d['other_amount']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'room_amount' in d:
            o.room_amount = d['room_amount']
        return o


