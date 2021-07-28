#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserMemberAlipaybigcardQueryModel(object):

    def __init__(self):
        self._available_cache = None
        self._channel = None
        self._request_time_mills = None
        self._user_id = None

    @property
    def available_cache(self):
        return self._available_cache

    @available_cache.setter
    def available_cache(self, value):
        self._available_cache = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def request_time_mills(self):
        return self._request_time_mills

    @request_time_mills.setter
    def request_time_mills(self, value):
        self._request_time_mills = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_cache:
            if hasattr(self.available_cache, 'to_alipay_dict'):
                params['available_cache'] = self.available_cache.to_alipay_dict()
            else:
                params['available_cache'] = self.available_cache
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.request_time_mills:
            if hasattr(self.request_time_mills, 'to_alipay_dict'):
                params['request_time_mills'] = self.request_time_mills.to_alipay_dict()
            else:
                params['request_time_mills'] = self.request_time_mills
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
        o = AlipayUserMemberAlipaybigcardQueryModel()
        if 'available_cache' in d:
            o.available_cache = d['available_cache']
        if 'channel' in d:
            o.channel = d['channel']
        if 'request_time_mills' in d:
            o.request_time_mills = d['request_time_mills']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


