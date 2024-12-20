#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemModeCommissionInfo(object):

    def __init__(self):
        self._item_id = None
        self._item_rate = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_rate(self):
        return self._item_rate

    @item_rate.setter
    def item_rate(self, value):
        self._item_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_rate:
            if hasattr(self.item_rate, 'to_alipay_dict'):
                params['item_rate'] = self.item_rate.to_alipay_dict()
            else:
                params['item_rate'] = self.item_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemModeCommissionInfo()
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_rate' in d:
            o.item_rate = d['item_rate']
        return o


