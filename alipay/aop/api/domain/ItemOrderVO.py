#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemOrderVO(object):

    def __init__(self):
        self._ext_info = None
        self._item_order_no = None
        self._merchant_fund = None
        self._platform_fund = None
        self._price = None
        self._quantity = None
        self._sku_id = None
        self._status = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def item_order_no(self):
        return self._item_order_no

    @item_order_no.setter
    def item_order_no(self, value):
        self._item_order_no = value
    @property
    def merchant_fund(self):
        return self._merchant_fund

    @merchant_fund.setter
    def merchant_fund(self, value):
        self._merchant_fund = value
    @property
    def platform_fund(self):
        return self._platform_fund

    @platform_fund.setter
    def platform_fund(self, value):
        self._platform_fund = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.item_order_no:
            if hasattr(self.item_order_no, 'to_alipay_dict'):
                params['item_order_no'] = self.item_order_no.to_alipay_dict()
            else:
                params['item_order_no'] = self.item_order_no
        if self.merchant_fund:
            if hasattr(self.merchant_fund, 'to_alipay_dict'):
                params['merchant_fund'] = self.merchant_fund.to_alipay_dict()
            else:
                params['merchant_fund'] = self.merchant_fund
        if self.platform_fund:
            if hasattr(self.platform_fund, 'to_alipay_dict'):
                params['platform_fund'] = self.platform_fund.to_alipay_dict()
            else:
                params['platform_fund'] = self.platform_fund
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemOrderVO()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'item_order_no' in d:
            o.item_order_no = d['item_order_no']
        if 'merchant_fund' in d:
            o.merchant_fund = d['merchant_fund']
        if 'platform_fund' in d:
            o.platform_fund = d['platform_fund']
        if 'price' in d:
            o.price = d['price']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'status' in d:
            o.status = d['status']
        return o


