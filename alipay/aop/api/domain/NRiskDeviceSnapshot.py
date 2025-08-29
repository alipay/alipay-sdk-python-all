#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NRiskDeviceSnapshotExtInfo import NRiskDeviceSnapshotExtInfo


class NRiskDeviceSnapshot(object):

    def __init__(self):
        self._customer_brand = None
        self._device_type = None
        self._ext_info = None
        self._last_trade_time = None
        self._last_turn_on_time = None
        self._poi_address = None
        self._poi_name = None
        self._sn = None

    @property
    def customer_brand(self):
        return self._customer_brand

    @customer_brand.setter
    def customer_brand(self, value):
        self._customer_brand = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, NRiskDeviceSnapshotExtInfo):
            self._ext_info = value
        else:
            self._ext_info = NRiskDeviceSnapshotExtInfo.from_alipay_dict(value)
    @property
    def last_trade_time(self):
        return self._last_trade_time

    @last_trade_time.setter
    def last_trade_time(self, value):
        self._last_trade_time = value
    @property
    def last_turn_on_time(self):
        return self._last_turn_on_time

    @last_turn_on_time.setter
    def last_turn_on_time(self, value):
        self._last_turn_on_time = value
    @property
    def poi_address(self):
        return self._poi_address

    @poi_address.setter
    def poi_address(self, value):
        self._poi_address = value
    @property
    def poi_name(self):
        return self._poi_name

    @poi_name.setter
    def poi_name(self, value):
        self._poi_name = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_brand:
            if hasattr(self.customer_brand, 'to_alipay_dict'):
                params['customer_brand'] = self.customer_brand.to_alipay_dict()
            else:
                params['customer_brand'] = self.customer_brand
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.last_trade_time:
            if hasattr(self.last_trade_time, 'to_alipay_dict'):
                params['last_trade_time'] = self.last_trade_time.to_alipay_dict()
            else:
                params['last_trade_time'] = self.last_trade_time
        if self.last_turn_on_time:
            if hasattr(self.last_turn_on_time, 'to_alipay_dict'):
                params['last_turn_on_time'] = self.last_turn_on_time.to_alipay_dict()
            else:
                params['last_turn_on_time'] = self.last_turn_on_time
        if self.poi_address:
            if hasattr(self.poi_address, 'to_alipay_dict'):
                params['poi_address'] = self.poi_address.to_alipay_dict()
            else:
                params['poi_address'] = self.poi_address
        if self.poi_name:
            if hasattr(self.poi_name, 'to_alipay_dict'):
                params['poi_name'] = self.poi_name.to_alipay_dict()
            else:
                params['poi_name'] = self.poi_name
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NRiskDeviceSnapshot()
        if 'customer_brand' in d:
            o.customer_brand = d['customer_brand']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'last_trade_time' in d:
            o.last_trade_time = d['last_trade_time']
        if 'last_turn_on_time' in d:
            o.last_turn_on_time = d['last_turn_on_time']
        if 'poi_address' in d:
            o.poi_address = d['poi_address']
        if 'poi_name' in d:
            o.poi_name = d['poi_name']
        if 'sn' in d:
            o.sn = d['sn']
        return o


