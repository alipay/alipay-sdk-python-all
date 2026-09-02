#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpecifiedSortChannelParam(object):

    def __init__(self):
        self._asset_type_code = None
        self._assigned_channel = None
        self._channel_full_name = None
        self._channel_index = None

    @property
    def asset_type_code(self):
        return self._asset_type_code

    @asset_type_code.setter
    def asset_type_code(self, value):
        self._asset_type_code = value
    @property
    def assigned_channel(self):
        return self._assigned_channel

    @assigned_channel.setter
    def assigned_channel(self, value):
        self._assigned_channel = value
    @property
    def channel_full_name(self):
        return self._channel_full_name

    @channel_full_name.setter
    def channel_full_name(self, value):
        self._channel_full_name = value
    @property
    def channel_index(self):
        return self._channel_index

    @channel_index.setter
    def channel_index(self, value):
        self._channel_index = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_type_code:
            if hasattr(self.asset_type_code, 'to_alipay_dict'):
                params['asset_type_code'] = self.asset_type_code.to_alipay_dict()
            else:
                params['asset_type_code'] = self.asset_type_code
        if self.assigned_channel:
            if hasattr(self.assigned_channel, 'to_alipay_dict'):
                params['assigned_channel'] = self.assigned_channel.to_alipay_dict()
            else:
                params['assigned_channel'] = self.assigned_channel
        if self.channel_full_name:
            if hasattr(self.channel_full_name, 'to_alipay_dict'):
                params['channel_full_name'] = self.channel_full_name.to_alipay_dict()
            else:
                params['channel_full_name'] = self.channel_full_name
        if self.channel_index:
            if hasattr(self.channel_index, 'to_alipay_dict'):
                params['channel_index'] = self.channel_index.to_alipay_dict()
            else:
                params['channel_index'] = self.channel_index
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpecifiedSortChannelParam()
        if 'asset_type_code' in d:
            o.asset_type_code = d['asset_type_code']
        if 'assigned_channel' in d:
            o.assigned_channel = d['assigned_channel']
        if 'channel_full_name' in d:
            o.channel_full_name = d['channel_full_name']
        if 'channel_index' in d:
            o.channel_index = d['channel_index']
        return o


