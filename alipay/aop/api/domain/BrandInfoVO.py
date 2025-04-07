#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BrandInfoVO(object):

    def __init__(self):
        self._item_brand_id = None
        self._item_brand_name = None

    @property
    def item_brand_id(self):
        return self._item_brand_id

    @item_brand_id.setter
    def item_brand_id(self, value):
        self._item_brand_id = value
    @property
    def item_brand_name(self):
        return self._item_brand_name

    @item_brand_name.setter
    def item_brand_name(self, value):
        self._item_brand_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_brand_id:
            if hasattr(self.item_brand_id, 'to_alipay_dict'):
                params['item_brand_id'] = self.item_brand_id.to_alipay_dict()
            else:
                params['item_brand_id'] = self.item_brand_id
        if self.item_brand_name:
            if hasattr(self.item_brand_name, 'to_alipay_dict'):
                params['item_brand_name'] = self.item_brand_name.to_alipay_dict()
            else:
                params['item_brand_name'] = self.item_brand_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BrandInfoVO()
        if 'item_brand_id' in d:
            o.item_brand_id = d['item_brand_id']
        if 'item_brand_name' in d:
            o.item_brand_name = d['item_brand_name']
        return o


