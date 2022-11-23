#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Amount import Amount


class GiftInfoDTO(object):

    def __init__(self):
        self._floor_amount = None
        self._gift = None

    @property
    def floor_amount(self):
        return self._floor_amount

    @floor_amount.setter
    def floor_amount(self, value):
        if isinstance(value, Amount):
            self._floor_amount = value
        else:
            self._floor_amount = Amount.from_alipay_dict(value)
    @property
    def gift(self):
        return self._gift

    @gift.setter
    def gift(self, value):
        self._gift = value


    def to_alipay_dict(self):
        params = dict()
        if self.floor_amount:
            if hasattr(self.floor_amount, 'to_alipay_dict'):
                params['floor_amount'] = self.floor_amount.to_alipay_dict()
            else:
                params['floor_amount'] = self.floor_amount
        if self.gift:
            if hasattr(self.gift, 'to_alipay_dict'):
                params['gift'] = self.gift.to_alipay_dict()
            else:
                params['gift'] = self.gift
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GiftInfoDTO()
        if 'floor_amount' in d:
            o.floor_amount = d['floor_amount']
        if 'gift' in d:
            o.gift = d['gift']
        return o


