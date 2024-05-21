#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppItemAllcategoryQueryModel(object):

    def __init__(self):
        self._cat_status = None
        self._item_type = None

    @property
    def cat_status(self):
        return self._cat_status

    @cat_status.setter
    def cat_status(self, value):
        self._cat_status = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.cat_status:
            if hasattr(self.cat_status, 'to_alipay_dict'):
                params['cat_status'] = self.cat_status.to_alipay_dict()
            else:
                params['cat_status'] = self.cat_status
        if self.item_type:
            if hasattr(self.item_type, 'to_alipay_dict'):
                params['item_type'] = self.item_type.to_alipay_dict()
            else:
                params['item_type'] = self.item_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppItemAllcategoryQueryModel()
        if 'cat_status' in d:
            o.cat_status = d['cat_status']
        if 'item_type' in d:
            o.item_type = d['item_type']
        return o


