#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenServicemarketOrderItemConfirmModel(object):

    def __init__(self):
        self._commodity_order_id = None
        self._mini_app_id = None
        self._shop_id = None

    @property
    def commodity_order_id(self):
        return self._commodity_order_id

    @commodity_order_id.setter
    def commodity_order_id(self, value):
        self._commodity_order_id = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.commodity_order_id:
            if hasattr(self.commodity_order_id, 'to_alipay_dict'):
                params['commodity_order_id'] = self.commodity_order_id.to_alipay_dict()
            else:
                params['commodity_order_id'] = self.commodity_order_id
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
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
        o = AlipayOpenServicemarketOrderItemConfirmModel()
        if 'commodity_order_id' in d:
            o.commodity_order_id = d['commodity_order_id']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


