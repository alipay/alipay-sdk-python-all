#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationMobileTagSyncModel(object):

    def __init__(self):
        self._bind_ai = None
        self._bind_replay = None
        self._biz_type = None
        self._has_device = None
        self._mobile_hash = None
        self._province = None

    @property
    def bind_ai(self):
        return self._bind_ai

    @bind_ai.setter
    def bind_ai(self, value):
        self._bind_ai = value
    @property
    def bind_replay(self):
        return self._bind_replay

    @bind_replay.setter
    def bind_replay(self, value):
        self._bind_replay = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def has_device(self):
        return self._has_device

    @has_device.setter
    def has_device(self, value):
        self._has_device = value
    @property
    def mobile_hash(self):
        return self._mobile_hash

    @mobile_hash.setter
    def mobile_hash(self, value):
        self._mobile_hash = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value


    def to_alipay_dict(self):
        params = dict()
        if self.bind_ai:
            if hasattr(self.bind_ai, 'to_alipay_dict'):
                params['bind_ai'] = self.bind_ai.to_alipay_dict()
            else:
                params['bind_ai'] = self.bind_ai
        if self.bind_replay:
            if hasattr(self.bind_replay, 'to_alipay_dict'):
                params['bind_replay'] = self.bind_replay.to_alipay_dict()
            else:
                params['bind_replay'] = self.bind_replay
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.has_device:
            if hasattr(self.has_device, 'to_alipay_dict'):
                params['has_device'] = self.has_device.to_alipay_dict()
            else:
                params['has_device'] = self.has_device
        if self.mobile_hash:
            if hasattr(self.mobile_hash, 'to_alipay_dict'):
                params['mobile_hash'] = self.mobile_hash.to_alipay_dict()
            else:
                params['mobile_hash'] = self.mobile_hash
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationMobileTagSyncModel()
        if 'bind_ai' in d:
            o.bind_ai = d['bind_ai']
        if 'bind_replay' in d:
            o.bind_replay = d['bind_replay']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'has_device' in d:
            o.has_device = d['has_device']
        if 'mobile_hash' in d:
            o.mobile_hash = d['mobile_hash']
        if 'province' in d:
            o.province = d['province']
        return o


