#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShopQueue import ShopQueue


class KoubeiCateringQueueShopqueueinfoSyncModel(object):

    def __init__(self):
        self._out_shop_id = None
        self._queue_list = None
        self._shop_id = None
        self._sync_timestamp = None

    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value
    @property
    def queue_list(self):
        return self._queue_list

    @queue_list.setter
    def queue_list(self, value):
        if isinstance(value, list):
            self._queue_list = list()
            for i in value:
                if isinstance(i, ShopQueue):
                    self._queue_list.append(i)
                else:
                    self._queue_list.append(ShopQueue.from_alipay_dict(i))
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
        if self.queue_list:
            if isinstance(self.queue_list, list):
                for i in range(0, len(self.queue_list)):
                    element = self.queue_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.queue_list[i] = element.to_alipay_dict()
            if hasattr(self.queue_list, 'to_alipay_dict'):
                params['queue_list'] = self.queue_list.to_alipay_dict()
            else:
                params['queue_list'] = self.queue_list
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
        o = KoubeiCateringQueueShopqueueinfoSyncModel()
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        if 'queue_list' in d:
            o.queue_list = d['queue_list']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sync_timestamp' in d:
            o.sync_timestamp = d['sync_timestamp']
        return o


