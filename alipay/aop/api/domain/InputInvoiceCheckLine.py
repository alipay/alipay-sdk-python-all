#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InputInvoiceCheckLine(object):

    def __init__(self):
        self._amount = None
        self._currency = None
        self._duty_free_flag = None
        self._measurement_unit = None
        self._product_name = None
        self._product_specification = None
        self._quantity = None
        self._tax_amount = None
        self._tax_exclusive_amt = None
        self._tax_rate = None
        self._unit_price = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def duty_free_flag(self):
        return self._duty_free_flag

    @duty_free_flag.setter
    def duty_free_flag(self, value):
        self._duty_free_flag = value
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
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self._tax_amount = value
    @property
    def tax_exclusive_amt(self):
        return self._tax_exclusive_amt

    @tax_exclusive_amt.setter
    def tax_exclusive_amt(self, value):
        self._tax_exclusive_amt = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value
    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.duty_free_flag:
            if hasattr(self.duty_free_flag, 'to_alipay_dict'):
                params['duty_free_flag'] = self.duty_free_flag.to_alipay_dict()
            else:
                params['duty_free_flag'] = self.duty_free_flag
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
        if self.tax_amount:
            if hasattr(self.tax_amount, 'to_alipay_dict'):
                params['tax_amount'] = self.tax_amount.to_alipay_dict()
            else:
                params['tax_amount'] = self.tax_amount
        if self.tax_exclusive_amt:
            if hasattr(self.tax_exclusive_amt, 'to_alipay_dict'):
                params['tax_exclusive_amt'] = self.tax_exclusive_amt.to_alipay_dict()
            else:
                params['tax_exclusive_amt'] = self.tax_exclusive_amt
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        if self.unit_price:
            if hasattr(self.unit_price, 'to_alipay_dict'):
                params['unit_price'] = self.unit_price.to_alipay_dict()
            else:
                params['unit_price'] = self.unit_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InputInvoiceCheckLine()
        if 'amount' in d:
            o.amount = d['amount']
        if 'currency' in d:
            o.currency = d['currency']
        if 'duty_free_flag' in d:
            o.duty_free_flag = d['duty_free_flag']
        if 'measurement_unit' in d:
            o.measurement_unit = d['measurement_unit']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'product_specification' in d:
            o.product_specification = d['product_specification']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'tax_amount' in d:
            o.tax_amount = d['tax_amount']
        if 'tax_exclusive_amt' in d:
            o.tax_exclusive_amt = d['tax_exclusive_amt']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'unit_price' in d:
            o.unit_price = d['unit_price']
        return o


