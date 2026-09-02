#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChannelList(object):

    def __init__(self):
        self._new_user_source = None
        self._ou_code = None
        self._sell_channel_code = None
        self._sell_channel_name = None

    @property
    def new_user_source(self):
        return self._new_user_source

    @new_user_source.setter
    def new_user_source(self, value):
        self._new_user_source = value
    @property
    def ou_code(self):
        return self._ou_code

    @ou_code.setter
    def ou_code(self, value):
        self._ou_code = value
    @property
    def sell_channel_code(self):
        return self._sell_channel_code

    @sell_channel_code.setter
    def sell_channel_code(self, value):
        self._sell_channel_code = value
    @property
    def sell_channel_name(self):
        return self._sell_channel_name

    @sell_channel_name.setter
    def sell_channel_name(self, value):
        self._sell_channel_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.new_user_source:
            if hasattr(self.new_user_source, 'to_alipay_dict'):
                params['new_user_source'] = self.new_user_source.to_alipay_dict()
            else:
                params['new_user_source'] = self.new_user_source
        if self.ou_code:
            if hasattr(self.ou_code, 'to_alipay_dict'):
                params['ou_code'] = self.ou_code.to_alipay_dict()
            else:
                params['ou_code'] = self.ou_code
        if self.sell_channel_code:
            if hasattr(self.sell_channel_code, 'to_alipay_dict'):
                params['sell_channel_code'] = self.sell_channel_code.to_alipay_dict()
            else:
                params['sell_channel_code'] = self.sell_channel_code
        if self.sell_channel_name:
            if hasattr(self.sell_channel_name, 'to_alipay_dict'):
                params['sell_channel_name'] = self.sell_channel_name.to_alipay_dict()
            else:
                params['sell_channel_name'] = self.sell_channel_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChannelList()
        if 'new_user_source' in d:
            o.new_user_source = d['new_user_source']
        if 'ou_code' in d:
            o.ou_code = d['ou_code']
        if 'sell_channel_code' in d:
            o.sell_channel_code = d['sell_channel_code']
        if 'sell_channel_name' in d:
            o.sell_channel_name = d['sell_channel_name']
        return o


