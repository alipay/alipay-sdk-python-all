#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringPosStallCreateModel(object):

    def __init__(self):
        self._dish_ids = None
        self._printer_id = None
        self._printer_type = None
        self._receipt_type = None
        self._shop_id = None
        self._stall_name = None

    @property
    def dish_ids(self):
        return self._dish_ids

    @dish_ids.setter
    def dish_ids(self, value):
        if isinstance(value, list):
            self._dish_ids = list()
            for i in value:
                self._dish_ids.append(i)
    @property
    def printer_id(self):
        return self._printer_id

    @printer_id.setter
    def printer_id(self, value):
        self._printer_id = value
    @property
    def printer_type(self):
        return self._printer_type

    @printer_type.setter
    def printer_type(self, value):
        self._printer_type = value
    @property
    def receipt_type(self):
        return self._receipt_type

    @receipt_type.setter
    def receipt_type(self, value):
        self._receipt_type = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def stall_name(self):
        return self._stall_name

    @stall_name.setter
    def stall_name(self, value):
        self._stall_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.dish_ids:
            if isinstance(self.dish_ids, list):
                for i in range(0, len(self.dish_ids)):
                    element = self.dish_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dish_ids[i] = element.to_alipay_dict()
            if hasattr(self.dish_ids, 'to_alipay_dict'):
                params['dish_ids'] = self.dish_ids.to_alipay_dict()
            else:
                params['dish_ids'] = self.dish_ids
        if self.printer_id:
            if hasattr(self.printer_id, 'to_alipay_dict'):
                params['printer_id'] = self.printer_id.to_alipay_dict()
            else:
                params['printer_id'] = self.printer_id
        if self.printer_type:
            if hasattr(self.printer_type, 'to_alipay_dict'):
                params['printer_type'] = self.printer_type.to_alipay_dict()
            else:
                params['printer_type'] = self.printer_type
        if self.receipt_type:
            if hasattr(self.receipt_type, 'to_alipay_dict'):
                params['receipt_type'] = self.receipt_type.to_alipay_dict()
            else:
                params['receipt_type'] = self.receipt_type
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.stall_name:
            if hasattr(self.stall_name, 'to_alipay_dict'):
                params['stall_name'] = self.stall_name.to_alipay_dict()
            else:
                params['stall_name'] = self.stall_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringPosStallCreateModel()
        if 'dish_ids' in d:
            o.dish_ids = d['dish_ids']
        if 'printer_id' in d:
            o.printer_id = d['printer_id']
        if 'printer_type' in d:
            o.printer_type = d['printer_type']
        if 'receipt_type' in d:
            o.receipt_type = d['receipt_type']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'stall_name' in d:
            o.stall_name = d['stall_name']
        return o


