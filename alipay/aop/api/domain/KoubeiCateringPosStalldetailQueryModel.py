#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringPosStalldetailQueryModel(object):

    def __init__(self):
        self._shop_id = None
        self._stall_id = None

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
        o = KoubeiCateringPosStalldetailQueryModel()
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'stall_id' in d:
            o.stall_id = d['stall_id']
        return o


