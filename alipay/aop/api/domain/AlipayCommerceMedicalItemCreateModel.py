#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemCreateInfoParam import ItemCreateInfoParam


class AlipayCommerceMedicalItemCreateModel(object):

    def __init__(self):
        self._item_list = None
        self._store_code = None

    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, ItemCreateInfoParam):
                    self._item_list.append(i)
                else:
                    self._item_list.append(ItemCreateInfoParam.from_alipay_dict(i))
    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, value):
        self._store_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_list:
            if isinstance(self.item_list, list):
                for i in range(0, len(self.item_list)):
                    element = self.item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_list[i] = element.to_alipay_dict()
            if hasattr(self.item_list, 'to_alipay_dict'):
                params['item_list'] = self.item_list.to_alipay_dict()
            else:
                params['item_list'] = self.item_list
        if self.store_code:
            if hasattr(self.store_code, 'to_alipay_dict'):
                params['store_code'] = self.store_code.to_alipay_dict()
            else:
                params['store_code'] = self.store_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalItemCreateModel()
        if 'item_list' in d:
            o.item_list = d['item_list']
        if 'store_code' in d:
            o.store_code = d['store_code']
        return o


