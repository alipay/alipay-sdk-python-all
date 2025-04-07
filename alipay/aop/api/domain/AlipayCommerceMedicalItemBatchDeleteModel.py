#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalItemBatchDeleteModel(object):

    def __init__(self):
        self._item_code_list = None
        self._store_code = None

    @property
    def item_code_list(self):
        return self._item_code_list

    @item_code_list.setter
    def item_code_list(self, value):
        if isinstance(value, list):
            self._item_code_list = list()
            for i in value:
                self._item_code_list.append(i)
    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, value):
        self._store_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_code_list:
            if isinstance(self.item_code_list, list):
                for i in range(0, len(self.item_code_list)):
                    element = self.item_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_code_list[i] = element.to_alipay_dict()
            if hasattr(self.item_code_list, 'to_alipay_dict'):
                params['item_code_list'] = self.item_code_list.to_alipay_dict()
            else:
                params['item_code_list'] = self.item_code_list
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
        o = AlipayCommerceMedicalItemBatchDeleteModel()
        if 'item_code_list' in d:
            o.item_code_list = d['item_code_list']
        if 'store_code' in d:
            o.store_code = d['store_code']
        return o


