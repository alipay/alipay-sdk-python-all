#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiRetailItemQueryModel(object):

    def __init__(self):
        self._city_id = None
        self._item_id = None

    @property
    def city_id(self):
        return self._city_id

    @city_id.setter
    def city_id(self, value):
        self._city_id = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_id:
            if hasattr(self.city_id, 'to_alipay_dict'):
                params['city_id'] = self.city_id.to_alipay_dict()
            else:
                params['city_id'] = self.city_id
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailItemQueryModel()
        if 'city_id' in d:
            o.city_id = d['city_id']
        if 'item_id' in d:
            o.item_id = d['item_id']
        return o


