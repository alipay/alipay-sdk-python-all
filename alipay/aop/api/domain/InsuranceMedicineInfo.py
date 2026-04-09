#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsuranceMedicineInfo(object):

    def __init__(self):
        self._medicine_amount = None
        self._medicine_name = None
        self._medicine_num = None
        self._medicine_price = None
        self._medicine_specification = None

    @property
    def medicine_amount(self):
        return self._medicine_amount

    @medicine_amount.setter
    def medicine_amount(self, value):
        self._medicine_amount = value
    @property
    def medicine_name(self):
        return self._medicine_name

    @medicine_name.setter
    def medicine_name(self, value):
        self._medicine_name = value
    @property
    def medicine_num(self):
        return self._medicine_num

    @medicine_num.setter
    def medicine_num(self, value):
        self._medicine_num = value
    @property
    def medicine_price(self):
        return self._medicine_price

    @medicine_price.setter
    def medicine_price(self, value):
        self._medicine_price = value
    @property
    def medicine_specification(self):
        return self._medicine_specification

    @medicine_specification.setter
    def medicine_specification(self, value):
        self._medicine_specification = value


    def to_alipay_dict(self):
        params = dict()
        if self.medicine_amount:
            if hasattr(self.medicine_amount, 'to_alipay_dict'):
                params['medicine_amount'] = self.medicine_amount.to_alipay_dict()
            else:
                params['medicine_amount'] = self.medicine_amount
        if self.medicine_name:
            if hasattr(self.medicine_name, 'to_alipay_dict'):
                params['medicine_name'] = self.medicine_name.to_alipay_dict()
            else:
                params['medicine_name'] = self.medicine_name
        if self.medicine_num:
            if hasattr(self.medicine_num, 'to_alipay_dict'):
                params['medicine_num'] = self.medicine_num.to_alipay_dict()
            else:
                params['medicine_num'] = self.medicine_num
        if self.medicine_price:
            if hasattr(self.medicine_price, 'to_alipay_dict'):
                params['medicine_price'] = self.medicine_price.to_alipay_dict()
            else:
                params['medicine_price'] = self.medicine_price
        if self.medicine_specification:
            if hasattr(self.medicine_specification, 'to_alipay_dict'):
                params['medicine_specification'] = self.medicine_specification.to_alipay_dict()
            else:
                params['medicine_specification'] = self.medicine_specification
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsuranceMedicineInfo()
        if 'medicine_amount' in d:
            o.medicine_amount = d['medicine_amount']
        if 'medicine_name' in d:
            o.medicine_name = d['medicine_name']
        if 'medicine_num' in d:
            o.medicine_num = d['medicine_num']
        if 'medicine_price' in d:
            o.medicine_price = d['medicine_price']
        if 'medicine_specification' in d:
            o.medicine_specification = d['medicine_specification']
        return o


