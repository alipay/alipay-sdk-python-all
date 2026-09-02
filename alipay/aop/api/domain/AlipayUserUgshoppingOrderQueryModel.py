#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserUgshoppingOrderQueryModel(object):

    def __init__(self):
        self._channel = None
        self._max_order_create_time = None
        self._min_order_create_time = None
        self._open_id = None
        self._user_id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def max_order_create_time(self):
        return self._max_order_create_time

    @max_order_create_time.setter
    def max_order_create_time(self, value):
        self._max_order_create_time = value
    @property
    def min_order_create_time(self):
        return self._min_order_create_time

    @min_order_create_time.setter
    def min_order_create_time(self, value):
        self._min_order_create_time = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.max_order_create_time:
            if hasattr(self.max_order_create_time, 'to_alipay_dict'):
                params['max_order_create_time'] = self.max_order_create_time.to_alipay_dict()
            else:
                params['max_order_create_time'] = self.max_order_create_time
        if self.min_order_create_time:
            if hasattr(self.min_order_create_time, 'to_alipay_dict'):
                params['min_order_create_time'] = self.min_order_create_time.to_alipay_dict()
            else:
                params['min_order_create_time'] = self.min_order_create_time
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        o = AlipayUserUgshoppingOrderQueryModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'max_order_create_time' in d:
            o.max_order_create_time = d['max_order_create_time']
        if 'min_order_create_time' in d:
            o.min_order_create_time = d['min_order_create_time']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


