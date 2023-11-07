#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FeeItemPrice(object):

    def __init__(self):
        self._amount = None
        self._cloud_product_code = None
        self._cloud_product_name = None
        self._fee_item_code = None
        self._fee_item_name = None
        self._measuring_unit_code = None
        self._measuring_unit_name = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def cloud_product_code(self):
        return self._cloud_product_code

    @cloud_product_code.setter
    def cloud_product_code(self, value):
        self._cloud_product_code = value
    @property
    def cloud_product_name(self):
        return self._cloud_product_name

    @cloud_product_name.setter
    def cloud_product_name(self, value):
        self._cloud_product_name = value
    @property
    def fee_item_code(self):
        return self._fee_item_code

    @fee_item_code.setter
    def fee_item_code(self, value):
        self._fee_item_code = value
    @property
    def fee_item_name(self):
        return self._fee_item_name

    @fee_item_name.setter
    def fee_item_name(self, value):
        self._fee_item_name = value
    @property
    def measuring_unit_code(self):
        return self._measuring_unit_code

    @measuring_unit_code.setter
    def measuring_unit_code(self, value):
        self._measuring_unit_code = value
    @property
    def measuring_unit_name(self):
        return self._measuring_unit_name

    @measuring_unit_name.setter
    def measuring_unit_name(self, value):
        self._measuring_unit_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.cloud_product_code:
            if hasattr(self.cloud_product_code, 'to_alipay_dict'):
                params['cloud_product_code'] = self.cloud_product_code.to_alipay_dict()
            else:
                params['cloud_product_code'] = self.cloud_product_code
        if self.cloud_product_name:
            if hasattr(self.cloud_product_name, 'to_alipay_dict'):
                params['cloud_product_name'] = self.cloud_product_name.to_alipay_dict()
            else:
                params['cloud_product_name'] = self.cloud_product_name
        if self.fee_item_code:
            if hasattr(self.fee_item_code, 'to_alipay_dict'):
                params['fee_item_code'] = self.fee_item_code.to_alipay_dict()
            else:
                params['fee_item_code'] = self.fee_item_code
        if self.fee_item_name:
            if hasattr(self.fee_item_name, 'to_alipay_dict'):
                params['fee_item_name'] = self.fee_item_name.to_alipay_dict()
            else:
                params['fee_item_name'] = self.fee_item_name
        if self.measuring_unit_code:
            if hasattr(self.measuring_unit_code, 'to_alipay_dict'):
                params['measuring_unit_code'] = self.measuring_unit_code.to_alipay_dict()
            else:
                params['measuring_unit_code'] = self.measuring_unit_code
        if self.measuring_unit_name:
            if hasattr(self.measuring_unit_name, 'to_alipay_dict'):
                params['measuring_unit_name'] = self.measuring_unit_name.to_alipay_dict()
            else:
                params['measuring_unit_name'] = self.measuring_unit_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FeeItemPrice()
        if 'amount' in d:
            o.amount = d['amount']
        if 'cloud_product_code' in d:
            o.cloud_product_code = d['cloud_product_code']
        if 'cloud_product_name' in d:
            o.cloud_product_name = d['cloud_product_name']
        if 'fee_item_code' in d:
            o.fee_item_code = d['fee_item_code']
        if 'fee_item_name' in d:
            o.fee_item_name = d['fee_item_name']
        if 'measuring_unit_code' in d:
            o.measuring_unit_code = d['measuring_unit_code']
        if 'measuring_unit_name' in d:
            o.measuring_unit_name = d['measuring_unit_name']
        return o


