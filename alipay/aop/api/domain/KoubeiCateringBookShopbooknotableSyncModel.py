#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringBookShopbooknotableSyncModel(object):

    def __init__(self):
        self._out_shop_id = None
        self._refuse_time = None
        self._shop_id = None
        self._sync_timestamp = None

    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value
    @property
    def refuse_time(self):
        return self._refuse_time

    @refuse_time.setter
    def refuse_time(self, value):
        if isinstance(value, list):
            self._refuse_time = list()
            for i in value:
                self._refuse_time.append(i)
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def sync_timestamp(self):
        return self._sync_timestamp

    @sync_timestamp.setter
    def sync_timestamp(self, value):
        self._sync_timestamp = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_shop_id:
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = self.out_shop_id.to_alipay_dict()
            else:
                params['out_shop_id'] = self.out_shop_id
        if self.refuse_time:
            if isinstance(self.refuse_time, list):
                for i in range(0, len(self.refuse_time)):
                    element = self.refuse_time[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refuse_time[i] = element.to_alipay_dict()
            if hasattr(self.refuse_time, 'to_alipay_dict'):
                params['refuse_time'] = self.refuse_time.to_alipay_dict()
            else:
                params['refuse_time'] = self.refuse_time
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.sync_timestamp:
            if hasattr(self.sync_timestamp, 'to_alipay_dict'):
                params['sync_timestamp'] = self.sync_timestamp.to_alipay_dict()
            else:
                params['sync_timestamp'] = self.sync_timestamp
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringBookShopbooknotableSyncModel()
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        if 'refuse_time' in d:
            o.refuse_time = d['refuse_time']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sync_timestamp' in d:
            o.sync_timestamp = d['sync_timestamp']
        return o


