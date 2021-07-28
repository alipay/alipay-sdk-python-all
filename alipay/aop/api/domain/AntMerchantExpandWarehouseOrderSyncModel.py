#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandWarehouseOrderSyncModel(object):

    def __init__(self):
        self._assign_item_id = None
        self._new_warehouse_id = None
        self._type = None

    @property
    def assign_item_id(self):
        return self._assign_item_id

    @assign_item_id.setter
    def assign_item_id(self, value):
        self._assign_item_id = value
    @property
    def new_warehouse_id(self):
        return self._new_warehouse_id

    @new_warehouse_id.setter
    def new_warehouse_id(self, value):
        self._new_warehouse_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.assign_item_id:
            if hasattr(self.assign_item_id, 'to_alipay_dict'):
                params['assign_item_id'] = self.assign_item_id.to_alipay_dict()
            else:
                params['assign_item_id'] = self.assign_item_id
        if self.new_warehouse_id:
            if hasattr(self.new_warehouse_id, 'to_alipay_dict'):
                params['new_warehouse_id'] = self.new_warehouse_id.to_alipay_dict()
            else:
                params['new_warehouse_id'] = self.new_warehouse_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandWarehouseOrderSyncModel()
        if 'assign_item_id' in d:
            o.assign_item_id = d['assign_item_id']
        if 'new_warehouse_id' in d:
            o.new_warehouse_id = d['new_warehouse_id']
        if 'type' in d:
            o.type = d['type']
        return o


