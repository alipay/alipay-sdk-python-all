#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TuitionISVChargeDetailDTO import TuitionISVChargeDetailDTO
from alipay.aop.api.domain.TuitionMoneyDTO import TuitionMoneyDTO
from alipay.aop.api.domain.TuitionMoneyDTO import TuitionMoneyDTO
from alipay.aop.api.domain.TuitionMoneyDTO import TuitionMoneyDTO


class TuitionISVAmountInfoDTO(object):

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
        if isinstance(value, list):
            self._charge_details = list()
            for i in value:
                if isinstance(i, TuitionISVChargeDetailDTO):
                    self._charge_details.append(i)
                else:
                    self._charge_details.append(TuitionISVChargeDetailDTO.from_alipay_dict(i))
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
        if isinstance(value, TuitionMoneyDTO):
            self._original_amount = value
        else:
            self._original_amount = TuitionMoneyDTO.from_alipay_dict(value)
    @property
    def target_amount(self):
        return self._target_amount

    @target_amount.setter
    def target_amount(self, value):
        if isinstance(value, TuitionMoneyDTO):
            self._target_amount = value
        else:
            self._target_amount = TuitionMoneyDTO.from_alipay_dict(value)
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        if isinstance(value, TuitionMoneyDTO):
            self._total_amount = value
        else:
            self._total_amount = TuitionMoneyDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.charge_details:
            if isinstance(self.charge_details, list):
                for i in range(0, len(self.charge_details)):
                    element = self.charge_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.charge_details[i] = element.to_alipay_dict()
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
        o = TuitionISVAmountInfoDTO()
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


