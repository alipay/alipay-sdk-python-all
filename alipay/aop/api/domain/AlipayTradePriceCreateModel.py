#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CustomUnitAmount import CustomUnitAmount
from alipay.aop.api.domain.ProductData import ProductData
from alipay.aop.api.domain.RecurringConfig import RecurringConfig


class AlipayTradePriceCreateModel(object):

    def __init__(self):
        self._custom_unit_amount = None
        self._eligibility_expire_time = None
        self._eligibility_type = None
        self._metadata = None
        self._product_data = None
        self._product_id = None
        self._recurring = None
        self._unit_amount = None

    @property
    def custom_unit_amount(self):
        return self._custom_unit_amount

    @custom_unit_amount.setter
    def custom_unit_amount(self, value):
        if isinstance(value, CustomUnitAmount):
            self._custom_unit_amount = value
        else:
            self._custom_unit_amount = CustomUnitAmount.from_alipay_dict(value)
    @property
    def eligibility_expire_time(self):
        return self._eligibility_expire_time

    @eligibility_expire_time.setter
    def eligibility_expire_time(self, value):
        self._eligibility_expire_time = value
    @property
    def eligibility_type(self):
        return self._eligibility_type

    @eligibility_type.setter
    def eligibility_type(self, value):
        self._eligibility_type = value
    @property
    def metadata(self):
        return self._metadata

    @metadata.setter
    def metadata(self, value):
        self._metadata = value
    @property
    def product_data(self):
        return self._product_data

    @product_data.setter
    def product_data(self, value):
        if isinstance(value, ProductData):
            self._product_data = value
        else:
            self._product_data = ProductData.from_alipay_dict(value)
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def recurring(self):
        return self._recurring

    @recurring.setter
    def recurring(self, value):
        if isinstance(value, RecurringConfig):
            self._recurring = value
        else:
            self._recurring = RecurringConfig.from_alipay_dict(value)
    @property
    def unit_amount(self):
        return self._unit_amount

    @unit_amount.setter
    def unit_amount(self, value):
        self._unit_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.custom_unit_amount:
            if hasattr(self.custom_unit_amount, 'to_alipay_dict'):
                params['custom_unit_amount'] = self.custom_unit_amount.to_alipay_dict()
            else:
                params['custom_unit_amount'] = self.custom_unit_amount
        if self.eligibility_expire_time:
            if hasattr(self.eligibility_expire_time, 'to_alipay_dict'):
                params['eligibility_expire_time'] = self.eligibility_expire_time.to_alipay_dict()
            else:
                params['eligibility_expire_time'] = self.eligibility_expire_time
        if self.eligibility_type:
            if hasattr(self.eligibility_type, 'to_alipay_dict'):
                params['eligibility_type'] = self.eligibility_type.to_alipay_dict()
            else:
                params['eligibility_type'] = self.eligibility_type
        if self.metadata:
            if hasattr(self.metadata, 'to_alipay_dict'):
                params['metadata'] = self.metadata.to_alipay_dict()
            else:
                params['metadata'] = self.metadata
        if self.product_data:
            if hasattr(self.product_data, 'to_alipay_dict'):
                params['product_data'] = self.product_data.to_alipay_dict()
            else:
                params['product_data'] = self.product_data
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.recurring:
            if hasattr(self.recurring, 'to_alipay_dict'):
                params['recurring'] = self.recurring.to_alipay_dict()
            else:
                params['recurring'] = self.recurring
        if self.unit_amount:
            if hasattr(self.unit_amount, 'to_alipay_dict'):
                params['unit_amount'] = self.unit_amount.to_alipay_dict()
            else:
                params['unit_amount'] = self.unit_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradePriceCreateModel()
        if 'custom_unit_amount' in d:
            o.custom_unit_amount = d['custom_unit_amount']
        if 'eligibility_expire_time' in d:
            o.eligibility_expire_time = d['eligibility_expire_time']
        if 'eligibility_type' in d:
            o.eligibility_type = d['eligibility_type']
        if 'metadata' in d:
            o.metadata = d['metadata']
        if 'product_data' in d:
            o.product_data = d['product_data']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'recurring' in d:
            o.recurring = d['recurring']
        if 'unit_amount' in d:
            o.unit_amount = d['unit_amount']
        return o


