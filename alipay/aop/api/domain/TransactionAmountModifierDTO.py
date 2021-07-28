#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TransactionAmountDTO import TransactionAmountDTO


class TransactionAmountModifierDTO(object):

    def __init__(self):
        self._amount = None
        self._description = None
        self._type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if isinstance(value, TransactionAmountDTO):
            self._amount = value
        else:
            self._amount = TransactionAmountDTO.from_alipay_dict(value)
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TransactionAmountModifierDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'description' in d:
            o.description = d['description']
        if 'type' in d:
            o.type = d['type']
        return o


