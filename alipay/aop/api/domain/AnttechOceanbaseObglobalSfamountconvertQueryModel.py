#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObglobalSfamountconvertQueryModel(object):

    def __init__(self):
        self._amount_minor_units = None
        self._from_currency = None
        self._to_currency = None

    @property
    def amount_minor_units(self):
        return self._amount_minor_units

    @amount_minor_units.setter
    def amount_minor_units(self, value):
        self._amount_minor_units = value
    @property
    def from_currency(self):
        return self._from_currency

    @from_currency.setter
    def from_currency(self, value):
        self._from_currency = value
    @property
    def to_currency(self):
        return self._to_currency

    @to_currency.setter
    def to_currency(self, value):
        self._to_currency = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_minor_units:
            if hasattr(self.amount_minor_units, 'to_alipay_dict'):
                params['amount_minor_units'] = self.amount_minor_units.to_alipay_dict()
            else:
                params['amount_minor_units'] = self.amount_minor_units
        if self.from_currency:
            if hasattr(self.from_currency, 'to_alipay_dict'):
                params['from_currency'] = self.from_currency.to_alipay_dict()
            else:
                params['from_currency'] = self.from_currency
        if self.to_currency:
            if hasattr(self.to_currency, 'to_alipay_dict'):
                params['to_currency'] = self.to_currency.to_alipay_dict()
            else:
                params['to_currency'] = self.to_currency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalSfamountconvertQueryModel()
        if 'amount_minor_units' in d:
            o.amount_minor_units = d['amount_minor_units']
        if 'from_currency' in d:
            o.from_currency = d['from_currency']
        if 'to_currency' in d:
            o.to_currency = d['to_currency']
        return o


