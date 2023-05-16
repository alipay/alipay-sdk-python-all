#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndrISVChargeDetailDTO import IndrISVChargeDetailDTO
from alipay.aop.api.domain.IndrMoneyDTO import IndrMoneyDTO
from alipay.aop.api.domain.IndrMoneyDTO import IndrMoneyDTO
from alipay.aop.api.domain.IndrMoneyDTO import IndrMoneyDTO


class IndrISVAmountInfoDTO(object):

    def __init__(self):
        self._charge_details = None
        self._exchange_rate = None
        self._original_amount = None
        self._target_amount = None
        self._total_amount = None

    @property
    def charge_details(self):
        return self._charge_details

    @charge_details.setter
    def charge_details(self, value):
        if isinstance(value, IndrISVChargeDetailDTO):
            self._charge_details = value
        else:
            self._charge_details = IndrISVChargeDetailDTO.from_alipay_dict(value)
    @property
    def exchange_rate(self):
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, value):
        self._exchange_rate = value
    @property
    def original_amount(self):
        return self._original_amount

    @original_amount.setter
    def original_amount(self, value):
        if isinstance(value, IndrMoneyDTO):
            self._original_amount = value
        else:
            self._original_amount = IndrMoneyDTO.from_alipay_dict(value)
    @property
    def target_amount(self):
        return self._target_amount

    @target_amount.setter
    def target_amount(self, value):
        if isinstance(value, IndrMoneyDTO):
            self._target_amount = value
        else:
            self._target_amount = IndrMoneyDTO.from_alipay_dict(value)
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        if isinstance(value, IndrMoneyDTO):
            self._total_amount = value
        else:
            self._total_amount = IndrMoneyDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.charge_details:
            if hasattr(self.charge_details, 'to_alipay_dict'):
                params['charge_details'] = self.charge_details.to_alipay_dict()
            else:
                params['charge_details'] = self.charge_details
        if self.exchange_rate:
            if hasattr(self.exchange_rate, 'to_alipay_dict'):
                params['exchange_rate'] = self.exchange_rate.to_alipay_dict()
            else:
                params['exchange_rate'] = self.exchange_rate
        if self.original_amount:
            if hasattr(self.original_amount, 'to_alipay_dict'):
                params['original_amount'] = self.original_amount.to_alipay_dict()
            else:
                params['original_amount'] = self.original_amount
        if self.target_amount:
            if hasattr(self.target_amount, 'to_alipay_dict'):
                params['target_amount'] = self.target_amount.to_alipay_dict()
            else:
                params['target_amount'] = self.target_amount
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndrISVAmountInfoDTO()
        if 'charge_details' in d:
            o.charge_details = d['charge_details']
        if 'exchange_rate' in d:
            o.exchange_rate = d['exchange_rate']
        if 'original_amount' in d:
            o.original_amount = d['original_amount']
        if 'target_amount' in d:
            o.target_amount = d['target_amount']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


