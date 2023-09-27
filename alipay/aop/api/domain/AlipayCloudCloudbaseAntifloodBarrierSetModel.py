#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseAntifloodBarrierSetModel(object):

    def __init__(self):
        self._ban_duration = None
        self._biz_app_id = None
        self._biz_env_id = None
        self._request_limit = None
        self._time_window = None

    @property
    def ban_duration(self):
        return self._ban_duration

    @ban_duration.setter
    def ban_duration(self, value):
        self._ban_duration = value
    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def biz_env_id(self):
        return self._biz_env_id

    @biz_env_id.setter
    def biz_env_id(self, value):
        self._biz_env_id = value
    @property
    def request_limit(self):
        return self._request_limit

    @request_limit.setter
    def request_limit(self, value):
        self._request_limit = value
    @property
    def time_window(self):
        return self._time_window

    @time_window.setter
    def time_window(self, value):
        self._time_window = value


    def to_alipay_dict(self):
        params = dict()
        if self.ban_duration:
            if hasattr(self.ban_duration, 'to_alipay_dict'):
                params['ban_duration'] = self.ban_duration.to_alipay_dict()
            else:
                params['ban_duration'] = self.ban_duration
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.biz_env_id:
            if hasattr(self.biz_env_id, 'to_alipay_dict'):
                params['biz_env_id'] = self.biz_env_id.to_alipay_dict()
            else:
                params['biz_env_id'] = self.biz_env_id
        if self.request_limit:
            if hasattr(self.request_limit, 'to_alipay_dict'):
                params['request_limit'] = self.request_limit.to_alipay_dict()
            else:
                params['request_limit'] = self.request_limit
        if self.time_window:
            if hasattr(self.time_window, 'to_alipay_dict'):
                params['time_window'] = self.time_window.to_alipay_dict()
            else:
                params['time_window'] = self.time_window
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseAntifloodBarrierSetModel()
        if 'ban_duration' in d:
            o.ban_duration = d['ban_duration']
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'request_limit' in d:
            o.request_limit = d['request_limit']
        if 'time_window' in d:
            o.time_window = d['time_window']
        return o


