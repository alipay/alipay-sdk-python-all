#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLifeserviceShopstockSyncModel(object):

    def __init__(self):
        self._shop_id = None
        self._status = None
        self._stock_date = None
        self._stock_end_time = None
        self._stock_start_time = None

    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def stock_date(self):
        return self._stock_date

    @stock_date.setter
    def stock_date(self, value):
        self._stock_date = value
    @property
    def stock_end_time(self):
        return self._stock_end_time

    @stock_end_time.setter
    def stock_end_time(self, value):
        self._stock_end_time = value
    @property
    def stock_start_time(self):
        return self._stock_start_time

    @stock_start_time.setter
    def stock_start_time(self, value):
        self._stock_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.stock_date:
            if hasattr(self.stock_date, 'to_alipay_dict'):
                params['stock_date'] = self.stock_date.to_alipay_dict()
            else:
                params['stock_date'] = self.stock_date
        if self.stock_end_time:
            if hasattr(self.stock_end_time, 'to_alipay_dict'):
                params['stock_end_time'] = self.stock_end_time.to_alipay_dict()
            else:
                params['stock_end_time'] = self.stock_end_time
        if self.stock_start_time:
            if hasattr(self.stock_start_time, 'to_alipay_dict'):
                params['stock_start_time'] = self.stock_start_time.to_alipay_dict()
            else:
                params['stock_start_time'] = self.stock_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLifeserviceShopstockSyncModel()
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'status' in d:
            o.status = d['status']
        if 'stock_date' in d:
            o.stock_date = d['stock_date']
        if 'stock_end_time' in d:
            o.stock_end_time = d['stock_end_time']
        if 'stock_start_time' in d:
            o.stock_start_time = d['stock_start_time']
        return o


