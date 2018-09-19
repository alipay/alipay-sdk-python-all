#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItermInfo(object):

    def __init__(self):
        self._error_message = None
        self._is_for_sale = None
        self._item_code = None
        self._mark_price = None
        self._success = None
        self._supplier_price = None

    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def is_for_sale(self):
        return self._is_for_sale

    @is_for_sale.setter
    def is_for_sale(self, value):
        self._is_for_sale = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def mark_price(self):
        return self._mark_price

    @mark_price.setter
    def mark_price(self, value):
        self._mark_price = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def supplier_price(self):
        return self._supplier_price

    @supplier_price.setter
    def supplier_price(self, value):
        self._supplier_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.error_message:
            if hasattr(self.error_message, 'to_alipay_dict'):
                params['error_message'] = self.error_message.to_alipay_dict()
            else:
                params['error_message'] = self.error_message
        if self.is_for_sale:
            if hasattr(self.is_for_sale, 'to_alipay_dict'):
                params['is_for_sale'] = self.is_for_sale.to_alipay_dict()
            else:
                params['is_for_sale'] = self.is_for_sale
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.mark_price:
            if hasattr(self.mark_price, 'to_alipay_dict'):
                params['mark_price'] = self.mark_price.to_alipay_dict()
            else:
                params['mark_price'] = self.mark_price
        if self.success:
            if hasattr(self.success, 'to_alipay_dict'):
                params['success'] = self.success.to_alipay_dict()
            else:
                params['success'] = self.success
        if self.supplier_price:
            if hasattr(self.supplier_price, 'to_alipay_dict'):
                params['supplier_price'] = self.supplier_price.to_alipay_dict()
            else:
                params['supplier_price'] = self.supplier_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItermInfo()
        if 'error_message' in d:
            o.error_message = d['error_message']
        if 'is_for_sale' in d:
            o.is_for_sale = d['is_for_sale']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'mark_price' in d:
            o.mark_price = d['mark_price']
        if 'success' in d:
            o.success = d['success']
        if 'supplier_price' in d:
            o.supplier_price = d['supplier_price']
        return o


