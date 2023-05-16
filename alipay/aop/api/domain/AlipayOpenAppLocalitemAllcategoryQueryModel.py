#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppLocalitemAllcategoryQueryModel(object):

    def __init__(self):
        self._item_type = None

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value


    def to_alipay_dict(self):
        params = dict()
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
        o = AlipayOpenAppLocalitemAllcategoryQueryModel()
        if 'item_type' in d:
            o.item_type = d['item_type']
        return o


