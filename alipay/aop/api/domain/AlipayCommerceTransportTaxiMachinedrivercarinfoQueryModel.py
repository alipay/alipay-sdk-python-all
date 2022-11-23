#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportTaxiMachinedrivercarinfoQueryModel(object):

    def __init__(self):
        self._driver_open_id = None
        self._driver_user_id = None
        self._request_id = None
        self._request_time = None

    @property
    def driver_open_id(self):
        return self._driver_open_id

    @driver_open_id.setter
    def driver_open_id(self, value):
        self._driver_open_id = value
    @property
    def driver_user_id(self):
        return self._driver_user_id

    @driver_user_id.setter
    def driver_user_id(self, value):
        self._driver_user_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def request_time(self):
        return self._request_time

    @request_time.setter
    def request_time(self, value):
        self._request_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.driver_open_id:
            if hasattr(self.driver_open_id, 'to_alipay_dict'):
                params['driver_open_id'] = self.driver_open_id.to_alipay_dict()
            else:
                params['driver_open_id'] = self.driver_open_id
        if self.driver_user_id:
            if hasattr(self.driver_user_id, 'to_alipay_dict'):
                params['driver_user_id'] = self.driver_user_id.to_alipay_dict()
            else:
                params['driver_user_id'] = self.driver_user_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.request_time:
            if hasattr(self.request_time, 'to_alipay_dict'):
                params['request_time'] = self.request_time.to_alipay_dict()
            else:
                params['request_time'] = self.request_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTaxiMachinedrivercarinfoQueryModel()
        if 'driver_open_id' in d:
            o.driver_open_id = d['driver_open_id']
        if 'driver_user_id' in d:
            o.driver_user_id = d['driver_user_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'request_time' in d:
            o.request_time = d['request_time']
        return o


