#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RequestExtShopItemQuery import RequestExtShopItemQuery


class KoubeiRetailShopitemBatchqueryModel(object):

    def __init__(self):
        self._shop_items = None

    @property
    def shop_items(self):
        return self._shop_items

    @shop_items.setter
    def shop_items(self, value):
        if isinstance(value, list):
            self._shop_items = list()
            for i in value:
                if isinstance(i, RequestExtShopItemQuery):
                    self._shop_items.append(i)
                else:
                    self._shop_items.append(RequestExtShopItemQuery.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.shop_items:
            if isinstance(self.shop_items, list):
                for i in range(0, len(self.shop_items)):
                    element = self.shop_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_items[i] = element.to_alipay_dict()
            if hasattr(self.shop_items, 'to_alipay_dict'):
                params['shop_items'] = self.shop_items.to_alipay_dict()
            else:
                params['shop_items'] = self.shop_items
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailShopitemBatchqueryModel()
        if 'shop_items' in d:
            o.shop_items = d['shop_items']
        return o


