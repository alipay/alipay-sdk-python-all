#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAuthLoginApplyModel(object):

    def __init__(self):
        self._login_channel = None
        self._sign_from = None
        self._target_url = None

    @property
    def login_channel(self):
        return self._login_channel

    @login_channel.setter
    def login_channel(self, value):
        self._login_channel = value
    @property
    def sign_from(self):
        return self._sign_from

    @sign_from.setter
    def sign_from(self, value):
        self._sign_from = value
    @property
    def target_url(self):
        return self._target_url

    @target_url.setter
    def target_url(self, value):
        self._target_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.login_channel:
            if hasattr(self.login_channel, 'to_alipay_dict'):
                params['login_channel'] = self.login_channel.to_alipay_dict()
            else:
                params['login_channel'] = self.login_channel
        if self.sign_from:
            if hasattr(self.sign_from, 'to_alipay_dict'):
                params['sign_from'] = self.sign_from.to_alipay_dict()
            else:
                params['sign_from'] = self.sign_from
        if self.target_url:
            if hasattr(self.target_url, 'to_alipay_dict'):
                params['target_url'] = self.target_url.to_alipay_dict()
            else:
                params['target_url'] = self.target_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAuthLoginApplyModel()
        if 'login_channel' in d:
            o.login_channel = d['login_channel']
        if 'sign_from' in d:
            o.sign_from = d['sign_from']
        if 'target_url' in d:
            o.target_url = d['target_url']
        return o


