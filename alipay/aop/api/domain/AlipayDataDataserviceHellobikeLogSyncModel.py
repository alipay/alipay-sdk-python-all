#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceHellobikeLogSyncModel(object):

    def __init__(self):
        self._action_type = None
        self._channel = None
        self._city_code = None
        self._pay_price_cent = None
        self._pay_tool = None
        self._trace_id = None
        self._user_id = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def pay_price_cent(self):
        return self._pay_price_cent

    @pay_price_cent.setter
    def pay_price_cent(self, value):
        self._pay_price_cent = value
    @property
    def pay_tool(self):
        return self._pay_tool

    @pay_tool.setter
    def pay_tool(self, value):
        self._pay_tool = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.pay_price_cent:
            if hasattr(self.pay_price_cent, 'to_alipay_dict'):
                params['pay_price_cent'] = self.pay_price_cent.to_alipay_dict()
            else:
                params['pay_price_cent'] = self.pay_price_cent
        if self.pay_tool:
            if hasattr(self.pay_tool, 'to_alipay_dict'):
                params['pay_tool'] = self.pay_tool.to_alipay_dict()
            else:
                params['pay_tool'] = self.pay_tool
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceHellobikeLogSyncModel()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'channel' in d:
            o.channel = d['channel']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'pay_price_cent' in d:
            o.pay_price_cent = d['pay_price_cent']
        if 'pay_tool' in d:
            o.pay_tool = d['pay_tool']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


