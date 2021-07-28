#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Amount import Amount


class ShopExtendParams(object):

    def __init__(self):
        self._categories = None
        self._original_delivery_fee = None
        self._sales_volume = None
        self._sales_volume_period = None
        self._visibility = None

    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, value):
        if isinstance(value, list):
            self._categories = list()
            for i in value:
                self._categories.append(i)
    @property
    def original_delivery_fee(self):
        return self._original_delivery_fee

    @original_delivery_fee.setter
    def original_delivery_fee(self, value):
        if isinstance(value, Amount):
            self._original_delivery_fee = value
        else:
            self._original_delivery_fee = Amount.from_alipay_dict(value)
    @property
    def sales_volume(self):
        return self._sales_volume

    @sales_volume.setter
    def sales_volume(self, value):
        self._sales_volume = value
    @property
    def sales_volume_period(self):
        return self._sales_volume_period

    @sales_volume_period.setter
    def sales_volume_period(self, value):
        self._sales_volume_period = value
    @property
    def visibility(self):
        return self._visibility

    @visibility.setter
    def visibility(self, value):
        self._visibility = value


    def to_alipay_dict(self):
        params = dict()
        if self.categories:
            if isinstance(self.categories, list):
                for i in range(0, len(self.categories)):
                    element = self.categories[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.categories[i] = element.to_alipay_dict()
            if hasattr(self.categories, 'to_alipay_dict'):
                params['categories'] = self.categories.to_alipay_dict()
            else:
                params['categories'] = self.categories
        if self.original_delivery_fee:
            if hasattr(self.original_delivery_fee, 'to_alipay_dict'):
                params['original_delivery_fee'] = self.original_delivery_fee.to_alipay_dict()
            else:
                params['original_delivery_fee'] = self.original_delivery_fee
        if self.sales_volume:
            if hasattr(self.sales_volume, 'to_alipay_dict'):
                params['sales_volume'] = self.sales_volume.to_alipay_dict()
            else:
                params['sales_volume'] = self.sales_volume
        if self.sales_volume_period:
            if hasattr(self.sales_volume_period, 'to_alipay_dict'):
                params['sales_volume_period'] = self.sales_volume_period.to_alipay_dict()
            else:
                params['sales_volume_period'] = self.sales_volume_period
        if self.visibility:
            if hasattr(self.visibility, 'to_alipay_dict'):
                params['visibility'] = self.visibility.to_alipay_dict()
            else:
                params['visibility'] = self.visibility
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopExtendParams()
        if 'categories' in d:
            o.categories = d['categories']
        if 'original_delivery_fee' in d:
            o.original_delivery_fee = d['original_delivery_fee']
        if 'sales_volume' in d:
            o.sales_volume = d['sales_volume']
        if 'sales_volume_period' in d:
            o.sales_volume_period = d['sales_volume_period']
        if 'visibility' in d:
            o.visibility = d['visibility']
        return o


