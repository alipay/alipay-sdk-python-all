#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ProductFeeItem import ProductFeeItem


class ResourcePackageInfo(object):

    def __init__(self):
        self._can_alter = None
        self._error_msg = None
        self._original_unit_amount = None
        self._product_fee_items = None
        self._spec_code = None
        self._spec_desc = None
        self._spec_name = None
        self._trade_unit_amount = None

    @property
    def can_alter(self):
        return self._can_alter

    @can_alter.setter
    def can_alter(self, value):
        self._can_alter = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def original_unit_amount(self):
        return self._original_unit_amount

    @original_unit_amount.setter
    def original_unit_amount(self, value):
        self._original_unit_amount = value
    @property
    def product_fee_items(self):
        return self._product_fee_items

    @product_fee_items.setter
    def product_fee_items(self, value):
        if isinstance(value, list):
            self._product_fee_items = list()
            for i in value:
                if isinstance(i, ProductFeeItem):
                    self._product_fee_items.append(i)
                else:
                    self._product_fee_items.append(ProductFeeItem.from_alipay_dict(i))
    @property
    def spec_code(self):
        return self._spec_code

    @spec_code.setter
    def spec_code(self, value):
        self._spec_code = value
    @property
    def spec_desc(self):
        return self._spec_desc

    @spec_desc.setter
    def spec_desc(self, value):
        self._spec_desc = value
    @property
    def spec_name(self):
        return self._spec_name

    @spec_name.setter
    def spec_name(self, value):
        self._spec_name = value
    @property
    def trade_unit_amount(self):
        return self._trade_unit_amount

    @trade_unit_amount.setter
    def trade_unit_amount(self, value):
        self._trade_unit_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.can_alter:
            if hasattr(self.can_alter, 'to_alipay_dict'):
                params['can_alter'] = self.can_alter.to_alipay_dict()
            else:
                params['can_alter'] = self.can_alter
        if self.error_msg:
            if hasattr(self.error_msg, 'to_alipay_dict'):
                params['error_msg'] = self.error_msg.to_alipay_dict()
            else:
                params['error_msg'] = self.error_msg
        if self.original_unit_amount:
            if hasattr(self.original_unit_amount, 'to_alipay_dict'):
                params['original_unit_amount'] = self.original_unit_amount.to_alipay_dict()
            else:
                params['original_unit_amount'] = self.original_unit_amount
        if self.product_fee_items:
            if isinstance(self.product_fee_items, list):
                for i in range(0, len(self.product_fee_items)):
                    element = self.product_fee_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_fee_items[i] = element.to_alipay_dict()
            if hasattr(self.product_fee_items, 'to_alipay_dict'):
                params['product_fee_items'] = self.product_fee_items.to_alipay_dict()
            else:
                params['product_fee_items'] = self.product_fee_items
        if self.spec_code:
            if hasattr(self.spec_code, 'to_alipay_dict'):
                params['spec_code'] = self.spec_code.to_alipay_dict()
            else:
                params['spec_code'] = self.spec_code
        if self.spec_desc:
            if hasattr(self.spec_desc, 'to_alipay_dict'):
                params['spec_desc'] = self.spec_desc.to_alipay_dict()
            else:
                params['spec_desc'] = self.spec_desc
        if self.spec_name:
            if hasattr(self.spec_name, 'to_alipay_dict'):
                params['spec_name'] = self.spec_name.to_alipay_dict()
            else:
                params['spec_name'] = self.spec_name
        if self.trade_unit_amount:
            if hasattr(self.trade_unit_amount, 'to_alipay_dict'):
                params['trade_unit_amount'] = self.trade_unit_amount.to_alipay_dict()
            else:
                params['trade_unit_amount'] = self.trade_unit_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ResourcePackageInfo()
        if 'can_alter' in d:
            o.can_alter = d['can_alter']
        if 'error_msg' in d:
            o.error_msg = d['error_msg']
        if 'original_unit_amount' in d:
            o.original_unit_amount = d['original_unit_amount']
        if 'product_fee_items' in d:
            o.product_fee_items = d['product_fee_items']
        if 'spec_code' in d:
            o.spec_code = d['spec_code']
        if 'spec_desc' in d:
            o.spec_desc = d['spec_desc']
        if 'spec_name' in d:
            o.spec_name = d['spec_name']
        if 'trade_unit_amount' in d:
            o.trade_unit_amount = d['trade_unit_amount']
        return o


