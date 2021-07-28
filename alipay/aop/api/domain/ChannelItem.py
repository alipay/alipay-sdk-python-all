#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChannelItem(object):

    def __init__(self):
        self._asset_id = None
        self._asset_type = None
        self._asset_type_code = None
        self._channel_index = None
        self._inst_id = None
        self._logo = None
        self._name = None
        self._recommend_tip = None

    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        self._asset_type = value
    @property
    def asset_type_code(self):
        return self._asset_type_code

    @asset_type_code.setter
    def asset_type_code(self, value):
        self._asset_type_code = value
    @property
    def channel_index(self):
        return self._channel_index

    @channel_index.setter
    def channel_index(self, value):
        self._channel_index = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def recommend_tip(self):
        return self._recommend_tip

    @recommend_tip.setter
    def recommend_tip(self, value):
        self._recommend_tip = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_id:
            if hasattr(self.asset_id, 'to_alipay_dict'):
                params['asset_id'] = self.asset_id.to_alipay_dict()
            else:
                params['asset_id'] = self.asset_id
        if self.asset_type:
            if hasattr(self.asset_type, 'to_alipay_dict'):
                params['asset_type'] = self.asset_type.to_alipay_dict()
            else:
                params['asset_type'] = self.asset_type
        if self.asset_type_code:
            if hasattr(self.asset_type_code, 'to_alipay_dict'):
                params['asset_type_code'] = self.asset_type_code.to_alipay_dict()
            else:
                params['asset_type_code'] = self.asset_type_code
        if self.channel_index:
            if hasattr(self.channel_index, 'to_alipay_dict'):
                params['channel_index'] = self.channel_index.to_alipay_dict()
            else:
                params['channel_index'] = self.channel_index
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.recommend_tip:
            if hasattr(self.recommend_tip, 'to_alipay_dict'):
                params['recommend_tip'] = self.recommend_tip.to_alipay_dict()
            else:
                params['recommend_tip'] = self.recommend_tip
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChannelItem()
        if 'asset_id' in d:
            o.asset_id = d['asset_id']
        if 'asset_type' in d:
            o.asset_type = d['asset_type']
        if 'asset_type_code' in d:
            o.asset_type_code = d['asset_type_code']
        if 'channel_index' in d:
            o.channel_index = d['channel_index']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'logo' in d:
            o.logo = d['logo']
        if 'name' in d:
            o.name = d['name']
        if 'recommend_tip' in d:
            o.recommend_tip = d['recommend_tip']
        return o


