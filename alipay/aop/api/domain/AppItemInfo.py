#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AppItemInfo(object):

    def __init__(self):
        self._item_id = None
        self._item_use_type = None
        self._mini_app_id = None
        self._out_item_id = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_use_type(self):
        return self._item_use_type

    @item_use_type.setter
    def item_use_type(self, value):
        self._item_use_type = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_use_type:
            if hasattr(self.item_use_type, 'to_alipay_dict'):
                params['item_use_type'] = self.item_use_type.to_alipay_dict()
            else:
                params['item_use_type'] = self.item_use_type
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppItemInfo()
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_use_type' in d:
            o.item_use_type = d['item_use_type']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        return o


