#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AttributeVO import AttributeVO
from alipay.aop.api.domain.AttributeVO import AttributeVO
from alipay.aop.api.domain.AttributeVO import AttributeVO
from alipay.aop.api.domain.AttributeVO import AttributeVO


class ItemAttrGroupVO(object):

    def __init__(self):
        self._item_attr_list = None
        self._product_attr_list = None
        self._sale_attr_list = None
        self._sku_attr_list = None

    @property
    def item_attr_list(self):
        return self._item_attr_list

    @item_attr_list.setter
    def item_attr_list(self, value):
        if isinstance(value, list):
            self._item_attr_list = list()
            for i in value:
                if isinstance(i, AttributeVO):
                    self._item_attr_list.append(i)
                else:
                    self._item_attr_list.append(AttributeVO.from_alipay_dict(i))
    @property
    def product_attr_list(self):
        return self._product_attr_list

    @product_attr_list.setter
    def product_attr_list(self, value):
        if isinstance(value, list):
            self._product_attr_list = list()
            for i in value:
                if isinstance(i, AttributeVO):
                    self._product_attr_list.append(i)
                else:
                    self._product_attr_list.append(AttributeVO.from_alipay_dict(i))
    @property
    def sale_attr_list(self):
        return self._sale_attr_list

    @sale_attr_list.setter
    def sale_attr_list(self, value):
        if isinstance(value, list):
            self._sale_attr_list = list()
            for i in value:
                if isinstance(i, AttributeVO):
                    self._sale_attr_list.append(i)
                else:
                    self._sale_attr_list.append(AttributeVO.from_alipay_dict(i))
    @property
    def sku_attr_list(self):
        return self._sku_attr_list

    @sku_attr_list.setter
    def sku_attr_list(self, value):
        if isinstance(value, list):
            self._sku_attr_list = list()
            for i in value:
                if isinstance(i, AttributeVO):
                    self._sku_attr_list.append(i)
                else:
                    self._sku_attr_list.append(AttributeVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.item_attr_list:
            if isinstance(self.item_attr_list, list):
                for i in range(0, len(self.item_attr_list)):
                    element = self.item_attr_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_attr_list[i] = element.to_alipay_dict()
            if hasattr(self.item_attr_list, 'to_alipay_dict'):
                params['item_attr_list'] = self.item_attr_list.to_alipay_dict()
            else:
                params['item_attr_list'] = self.item_attr_list
        if self.product_attr_list:
            if isinstance(self.product_attr_list, list):
                for i in range(0, len(self.product_attr_list)):
                    element = self.product_attr_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_attr_list[i] = element.to_alipay_dict()
            if hasattr(self.product_attr_list, 'to_alipay_dict'):
                params['product_attr_list'] = self.product_attr_list.to_alipay_dict()
            else:
                params['product_attr_list'] = self.product_attr_list
        if self.sale_attr_list:
            if isinstance(self.sale_attr_list, list):
                for i in range(0, len(self.sale_attr_list)):
                    element = self.sale_attr_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sale_attr_list[i] = element.to_alipay_dict()
            if hasattr(self.sale_attr_list, 'to_alipay_dict'):
                params['sale_attr_list'] = self.sale_attr_list.to_alipay_dict()
            else:
                params['sale_attr_list'] = self.sale_attr_list
        if self.sku_attr_list:
            if isinstance(self.sku_attr_list, list):
                for i in range(0, len(self.sku_attr_list)):
                    element = self.sku_attr_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sku_attr_list[i] = element.to_alipay_dict()
            if hasattr(self.sku_attr_list, 'to_alipay_dict'):
                params['sku_attr_list'] = self.sku_attr_list.to_alipay_dict()
            else:
                params['sku_attr_list'] = self.sku_attr_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemAttrGroupVO()
        if 'item_attr_list' in d:
            o.item_attr_list = d['item_attr_list']
        if 'product_attr_list' in d:
            o.product_attr_list = d['product_attr_list']
        if 'sale_attr_list' in d:
            o.sale_attr_list = d['sale_attr_list']
        if 'sku_attr_list' in d:
            o.sku_attr_list = d['sku_attr_list']
        return o


