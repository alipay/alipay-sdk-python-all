#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetChannelInfo(object):

    def __init__(self):
        self._asset_type_code = None
        self._card_type = None
        self._channel = None
        self._channel_code = None
        self._channel_type_code = None
        self._inst_id = None

    @property
    def asset_type_code(self):
        return self._asset_type_code

    @asset_type_code.setter
    def asset_type_code(self, value):
        self._asset_type_code = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def channel_type_code(self):
        return self._channel_type_code

    @channel_type_code.setter
    def channel_type_code(self, value):
        self._channel_type_code = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_type_code:
            if hasattr(self.asset_type_code, 'to_alipay_dict'):
                params['asset_type_code'] = self.asset_type_code.to_alipay_dict()
            else:
                params['asset_type_code'] = self.asset_type_code
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.channel_code:
            if hasattr(self.channel_code, 'to_alipay_dict'):
                params['channel_code'] = self.channel_code.to_alipay_dict()
            else:
                params['channel_code'] = self.channel_code
        if self.channel_type_code:
            if hasattr(self.channel_type_code, 'to_alipay_dict'):
                params['channel_type_code'] = self.channel_type_code.to_alipay_dict()
            else:
                params['channel_type_code'] = self.channel_type_code
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetChannelInfo()
        if 'asset_type_code' in d:
            o.asset_type_code = d['asset_type_code']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'channel' in d:
            o.channel = d['channel']
        if 'channel_code' in d:
            o.channel_code = d['channel_code']
        if 'channel_type_code' in d:
            o.channel_type_code = d['channel_type_code']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        return o


