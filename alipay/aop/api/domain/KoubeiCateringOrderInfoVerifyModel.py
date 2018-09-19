#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringOrderInfoVerifyModel(object):

    def __init__(self):
        self._shop_id = None
        self._verify_order_id = None

    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def verify_order_id(self):
        return self._verify_order_id

    @verify_order_id.setter
    def verify_order_id(self, value):
        self._verify_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.verify_order_id:
            if hasattr(self.verify_order_id, 'to_alipay_dict'):
                params['verify_order_id'] = self.verify_order_id.to_alipay_dict()
            else:
                params['verify_order_id'] = self.verify_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringOrderInfoVerifyModel()
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'verify_order_id' in d:
            o.verify_order_id = d['verify_order_id']
        return o


