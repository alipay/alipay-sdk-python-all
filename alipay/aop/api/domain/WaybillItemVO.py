#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WaybillItemVO(object):

    def __init__(self):
        self._app_item_code = None
        self._item_name = None
        self._quantity_item = None

    @property
    def app_item_code(self):
        return self._app_item_code

    @app_item_code.setter
    def app_item_code(self, value):
        self._app_item_code = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def quantity_item(self):
        return self._quantity_item

    @quantity_item.setter
    def quantity_item(self, value):
        self._quantity_item = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_item_code:
            if hasattr(self.app_item_code, 'to_alipay_dict'):
                params['app_item_code'] = self.app_item_code.to_alipay_dict()
            else:
                params['app_item_code'] = self.app_item_code
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.quantity_item:
            if hasattr(self.quantity_item, 'to_alipay_dict'):
                params['quantity_item'] = self.quantity_item.to_alipay_dict()
            else:
                params['quantity_item'] = self.quantity_item
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WaybillItemVO()
        if 'app_item_code' in d:
            o.app_item_code = d['app_item_code']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'quantity_item' in d:
            o.quantity_item = d['quantity_item']
        return o


