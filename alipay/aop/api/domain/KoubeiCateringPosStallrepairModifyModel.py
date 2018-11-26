#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringPosStallrepairModifyModel(object):

    def __init__(self):
        self._dish_id = None
        self._shop_id = None
        self._stall_id = None

    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def stall_id(self):
        return self._stall_id

    @stall_id.setter
    def stall_id(self, value):
        self._stall_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.dish_id:
            if hasattr(self.dish_id, 'to_alipay_dict'):
                params['dish_id'] = self.dish_id.to_alipay_dict()
            else:
                params['dish_id'] = self.dish_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.stall_id:
            if hasattr(self.stall_id, 'to_alipay_dict'):
                params['stall_id'] = self.stall_id.to_alipay_dict()
            else:
                params['stall_id'] = self.stall_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringPosStallrepairModifyModel()
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'stall_id' in d:
            o.stall_id = d['stall_id']
        return o


