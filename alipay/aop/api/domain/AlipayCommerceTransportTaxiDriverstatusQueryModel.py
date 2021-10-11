#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportTaxiDriverstatusQueryModel(object):

    def __init__(self):
        self._request_time = None
        self._sys_driver_id = None

    @property
    def request_time(self):
        return self._request_time

    @request_time.setter
    def request_time(self, value):
        self._request_time = value
    @property
    def sys_driver_id(self):
        return self._sys_driver_id

    @sys_driver_id.setter
    def sys_driver_id(self, value):
        self._sys_driver_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.request_time:
            if hasattr(self.request_time, 'to_alipay_dict'):
                params['request_time'] = self.request_time.to_alipay_dict()
            else:
                params['request_time'] = self.request_time
        if self.sys_driver_id:
            if hasattr(self.sys_driver_id, 'to_alipay_dict'):
                params['sys_driver_id'] = self.sys_driver_id.to_alipay_dict()
            else:
                params['sys_driver_id'] = self.sys_driver_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTaxiDriverstatusQueryModel()
        if 'request_time' in d:
            o.request_time = d['request_time']
        if 'sys_driver_id' in d:
            o.sys_driver_id = d['sys_driver_id']
        return o


