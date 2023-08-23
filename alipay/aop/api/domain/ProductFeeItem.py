#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FeeItem import FeeItem


class ProductFeeItem(object):

    def __init__(self):
        self._fee_items = None
        self._product_name = None

    @property
    def fee_items(self):
        return self._fee_items

    @fee_items.setter
    def fee_items(self, value):
        if isinstance(value, list):
            self._fee_items = list()
            for i in value:
                if isinstance(i, FeeItem):
                    self._fee_items.append(i)
                else:
                    self._fee_items.append(FeeItem.from_alipay_dict(i))
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.fee_items:
            if isinstance(self.fee_items, list):
                for i in range(0, len(self.fee_items)):
                    element = self.fee_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fee_items[i] = element.to_alipay_dict()
            if hasattr(self.fee_items, 'to_alipay_dict'):
                params['fee_items'] = self.fee_items.to_alipay_dict()
            else:
                params['fee_items'] = self.fee_items
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductFeeItem()
        if 'fee_items' in d:
            o.fee_items = d['fee_items']
        if 'product_name' in d:
            o.product_name = d['product_name']
        return o


