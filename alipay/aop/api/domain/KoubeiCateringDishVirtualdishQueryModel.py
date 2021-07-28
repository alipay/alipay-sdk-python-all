#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringDishVirtualdishQueryModel(object):

    def __init__(self):
        self._catetory_id = None
        self._shop_id = None

    @property
    def catetory_id(self):
        return self._catetory_id

    @catetory_id.setter
    def catetory_id(self, value):
        self._catetory_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.catetory_id:
            if hasattr(self.catetory_id, 'to_alipay_dict'):
                params['catetory_id'] = self.catetory_id.to_alipay_dict()
            else:
                params['catetory_id'] = self.catetory_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringDishVirtualdishQueryModel()
        if 'catetory_id' in d:
            o.catetory_id = d['catetory_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


