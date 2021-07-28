#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportTaxiDriverlevelQueryModel(object):

    def __init__(self):
        self._channel = None
        self._driver_name = None
        self._driver_phone = None
        self._ext_info = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def driver_name(self):
        return self._driver_name

    @driver_name.setter
    def driver_name(self, value):
        self._driver_name = value
    @property
    def driver_phone(self):
        return self._driver_phone

    @driver_phone.setter
    def driver_phone(self, value):
        self._driver_phone = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.driver_name:
            if hasattr(self.driver_name, 'to_alipay_dict'):
                params['driver_name'] = self.driver_name.to_alipay_dict()
            else:
                params['driver_name'] = self.driver_name
        if self.driver_phone:
            if hasattr(self.driver_phone, 'to_alipay_dict'):
                params['driver_phone'] = self.driver_phone.to_alipay_dict()
            else:
                params['driver_phone'] = self.driver_phone
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTaxiDriverlevelQueryModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'driver_name' in d:
            o.driver_name = d['driver_name']
        if 'driver_phone' in d:
            o.driver_phone = d['driver_phone']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        return o


