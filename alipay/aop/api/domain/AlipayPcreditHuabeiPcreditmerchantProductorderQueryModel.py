#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ProductOrderQueryItem import ProductOrderQueryItem


class AlipayPcreditHuabeiPcreditmerchantProductorderQueryModel(object):

    def __init__(self):
        self._biz_from = None
        self._from_app = None
        self._pid = None
        self._product_order_query_items = None

    @property
    def biz_from(self):
        return self._biz_from

    @biz_from.setter
    def biz_from(self, value):
        self._biz_from = value
    @property
    def from_app(self):
        return self._from_app

    @from_app.setter
    def from_app(self, value):
        self._from_app = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def product_order_query_items(self):
        return self._product_order_query_items

    @product_order_query_items.setter
    def product_order_query_items(self, value):
        if isinstance(value, list):
            self._product_order_query_items = list()
            for i in value:
                if isinstance(i, ProductOrderQueryItem):
                    self._product_order_query_items.append(i)
                else:
                    self._product_order_query_items.append(ProductOrderQueryItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.biz_from:
            if hasattr(self.biz_from, 'to_alipay_dict'):
                params['biz_from'] = self.biz_from.to_alipay_dict()
            else:
                params['biz_from'] = self.biz_from
        if self.from_app:
            if hasattr(self.from_app, 'to_alipay_dict'):
                params['from_app'] = self.from_app.to_alipay_dict()
            else:
                params['from_app'] = self.from_app
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.product_order_query_items:
            if isinstance(self.product_order_query_items, list):
                for i in range(0, len(self.product_order_query_items)):
                    element = self.product_order_query_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_order_query_items[i] = element.to_alipay_dict()
            if hasattr(self.product_order_query_items, 'to_alipay_dict'):
                params['product_order_query_items'] = self.product_order_query_items.to_alipay_dict()
            else:
                params['product_order_query_items'] = self.product_order_query_items
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiPcreditmerchantProductorderQueryModel()
        if 'biz_from' in d:
            o.biz_from = d['biz_from']
        if 'from_app' in d:
            o.from_app = d['from_app']
        if 'pid' in d:
            o.pid = d['pid']
        if 'product_order_query_items' in d:
            o.product_order_query_items = d['product_order_query_items']
        return o


