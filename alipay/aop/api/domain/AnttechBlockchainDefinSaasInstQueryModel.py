#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainDefinSaasInstQueryModel(object):

    def __init__(self):
        self._channel_name = None
        self._platform_member_id = None

    @property
    def channel_name(self):
        return self._channel_name

    @channel_name.setter
    def channel_name(self, value):
        self._channel_name = value
    @property
    def platform_member_id(self):
        return self._platform_member_id

    @platform_member_id.setter
    def platform_member_id(self, value):
        self._platform_member_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_name:
            if hasattr(self.channel_name, 'to_alipay_dict'):
                params['channel_name'] = self.channel_name.to_alipay_dict()
            else:
                params['channel_name'] = self.channel_name
        if self.platform_member_id:
            if hasattr(self.platform_member_id, 'to_alipay_dict'):
                params['platform_member_id'] = self.platform_member_id.to_alipay_dict()
            else:
                params['platform_member_id'] = self.platform_member_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainDefinSaasInstQueryModel()
        if 'channel_name' in d:
            o.channel_name = d['channel_name']
        if 'platform_member_id' in d:
            o.platform_member_id = d['platform_member_id']
        return o


