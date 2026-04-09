#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLifeserviceItembookingBatchqueryModel(object):

    def __init__(self):
        self._item_code = None
        self._room_id = None
        self._service_id = None
        self._sku_code = None
        self._technician_id = None

    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, value):
        self._room_id = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def sku_code(self):
        return self._sku_code

    @sku_code.setter
    def sku_code(self, value):
        self._sku_code = value
    @property
    def technician_id(self):
        return self._technician_id

    @technician_id.setter
    def technician_id(self, value):
        self._technician_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.room_id:
            if hasattr(self.room_id, 'to_alipay_dict'):
                params['room_id'] = self.room_id.to_alipay_dict()
            else:
                params['room_id'] = self.room_id
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.sku_code:
            if hasattr(self.sku_code, 'to_alipay_dict'):
                params['sku_code'] = self.sku_code.to_alipay_dict()
            else:
                params['sku_code'] = self.sku_code
        if self.technician_id:
            if hasattr(self.technician_id, 'to_alipay_dict'):
                params['technician_id'] = self.technician_id.to_alipay_dict()
            else:
                params['technician_id'] = self.technician_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLifeserviceItembookingBatchqueryModel()
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'room_id' in d:
            o.room_id = d['room_id']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'sku_code' in d:
            o.sku_code = d['sku_code']
        if 'technician_id' in d:
            o.technician_id = d['technician_id']
        return o


