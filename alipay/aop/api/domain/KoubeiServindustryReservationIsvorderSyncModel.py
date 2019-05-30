#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiServindustryReservationIsvorderSyncModel(object):

    def __init__(self):
        self._arrive_time = None
        self._memo = None
        self._order_id = None
        self._shop_id = None

    @property
    def arrive_time(self):
        return self._arrive_time

    @arrive_time.setter
    def arrive_time(self, value):
        self._arrive_time = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.arrive_time:
            if hasattr(self.arrive_time, 'to_alipay_dict'):
                params['arrive_time'] = self.arrive_time.to_alipay_dict()
            else:
                params['arrive_time'] = self.arrive_time
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
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
        o = KoubeiServindustryReservationIsvorderSyncModel()
        if 'arrive_time' in d:
            o.arrive_time = d['arrive_time']
        if 'memo' in d:
            o.memo = d['memo']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


