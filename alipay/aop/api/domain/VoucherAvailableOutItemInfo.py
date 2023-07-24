#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherAvailableOutItemInfo(object):

    def __init__(self):
        self._item_app_id = None
        self._out_item_id = None

    @property
    def item_app_id(self):
        return self._item_app_id

    @item_app_id.setter
    def item_app_id(self, value):
        self._item_app_id = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_app_id:
            if hasattr(self.item_app_id, 'to_alipay_dict'):
                params['item_app_id'] = self.item_app_id.to_alipay_dict()
            else:
                params['item_app_id'] = self.item_app_id
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
        o = VoucherAvailableOutItemInfo()
        if 'item_app_id' in d:
            o.item_app_id = d['item_app_id']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        return o


