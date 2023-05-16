#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndrMoneyDTO import IndrMoneyDTO


class IndrISVChargeDetailDTO(object):

    def __init__(self):
        self._fee_amount = None
        self._fee_name = None

    @property
    def fee_amount(self):
        return self._fee_amount

    @fee_amount.setter
    def fee_amount(self, value):
        if isinstance(value, IndrMoneyDTO):
            self._fee_amount = value
        else:
            self._fee_amount = IndrMoneyDTO.from_alipay_dict(value)
    @property
    def fee_name(self):
        return self._fee_name

    @fee_name.setter
    def fee_name(self, value):
        self._fee_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.fee_amount:
            if hasattr(self.fee_amount, 'to_alipay_dict'):
                params['fee_amount'] = self.fee_amount.to_alipay_dict()
            else:
                params['fee_amount'] = self.fee_amount
        if self.fee_name:
            if hasattr(self.fee_name, 'to_alipay_dict'):
                params['fee_name'] = self.fee_name.to_alipay_dict()
            else:
                params['fee_name'] = self.fee_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndrISVChargeDetailDTO()
        if 'fee_amount' in d:
            o.fee_amount = d['fee_amount']
        if 'fee_name' in d:
            o.fee_name = d['fee_name']
        return o


