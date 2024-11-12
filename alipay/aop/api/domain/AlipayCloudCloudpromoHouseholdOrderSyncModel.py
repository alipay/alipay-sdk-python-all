#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoHouseholdOrderSyncModel(object):

    def __init__(self):
        self._alipay_order_id = None
        self._main_order_id = None
        self._order_amount = None
        self._order_id = None
        self._order_stat = None
        self._order_time = None
        self._order_title = None
        self._platform = None
        self._pre_amount = None

    @property
    def alipay_order_id(self):
        return self._alipay_order_id

    @alipay_order_id.setter
    def alipay_order_id(self, value):
        self._alipay_order_id = value
    @property
    def main_order_id(self):
        return self._main_order_id

    @main_order_id.setter
    def main_order_id(self, value):
        self._main_order_id = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_stat(self):
        return self._order_stat

    @order_stat.setter
    def order_stat(self, value):
        self._order_stat = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def order_title(self):
        return self._order_title

    @order_title.setter
    def order_title(self, value):
        self._order_title = value
    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):
        self._platform = value
    @property
    def pre_amount(self):
        return self._pre_amount

    @pre_amount.setter
    def pre_amount(self, value):
        self._pre_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_order_id:
            if hasattr(self.alipay_order_id, 'to_alipay_dict'):
                params['alipay_order_id'] = self.alipay_order_id.to_alipay_dict()
            else:
                params['alipay_order_id'] = self.alipay_order_id
        if self.main_order_id:
            if hasattr(self.main_order_id, 'to_alipay_dict'):
                params['main_order_id'] = self.main_order_id.to_alipay_dict()
            else:
                params['main_order_id'] = self.main_order_id
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_stat:
            if hasattr(self.order_stat, 'to_alipay_dict'):
                params['order_stat'] = self.order_stat.to_alipay_dict()
            else:
                params['order_stat'] = self.order_stat
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        if self.order_title:
            if hasattr(self.order_title, 'to_alipay_dict'):
                params['order_title'] = self.order_title.to_alipay_dict()
            else:
                params['order_title'] = self.order_title
        if self.platform:
            if hasattr(self.platform, 'to_alipay_dict'):
                params['platform'] = self.platform.to_alipay_dict()
            else:
                params['platform'] = self.platform
        if self.pre_amount:
            if hasattr(self.pre_amount, 'to_alipay_dict'):
                params['pre_amount'] = self.pre_amount.to_alipay_dict()
            else:
                params['pre_amount'] = self.pre_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoHouseholdOrderSyncModel()
        if 'alipay_order_id' in d:
            o.alipay_order_id = d['alipay_order_id']
        if 'main_order_id' in d:
            o.main_order_id = d['main_order_id']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_stat' in d:
            o.order_stat = d['order_stat']
        if 'order_time' in d:
            o.order_time = d['order_time']
        if 'order_title' in d:
            o.order_title = d['order_title']
        if 'platform' in d:
            o.platform = d['platform']
        if 'pre_amount' in d:
            o.pre_amount = d['pre_amount']
        return o


