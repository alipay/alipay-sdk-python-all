#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HomeNormalApiContent(object):

    def __init__(self):
        self._delivery_time = None
        self._detail_url = None
        self._is_scan = None
        self._merchant_address = None
        self._merchant_logo = None
        self._merchant_name = None
        self._merchant_pid = None
        self._order_url = None
        self._queue_code = None
        self._queue_num = None
        self._queue_way = None
        self._shop_id = None

    @property
    def delivery_time(self):
        return self._delivery_time

    @delivery_time.setter
    def delivery_time(self, value):
        self._delivery_time = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def is_scan(self):
        return self._is_scan

    @is_scan.setter
    def is_scan(self, value):
        self._is_scan = value
    @property
    def merchant_address(self):
        return self._merchant_address

    @merchant_address.setter
    def merchant_address(self, value):
        self._merchant_address = value
    @property
    def merchant_logo(self):
        return self._merchant_logo

    @merchant_logo.setter
    def merchant_logo(self, value):
        self._merchant_logo = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def order_url(self):
        return self._order_url

    @order_url.setter
    def order_url(self, value):
        self._order_url = value
    @property
    def queue_code(self):
        return self._queue_code

    @queue_code.setter
    def queue_code(self, value):
        self._queue_code = value
    @property
    def queue_num(self):
        return self._queue_num

    @queue_num.setter
    def queue_num(self, value):
        self._queue_num = value
    @property
    def queue_way(self):
        return self._queue_way

    @queue_way.setter
    def queue_way(self, value):
        self._queue_way = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_time:
            if hasattr(self.delivery_time, 'to_alipay_dict'):
                params['delivery_time'] = self.delivery_time.to_alipay_dict()
            else:
                params['delivery_time'] = self.delivery_time
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.is_scan:
            if hasattr(self.is_scan, 'to_alipay_dict'):
                params['is_scan'] = self.is_scan.to_alipay_dict()
            else:
                params['is_scan'] = self.is_scan
        if self.merchant_address:
            if hasattr(self.merchant_address, 'to_alipay_dict'):
                params['merchant_address'] = self.merchant_address.to_alipay_dict()
            else:
                params['merchant_address'] = self.merchant_address
        if self.merchant_logo:
            if hasattr(self.merchant_logo, 'to_alipay_dict'):
                params['merchant_logo'] = self.merchant_logo.to_alipay_dict()
            else:
                params['merchant_logo'] = self.merchant_logo
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.order_url:
            if hasattr(self.order_url, 'to_alipay_dict'):
                params['order_url'] = self.order_url.to_alipay_dict()
            else:
                params['order_url'] = self.order_url
        if self.queue_code:
            if hasattr(self.queue_code, 'to_alipay_dict'):
                params['queue_code'] = self.queue_code.to_alipay_dict()
            else:
                params['queue_code'] = self.queue_code
        if self.queue_num:
            if hasattr(self.queue_num, 'to_alipay_dict'):
                params['queue_num'] = self.queue_num.to_alipay_dict()
            else:
                params['queue_num'] = self.queue_num
        if self.queue_way:
            if hasattr(self.queue_way, 'to_alipay_dict'):
                params['queue_way'] = self.queue_way.to_alipay_dict()
            else:
                params['queue_way'] = self.queue_way
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
        o = HomeNormalApiContent()
        if 'delivery_time' in d:
            o.delivery_time = d['delivery_time']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'is_scan' in d:
            o.is_scan = d['is_scan']
        if 'merchant_address' in d:
            o.merchant_address = d['merchant_address']
        if 'merchant_logo' in d:
            o.merchant_logo = d['merchant_logo']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'order_url' in d:
            o.order_url = d['order_url']
        if 'queue_code' in d:
            o.queue_code = d['queue_code']
        if 'queue_num' in d:
            o.queue_num = d['queue_num']
        if 'queue_way' in d:
            o.queue_way = d['queue_way']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


