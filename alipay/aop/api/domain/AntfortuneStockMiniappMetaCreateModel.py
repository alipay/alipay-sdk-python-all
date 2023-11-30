#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneStockMiniappMetaCreateModel(object):

    def __init__(self):
        self._ant_app_id = None
        self._channel = None
        self._inst_app_id = None
        self._inst_id = None
        self._secret = None

    @property
    def ant_app_id(self):
        return self._ant_app_id

    @ant_app_id.setter
    def ant_app_id(self, value):
        self._ant_app_id = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def inst_app_id(self):
        return self._inst_app_id

    @inst_app_id.setter
    def inst_app_id(self, value):
        self._inst_app_id = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def secret(self):
        return self._secret

    @secret.setter
    def secret(self, value):
        self._secret = value


    def to_alipay_dict(self):
        params = dict()
        if self.ant_app_id:
            if hasattr(self.ant_app_id, 'to_alipay_dict'):
                params['ant_app_id'] = self.ant_app_id.to_alipay_dict()
            else:
                params['ant_app_id'] = self.ant_app_id
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.inst_app_id:
            if hasattr(self.inst_app_id, 'to_alipay_dict'):
                params['inst_app_id'] = self.inst_app_id.to_alipay_dict()
            else:
                params['inst_app_id'] = self.inst_app_id
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.secret:
            if hasattr(self.secret, 'to_alipay_dict'):
                params['secret'] = self.secret.to_alipay_dict()
            else:
                params['secret'] = self.secret
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneStockMiniappMetaCreateModel()
        if 'ant_app_id' in d:
            o.ant_app_id = d['ant_app_id']
        if 'channel' in d:
            o.channel = d['channel']
        if 'inst_app_id' in d:
            o.inst_app_id = d['inst_app_id']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'secret' in d:
            o.secret = d['secret']
        return o


