#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BsStore import BsStore


class AlipayCommerceUtcActivitySyncModel(object):

    def __init__(self):
        self._biz_id = None
        self._biz_time = None
        self._retailer_activity_id = None
        self._store_list = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def retailer_activity_id(self):
        return self._retailer_activity_id

    @retailer_activity_id.setter
    def retailer_activity_id(self, value):
        self._retailer_activity_id = value
    @property
    def store_list(self):
        return self._store_list

    @store_list.setter
    def store_list(self, value):
        if isinstance(value, list):
            self._store_list = list()
            for i in value:
                if isinstance(i, BsStore):
                    self._store_list.append(i)
                else:
                    self._store_list.append(BsStore.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.retailer_activity_id:
            if hasattr(self.retailer_activity_id, 'to_alipay_dict'):
                params['retailer_activity_id'] = self.retailer_activity_id.to_alipay_dict()
            else:
                params['retailer_activity_id'] = self.retailer_activity_id
        if self.store_list:
            if isinstance(self.store_list, list):
                for i in range(0, len(self.store_list)):
                    element = self.store_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.store_list[i] = element.to_alipay_dict()
            if hasattr(self.store_list, 'to_alipay_dict'):
                params['store_list'] = self.store_list.to_alipay_dict()
            else:
                params['store_list'] = self.store_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceUtcActivitySyncModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'retailer_activity_id' in d:
            o.retailer_activity_id = d['retailer_activity_id']
        if 'store_list' in d:
            o.store_list = d['store_list']
        return o


