#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PlanItem(object):

    def __init__(self):
        self._item_id = None
        self._item_name = None
        self._warehouse_id = None
        self._warehouse_name = None

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
    def warehouse_id(self):
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, value):
        self._warehouse_id = value
    @property
    def warehouse_name(self):
        return self._warehouse_name

    @warehouse_name.setter
    def warehouse_name(self, value):
        self._warehouse_name = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.warehouse_id:
            if hasattr(self.warehouse_id, 'to_alipay_dict'):
                params['warehouse_id'] = self.warehouse_id.to_alipay_dict()
            else:
                params['warehouse_id'] = self.warehouse_id
        if self.warehouse_name:
            if hasattr(self.warehouse_name, 'to_alipay_dict'):
                params['warehouse_name'] = self.warehouse_name.to_alipay_dict()
            else:
                params['warehouse_name'] = self.warehouse_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PlanItem()
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'warehouse_id' in d:
            o.warehouse_id = d['warehouse_id']
        if 'warehouse_name' in d:
            o.warehouse_name = d['warehouse_name']
        return o


