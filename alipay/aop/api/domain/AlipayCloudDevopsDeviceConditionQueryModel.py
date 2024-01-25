#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudDevopsDeviceConditionQueryModel(object):

    def __init__(self):
        self._biz_state = None
        self._channel_user_id = None
        self._channel_user_tag = None
        self._platform = None
        self._private_device = None
        self._state = None
        self._vnc = None

    @property
    def biz_state(self):
        return self._biz_state

    @biz_state.setter
    def biz_state(self, value):
        self._biz_state = value
    @property
    def channel_user_id(self):
        return self._channel_user_id

    @channel_user_id.setter
    def channel_user_id(self, value):
        self._channel_user_id = value
    @property
    def channel_user_tag(self):
        return self._channel_user_tag

    @channel_user_tag.setter
    def channel_user_tag(self, value):
        self._channel_user_tag = value
    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):
        self._platform = value
    @property
    def private_device(self):
        return self._private_device

    @private_device.setter
    def private_device(self, value):
        self._private_device = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
    @property
    def vnc(self):
        return self._vnc

    @vnc.setter
    def vnc(self, value):
        self._vnc = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_state:
            if hasattr(self.biz_state, 'to_alipay_dict'):
                params['biz_state'] = self.biz_state.to_alipay_dict()
            else:
                params['biz_state'] = self.biz_state
        if self.channel_user_id:
            if hasattr(self.channel_user_id, 'to_alipay_dict'):
                params['channel_user_id'] = self.channel_user_id.to_alipay_dict()
            else:
                params['channel_user_id'] = self.channel_user_id
        if self.channel_user_tag:
            if hasattr(self.channel_user_tag, 'to_alipay_dict'):
                params['channel_user_tag'] = self.channel_user_tag.to_alipay_dict()
            else:
                params['channel_user_tag'] = self.channel_user_tag
        if self.platform:
            if hasattr(self.platform, 'to_alipay_dict'):
                params['platform'] = self.platform.to_alipay_dict()
            else:
                params['platform'] = self.platform
        if self.private_device:
            if hasattr(self.private_device, 'to_alipay_dict'):
                params['private_device'] = self.private_device.to_alipay_dict()
            else:
                params['private_device'] = self.private_device
        if self.state:
            if hasattr(self.state, 'to_alipay_dict'):
                params['state'] = self.state.to_alipay_dict()
            else:
                params['state'] = self.state
        if self.vnc:
            if hasattr(self.vnc, 'to_alipay_dict'):
                params['vnc'] = self.vnc.to_alipay_dict()
            else:
                params['vnc'] = self.vnc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudDevopsDeviceConditionQueryModel()
        if 'biz_state' in d:
            o.biz_state = d['biz_state']
        if 'channel_user_id' in d:
            o.channel_user_id = d['channel_user_id']
        if 'channel_user_tag' in d:
            o.channel_user_tag = d['channel_user_tag']
        if 'platform' in d:
            o.platform = d['platform']
        if 'private_device' in d:
            o.private_device = d['private_device']
        if 'state' in d:
            o.state = d['state']
        if 'vnc' in d:
            o.vnc = d['vnc']
        return o


