#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceDetail(object):

    def __init__(self):
        self._measurement_unit = None
        self._product_name = None
        self._product_specification = None
        self._quantity = None
        self._rate = None
        self._tax_amount = None
        self._tax_amount_currency = None
        self._tax_exclusive_amount = None
        self._tax_exclusive_amount_currency = None
        self._tax_rate = None

    @property
    def measurement_unit(self):
        return self._measurement_unit

    @measurement_unit.setter
    def measurement_unit(self, value):
        self._measurement_unit = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def product_specification(self):
        return self._product_specification

    @product_specification.setter
    def product_specification(self, value):
        self._product_specification = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value
    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self._tax_amount = value
    @property
    def tax_amount_currency(self):
        return self._tax_amount_currency

    @tax_amount_currency.setter
    def tax_amount_currency(self, value):
        self._tax_amount_currency = value
    @property
    def tax_exclusive_amount(self):
        return self._tax_exclusive_amount

    @tax_exclusive_amount.setter
    def tax_exclusive_amount(self, value):
        self._tax_exclusive_amount = value
    @property
    def tax_exclusive_amount_currency(self):
        return self._tax_exclusive_amount_currency

    @tax_exclusive_amount_currency.setter
    def tax_exclusive_amount_currency(self, value):
        self._tax_exclusive_amount_currency = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.measurement_unit:
            if hasattr(self.measurement_unit, 'to_alipay_dict'):
                params['measurement_unit'] = self.measurement_unit.to_alipay_dict()
            else:
                params['measurement_unit'] = self.measurement_unit
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.product_specification:
            if hasattr(self.product_specification, 'to_alipay_dict'):
                params['product_specification'] = self.product_specification.to_alipay_dict()
            else:
                params['product_specification'] = self.product_specification
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.rate:
            if hasattr(self.rate, 'to_alipay_dict'):
                params['rate'] = self.rate.to_alipay_dict()
            else:
                params['rate'] = self.rate
        if self.tax_amount:
            if hasattr(self.tax_amount, 'to_alipay_dict'):
                params['tax_amount'] = self.tax_amount.to_alipay_dict()
            else:
                params['tax_amount'] = self.tax_amount
        if self.tax_amount_currency:
            if hasattr(self.tax_amount_currency, 'to_alipay_dict'):
                params['tax_amount_currency'] = self.tax_amount_currency.to_alipay_dict()
            else:
                params['tax_amount_currency'] = self.tax_amount_currency
        if self.tax_exclusive_amount:
            if hasattr(self.tax_exclusive_amount, 'to_alipay_dict'):
                params['tax_exclusive_amount'] = self.tax_exclusive_amount.to_alipay_dict()
            else:
                params['tax_exclusive_amount'] = self.tax_exclusive_amount
        if self.tax_exclusive_amount_currency:
            if hasattr(self.tax_exclusive_amount_currency, 'to_alipay_dict'):
                params['tax_exclusive_amount_currency'] = self.tax_exclusive_amount_currency.to_alipay_dict()
            else:
                params['tax_exclusive_amount_currency'] = self.tax_exclusive_amount_currency
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceDetail()
        if 'measurement_unit' in d:
            o.measurement_unit = d['measurement_unit']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'product_specification' in d:
            o.product_specification = d['product_specification']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'rate' in d:
            o.rate = d['rate']
        if 'tax_amount' in d:
            o.tax_amount = d['tax_amount']
        if 'tax_amount_currency' in d:
            o.tax_amount_currency = d['tax_amount_currency']
        if 'tax_exclusive_amount' in d:
            o.tax_exclusive_amount = d['tax_exclusive_amount']
        if 'tax_exclusive_amount_currency' in d:
            o.tax_exclusive_amount_currency = d['tax_exclusive_amount_currency']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        return o


