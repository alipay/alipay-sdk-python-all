#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemCodeUpdateByIdVO import ItemCodeUpdateByIdVO


class AlipayCommerceMedicalItemcodeByidModifyModel(object):

    def __init__(self):
        self._item_code_data = None
        self._store_code = None

    @property
    def item_code_data(self):
        return self._item_code_data

    @item_code_data.setter
    def item_code_data(self, value):
        if isinstance(value, list):
            self._item_code_data = list()
            for i in value:
                if isinstance(i, ItemCodeUpdateByIdVO):
                    self._item_code_data.append(i)
                else:
                    self._item_code_data.append(ItemCodeUpdateByIdVO.from_alipay_dict(i))
    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, value):
        self._store_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_code_data:
            if isinstance(self.item_code_data, list):
                for i in range(0, len(self.item_code_data)):
                    element = self.item_code_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_code_data[i] = element.to_alipay_dict()
            if hasattr(self.item_code_data, 'to_alipay_dict'):
                params['item_code_data'] = self.item_code_data.to_alipay_dict()
            else:
                params['item_code_data'] = self.item_code_data
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
        o = AlipayCommerceMedicalItemcodeByidModifyModel()
        if 'item_code_data' in d:
            o.item_code_data = d['item_code_data']
        if 'store_code' in d:
            o.store_code = d['store_code']
        return o


