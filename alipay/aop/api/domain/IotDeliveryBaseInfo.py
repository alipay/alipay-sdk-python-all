#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IotDeliveryBaseInfo(object):

    def __init__(self):
        self._delivery_begin_time = None
        self._delivery_end_time = None
        self._delivery_name = None
        self._device_file_id = None
        self._device_file_url = None
        self._exclude_shop_ids = None
        self._include_shop_ids = None
        self._trade_down_threshold = None
        self._trade_upon_threshold = None

    @property
    def delivery_begin_time(self):
        return self._delivery_begin_time

    @delivery_begin_time.setter
    def delivery_begin_time(self, value):
        self._delivery_begin_time = value
    @property
    def delivery_end_time(self):
        return self._delivery_end_time

    @delivery_end_time.setter
    def delivery_end_time(self, value):
        self._delivery_end_time = value
    @property
    def delivery_name(self):
        return self._delivery_name

    @delivery_name.setter
    def delivery_name(self, value):
        self._delivery_name = value
    @property
    def device_file_id(self):
        return self._device_file_id

    @device_file_id.setter
    def device_file_id(self, value):
        self._device_file_id = value
    @property
    def device_file_url(self):
        return self._device_file_url

    @device_file_url.setter
    def device_file_url(self, value):
        self._device_file_url = value
    @property
    def exclude_shop_ids(self):
        return self._exclude_shop_ids

    @exclude_shop_ids.setter
    def exclude_shop_ids(self, value):
        self._exclude_shop_ids = value
    @property
    def include_shop_ids(self):
        return self._include_shop_ids

    @include_shop_ids.setter
    def include_shop_ids(self, value):
        self._include_shop_ids = value
    @property
    def trade_down_threshold(self):
        return self._trade_down_threshold

    @trade_down_threshold.setter
    def trade_down_threshold(self, value):
        self._trade_down_threshold = value
    @property
    def trade_upon_threshold(self):
        return self._trade_upon_threshold

    @trade_upon_threshold.setter
    def trade_upon_threshold(self, value):
        self._trade_upon_threshold = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_begin_time:
            if hasattr(self.delivery_begin_time, 'to_alipay_dict'):
                params['delivery_begin_time'] = self.delivery_begin_time.to_alipay_dict()
            else:
                params['delivery_begin_time'] = self.delivery_begin_time
        if self.delivery_end_time:
            if hasattr(self.delivery_end_time, 'to_alipay_dict'):
                params['delivery_end_time'] = self.delivery_end_time.to_alipay_dict()
            else:
                params['delivery_end_time'] = self.delivery_end_time
        if self.delivery_name:
            if hasattr(self.delivery_name, 'to_alipay_dict'):
                params['delivery_name'] = self.delivery_name.to_alipay_dict()
            else:
                params['delivery_name'] = self.delivery_name
        if self.device_file_id:
            if hasattr(self.device_file_id, 'to_alipay_dict'):
                params['device_file_id'] = self.device_file_id.to_alipay_dict()
            else:
                params['device_file_id'] = self.device_file_id
        if self.device_file_url:
            if hasattr(self.device_file_url, 'to_alipay_dict'):
                params['device_file_url'] = self.device_file_url.to_alipay_dict()
            else:
                params['device_file_url'] = self.device_file_url
        if self.exclude_shop_ids:
            if hasattr(self.exclude_shop_ids, 'to_alipay_dict'):
                params['exclude_shop_ids'] = self.exclude_shop_ids.to_alipay_dict()
            else:
                params['exclude_shop_ids'] = self.exclude_shop_ids
        if self.include_shop_ids:
            if hasattr(self.include_shop_ids, 'to_alipay_dict'):
                params['include_shop_ids'] = self.include_shop_ids.to_alipay_dict()
            else:
                params['include_shop_ids'] = self.include_shop_ids
        if self.trade_down_threshold:
            if hasattr(self.trade_down_threshold, 'to_alipay_dict'):
                params['trade_down_threshold'] = self.trade_down_threshold.to_alipay_dict()
            else:
                params['trade_down_threshold'] = self.trade_down_threshold
        if self.trade_upon_threshold:
            if hasattr(self.trade_upon_threshold, 'to_alipay_dict'):
                params['trade_upon_threshold'] = self.trade_upon_threshold.to_alipay_dict()
            else:
                params['trade_upon_threshold'] = self.trade_upon_threshold
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IotDeliveryBaseInfo()
        if 'delivery_begin_time' in d:
            o.delivery_begin_time = d['delivery_begin_time']
        if 'delivery_end_time' in d:
            o.delivery_end_time = d['delivery_end_time']
        if 'delivery_name' in d:
            o.delivery_name = d['delivery_name']
        if 'device_file_id' in d:
            o.device_file_id = d['device_file_id']
        if 'device_file_url' in d:
            o.device_file_url = d['device_file_url']
        if 'exclude_shop_ids' in d:
            o.exclude_shop_ids = d['exclude_shop_ids']
        if 'include_shop_ids' in d:
            o.include_shop_ids = d['include_shop_ids']
        if 'trade_down_threshold' in d:
            o.trade_down_threshold = d['trade_down_threshold']
        if 'trade_upon_threshold' in d:
            o.trade_upon_threshold = d['trade_upon_threshold']
        return o


