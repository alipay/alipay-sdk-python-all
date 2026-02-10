#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLifeserviceItembookingBindModel(object):

    def __init__(self):
        self._item_code = None
        self._room_ids = None
        self._service_ids = None
        self._sku_code = None
        self._technician_ids = None

    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def room_ids(self):
        return self._room_ids

    @room_ids.setter
    def room_ids(self, value):
        if isinstance(value, list):
            self._room_ids = list()
            for i in value:
                self._room_ids.append(i)
    @property
    def service_ids(self):
        return self._service_ids

    @service_ids.setter
    def service_ids(self, value):
        if isinstance(value, list):
            self._service_ids = list()
            for i in value:
                self._service_ids.append(i)
    @property
    def sku_code(self):
        return self._sku_code

    @sku_code.setter
    def sku_code(self, value):
        self._sku_code = value
    @property
    def technician_ids(self):
        return self._technician_ids

    @technician_ids.setter
    def technician_ids(self, value):
        if isinstance(value, list):
            self._technician_ids = list()
            for i in value:
                self._technician_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.room_ids:
            if isinstance(self.room_ids, list):
                for i in range(0, len(self.room_ids)):
                    element = self.room_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.room_ids[i] = element.to_alipay_dict()
            if hasattr(self.room_ids, 'to_alipay_dict'):
                params['room_ids'] = self.room_ids.to_alipay_dict()
            else:
                params['room_ids'] = self.room_ids
        if self.service_ids:
            if isinstance(self.service_ids, list):
                for i in range(0, len(self.service_ids)):
                    element = self.service_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_ids[i] = element.to_alipay_dict()
            if hasattr(self.service_ids, 'to_alipay_dict'):
                params['service_ids'] = self.service_ids.to_alipay_dict()
            else:
                params['service_ids'] = self.service_ids
        if self.sku_code:
            if hasattr(self.sku_code, 'to_alipay_dict'):
                params['sku_code'] = self.sku_code.to_alipay_dict()
            else:
                params['sku_code'] = self.sku_code
        if self.technician_ids:
            if isinstance(self.technician_ids, list):
                for i in range(0, len(self.technician_ids)):
                    element = self.technician_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.technician_ids[i] = element.to_alipay_dict()
            if hasattr(self.technician_ids, 'to_alipay_dict'):
                params['technician_ids'] = self.technician_ids.to_alipay_dict()
            else:
                params['technician_ids'] = self.technician_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLifeserviceItembookingBindModel()
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'room_ids' in d:
            o.room_ids = d['room_ids']
        if 'service_ids' in d:
            o.service_ids = d['service_ids']
        if 'sku_code' in d:
            o.sku_code = d['sku_code']
        if 'technician_ids' in d:
            o.technician_ids = d['technician_ids']
        return o


