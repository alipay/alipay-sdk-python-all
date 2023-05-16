#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemDynamicQueryOrder(object):

    def __init__(self):
        self._catagory_id = None
        self._item_id = None
        self._item_type = None
        self._outer_item_id = None

    @property
    def catagory_id(self):
        return self._catagory_id

    @catagory_id.setter
    def catagory_id(self, value):
        self._catagory_id = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
    @property
    def outer_item_id(self):
        return self._outer_item_id

    @outer_item_id.setter
    def outer_item_id(self, value):
        self._outer_item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.catagory_id:
            if hasattr(self.catagory_id, 'to_alipay_dict'):
                params['catagory_id'] = self.catagory_id.to_alipay_dict()
            else:
                params['catagory_id'] = self.catagory_id
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_type:
            if hasattr(self.item_type, 'to_alipay_dict'):
                params['item_type'] = self.item_type.to_alipay_dict()
            else:
                params['item_type'] = self.item_type
        if self.outer_item_id:
            if hasattr(self.outer_item_id, 'to_alipay_dict'):
                params['outer_item_id'] = self.outer_item_id.to_alipay_dict()
            else:
                params['outer_item_id'] = self.outer_item_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemDynamicQueryOrder()
        if 'catagory_id' in d:
            o.catagory_id = d['catagory_id']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_type' in d:
            o.item_type = d['item_type']
        if 'outer_item_id' in d:
            o.outer_item_id = d['outer_item_id']
        return o


