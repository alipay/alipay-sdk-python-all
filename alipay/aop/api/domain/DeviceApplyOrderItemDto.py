#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeviceApplyOrderItemDto(object):

    def __init__(self):
        self._apply_amount = None
        self._billed = None
        self._item_id = None
        self._item_name = None
        self._model_number = None
        self._selling_price = None
        self._sn_list = None
        self._supplier_id = None

    @property
    def apply_amount(self):
        return self._apply_amount

    @apply_amount.setter
    def apply_amount(self, value):
        self._apply_amount = value
    @property
    def billed(self):
        return self._billed

    @billed.setter
    def billed(self, value):
        self._billed = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def model_number(self):
        return self._model_number

    @model_number.setter
    def model_number(self, value):
        self._model_number = value
    @property
    def selling_price(self):
        return self._selling_price

    @selling_price.setter
    def selling_price(self, value):
        self._selling_price = value
    @property
    def sn_list(self):
        return self._sn_list

    @sn_list.setter
    def sn_list(self, value):
        if isinstance(value, list):
            self._sn_list = list()
            for i in value:
                self._sn_list.append(i)
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_amount:
            if hasattr(self.apply_amount, 'to_alipay_dict'):
                params['apply_amount'] = self.apply_amount.to_alipay_dict()
            else:
                params['apply_amount'] = self.apply_amount
        if self.billed:
            if hasattr(self.billed, 'to_alipay_dict'):
                params['billed'] = self.billed.to_alipay_dict()
            else:
                params['billed'] = self.billed
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.model_number:
            if hasattr(self.model_number, 'to_alipay_dict'):
                params['model_number'] = self.model_number.to_alipay_dict()
            else:
                params['model_number'] = self.model_number
        if self.selling_price:
            if hasattr(self.selling_price, 'to_alipay_dict'):
                params['selling_price'] = self.selling_price.to_alipay_dict()
            else:
                params['selling_price'] = self.selling_price
        if self.sn_list:
            if isinstance(self.sn_list, list):
                for i in range(0, len(self.sn_list)):
                    element = self.sn_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sn_list[i] = element.to_alipay_dict()
            if hasattr(self.sn_list, 'to_alipay_dict'):
                params['sn_list'] = self.sn_list.to_alipay_dict()
            else:
                params['sn_list'] = self.sn_list
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeviceApplyOrderItemDto()
        if 'apply_amount' in d:
            o.apply_amount = d['apply_amount']
        if 'billed' in d:
            o.billed = d['billed']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'model_number' in d:
            o.model_number = d['model_number']
        if 'selling_price' in d:
            o.selling_price = d['selling_price']
        if 'sn_list' in d:
            o.sn_list = d['sn_list']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        return o


