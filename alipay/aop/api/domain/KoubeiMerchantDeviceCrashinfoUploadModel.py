#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMerchantDeviceCrashinfoUploadModel(object):

    def __init__(self):
        self._event_time = None
        self._extend_info = None
        self._hardware_version = None
        self._log_time = None
        self._message_type = None
        self._product = None
        self._shop_id = None
        self._sn_id = None

    @property
    def event_time(self):
        return self._event_time

    @event_time.setter
    def event_time(self, value):
        self._event_time = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def hardware_version(self):
        return self._hardware_version

    @hardware_version.setter
    def hardware_version(self, value):
        self._hardware_version = value
    @property
    def log_time(self):
        return self._log_time

    @log_time.setter
    def log_time(self, value):
        self._log_time = value
    @property
    def message_type(self):
        return self._message_type

    @message_type.setter
    def message_type(self, value):
        self._message_type = value
    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def sn_id(self):
        return self._sn_id

    @sn_id.setter
    def sn_id(self, value):
        self._sn_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.event_time:
            if hasattr(self.event_time, 'to_alipay_dict'):
                params['event_time'] = self.event_time.to_alipay_dict()
            else:
                params['event_time'] = self.event_time
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.hardware_version:
            if hasattr(self.hardware_version, 'to_alipay_dict'):
                params['hardware_version'] = self.hardware_version.to_alipay_dict()
            else:
                params['hardware_version'] = self.hardware_version
        if self.log_time:
            if hasattr(self.log_time, 'to_alipay_dict'):
                params['log_time'] = self.log_time.to_alipay_dict()
            else:
                params['log_time'] = self.log_time
        if self.message_type:
            if hasattr(self.message_type, 'to_alipay_dict'):
                params['message_type'] = self.message_type.to_alipay_dict()
            else:
                params['message_type'] = self.message_type
        if self.product:
            if hasattr(self.product, 'to_alipay_dict'):
                params['product'] = self.product.to_alipay_dict()
            else:
                params['product'] = self.product
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.sn_id:
            if hasattr(self.sn_id, 'to_alipay_dict'):
                params['sn_id'] = self.sn_id.to_alipay_dict()
            else:
                params['sn_id'] = self.sn_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMerchantDeviceCrashinfoUploadModel()
        if 'event_time' in d:
            o.event_time = d['event_time']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'hardware_version' in d:
            o.hardware_version = d['hardware_version']
        if 'log_time' in d:
            o.log_time = d['log_time']
        if 'message_type' in d:
            o.message_type = d['message_type']
        if 'product' in d:
            o.product = d['product']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sn_id' in d:
            o.sn_id = d['sn_id']
        return o


