#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OperationExtDataModel(object):

    def __init__(self):
        self._prize_amount = None
        self._prize_id = None
        self._prize_name = None
        self._promo_error_code = None

    @property
    def prize_amount(self):
        return self._prize_amount

    @prize_amount.setter
    def prize_amount(self, value):
        self._prize_amount = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value
    @property
    def promo_error_code(self):
        return self._promo_error_code

    @promo_error_code.setter
    def promo_error_code(self, value):
        self._promo_error_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.prize_amount:
            if hasattr(self.prize_amount, 'to_alipay_dict'):
                params['prize_amount'] = self.prize_amount.to_alipay_dict()
            else:
                params['prize_amount'] = self.prize_amount
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.prize_name:
            if hasattr(self.prize_name, 'to_alipay_dict'):
                params['prize_name'] = self.prize_name.to_alipay_dict()
            else:
                params['prize_name'] = self.prize_name
        if self.promo_error_code:
            if hasattr(self.promo_error_code, 'to_alipay_dict'):
                params['promo_error_code'] = self.promo_error_code.to_alipay_dict()
            else:
                params['promo_error_code'] = self.promo_error_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OperationExtDataModel()
        if 'prize_amount' in d:
            o.prize_amount = d['prize_amount']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        if 'promo_error_code' in d:
            o.promo_error_code = d['promo_error_code']
        return o


