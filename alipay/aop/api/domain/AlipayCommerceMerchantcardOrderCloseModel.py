#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMerchantcardOrderCloseModel(object):

    def __init__(self):
        self._card_id = None
        self._damages_cash = None
        self._deduction_type = None
        self._open_id = None
        self._total_cash = None
        self._user_id = None

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def damages_cash(self):
        return self._damages_cash

    @damages_cash.setter
    def damages_cash(self, value):
        self._damages_cash = value
    @property
    def deduction_type(self):
        return self._deduction_type

    @deduction_type.setter
    def deduction_type(self, value):
        self._deduction_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def total_cash(self):
        return self._total_cash

    @total_cash.setter
    def total_cash(self, value):
        self._total_cash = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.damages_cash:
            if hasattr(self.damages_cash, 'to_alipay_dict'):
                params['damages_cash'] = self.damages_cash.to_alipay_dict()
            else:
                params['damages_cash'] = self.damages_cash
        if self.deduction_type:
            if hasattr(self.deduction_type, 'to_alipay_dict'):
                params['deduction_type'] = self.deduction_type.to_alipay_dict()
            else:
                params['deduction_type'] = self.deduction_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.total_cash:
            if hasattr(self.total_cash, 'to_alipay_dict'):
                params['total_cash'] = self.total_cash.to_alipay_dict()
            else:
                params['total_cash'] = self.total_cash
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardOrderCloseModel()
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'damages_cash' in d:
            o.damages_cash = d['damages_cash']
        if 'deduction_type' in d:
            o.deduction_type = d['deduction_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'total_cash' in d:
            o.total_cash = d['total_cash']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


