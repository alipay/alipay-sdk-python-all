#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTravelShopSyncresultQueryModel(object):

    def __init__(self):
        self._out_shop_id = None
        self._sync_order_id = None

    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value
    @property
    def sync_order_id(self):
        return self._sync_order_id

    @sync_order_id.setter
    def sync_order_id(self, value):
        self._sync_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_shop_id:
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = self.out_shop_id.to_alipay_dict()
            else:
                params['out_shop_id'] = self.out_shop_id
        if self.sync_order_id:
            if hasattr(self.sync_order_id, 'to_alipay_dict'):
                params['sync_order_id'] = self.sync_order_id.to_alipay_dict()
            else:
                params['sync_order_id'] = self.sync_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTravelShopSyncresultQueryModel()
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        if 'sync_order_id' in d:
            o.sync_order_id = d['sync_order_id']
        return o


