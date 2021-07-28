#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateCreditbankCreditQueryModel(object):

    def __init__(self):
        self._cb_id = None
        self._channel = None
        self._user_id = None

    @property
    def cb_id(self):
        return self._cb_id

    @cb_id.setter
    def cb_id(self, value):
        self._cb_id = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cb_id:
            if hasattr(self.cb_id, 'to_alipay_dict'):
                params['cb_id'] = self.cb_id.to_alipay_dict()
            else:
                params['cb_id'] = self.cb_id
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
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
        o = AlipayCommerceEducateCreditbankCreditQueryModel()
        if 'cb_id' in d:
            o.cb_id = d['cb_id']
        if 'channel' in d:
            o.channel = d['channel']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


