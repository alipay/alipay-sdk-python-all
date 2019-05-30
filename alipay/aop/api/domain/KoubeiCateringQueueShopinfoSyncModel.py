#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringQueueShopinfoSyncModel(object):

    def __init__(self):
        self._discard_off = None
        self._discount_desc = None
        self._distance_limit = None
        self._notice = None
        self._out_shop_id = None
        self._shop_id = None
        self._show_order_wait_time = None
        self._show_wait_time = None
        self._sync_timestamp = None

    @property
    def discard_off(self):
        return self._discard_off

    @discard_off.setter
    def discard_off(self, value):
        self._discard_off = value
    @property
    def discount_desc(self):
        return self._discount_desc

    @discount_desc.setter
    def discount_desc(self, value):
        self._discount_desc = value
    @property
    def distance_limit(self):
        return self._distance_limit

    @distance_limit.setter
    def distance_limit(self, value):
        self._distance_limit = value
    @property
    def notice(self):
        return self._notice

    @notice.setter
    def notice(self, value):
        self._notice = value
    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def show_order_wait_time(self):
        return self._show_order_wait_time

    @show_order_wait_time.setter
    def show_order_wait_time(self, value):
        self._show_order_wait_time = value
    @property
    def show_wait_time(self):
        return self._show_wait_time

    @show_wait_time.setter
    def show_wait_time(self, value):
        self._show_wait_time = value
    @property
    def sync_timestamp(self):
        return self._sync_timestamp

    @sync_timestamp.setter
    def sync_timestamp(self, value):
        self._sync_timestamp = value


    def to_alipay_dict(self):
        params = dict()
        if self.discard_off:
            if hasattr(self.discard_off, 'to_alipay_dict'):
                params['discard_off'] = self.discard_off.to_alipay_dict()
            else:
                params['discard_off'] = self.discard_off
        if self.discount_desc:
            if hasattr(self.discount_desc, 'to_alipay_dict'):
                params['discount_desc'] = self.discount_desc.to_alipay_dict()
            else:
                params['discount_desc'] = self.discount_desc
        if self.distance_limit:
            if hasattr(self.distance_limit, 'to_alipay_dict'):
                params['distance_limit'] = self.distance_limit.to_alipay_dict()
            else:
                params['distance_limit'] = self.distance_limit
        if self.notice:
            if hasattr(self.notice, 'to_alipay_dict'):
                params['notice'] = self.notice.to_alipay_dict()
            else:
                params['notice'] = self.notice
        if self.out_shop_id:
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = self.out_shop_id.to_alipay_dict()
            else:
                params['out_shop_id'] = self.out_shop_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.show_order_wait_time:
            if hasattr(self.show_order_wait_time, 'to_alipay_dict'):
                params['show_order_wait_time'] = self.show_order_wait_time.to_alipay_dict()
            else:
                params['show_order_wait_time'] = self.show_order_wait_time
        if self.show_wait_time:
            if hasattr(self.show_wait_time, 'to_alipay_dict'):
                params['show_wait_time'] = self.show_wait_time.to_alipay_dict()
            else:
                params['show_wait_time'] = self.show_wait_time
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
        o = KoubeiCateringQueueShopinfoSyncModel()
        if 'discard_off' in d:
            o.discard_off = d['discard_off']
        if 'discount_desc' in d:
            o.discount_desc = d['discount_desc']
        if 'distance_limit' in d:
            o.distance_limit = d['distance_limit']
        if 'notice' in d:
            o.notice = d['notice']
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'show_order_wait_time' in d:
            o.show_order_wait_time = d['show_order_wait_time']
        if 'show_wait_time' in d:
            o.show_wait_time = d['show_wait_time']
        if 'sync_timestamp' in d:
            o.sync_timestamp = d['sync_timestamp']
        return o


