#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StallKdsEntity import StallKdsEntity


class StallEntity(object):

    def __init__(self):
        self._dish_ids = None
        self._id = None
        self._kds_list = None
        self._merchant_id = None
        self._printer_id = None
        self._printer_name = None
        self._printer_type = None
        self._receipt_type = None
        self._shop_id = None
        self._stall_name = None
        self._use = None

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
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def kds_list(self):
        return self._kds_list

    @kds_list.setter
    def kds_list(self, value):
        if isinstance(value, list):
            self._kds_list = list()
            for i in value:
                if isinstance(i, StallKdsEntity):
                    self._kds_list.append(i)
                else:
                    self._kds_list.append(StallKdsEntity.from_alipay_dict(i))
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def printer_id(self):
        return self._printer_id

    @printer_id.setter
    def printer_id(self, value):
        self._printer_id = value
    @property
    def printer_name(self):
        return self._printer_name

    @printer_name.setter
    def printer_name(self, value):
        self._printer_name = value
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
    @property
    def use(self):
        return self._use

    @use.setter
    def use(self, value):
        self._use = value


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
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.kds_list:
            if isinstance(self.kds_list, list):
                for i in range(0, len(self.kds_list)):
                    element = self.kds_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.kds_list[i] = element.to_alipay_dict()
            if hasattr(self.kds_list, 'to_alipay_dict'):
                params['kds_list'] = self.kds_list.to_alipay_dict()
            else:
                params['kds_list'] = self.kds_list
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.printer_id:
            if hasattr(self.printer_id, 'to_alipay_dict'):
                params['printer_id'] = self.printer_id.to_alipay_dict()
            else:
                params['printer_id'] = self.printer_id
        if self.printer_name:
            if hasattr(self.printer_name, 'to_alipay_dict'):
                params['printer_name'] = self.printer_name.to_alipay_dict()
            else:
                params['printer_name'] = self.printer_name
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
        if self.use:
            if hasattr(self.use, 'to_alipay_dict'):
                params['use'] = self.use.to_alipay_dict()
            else:
                params['use'] = self.use
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StallEntity()
        if 'dish_ids' in d:
            o.dish_ids = d['dish_ids']
        if 'id' in d:
            o.id = d['id']
        if 'kds_list' in d:
            o.kds_list = d['kds_list']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'printer_id' in d:
            o.printer_id = d['printer_id']
        if 'printer_name' in d:
            o.printer_name = d['printer_name']
        if 'printer_type' in d:
            o.printer_type = d['printer_type']
        if 'receipt_type' in d:
            o.receipt_type = d['receipt_type']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'stall_name' in d:
            o.stall_name = d['stall_name']
        if 'use' in d:
            o.use = d['use']
        return o


