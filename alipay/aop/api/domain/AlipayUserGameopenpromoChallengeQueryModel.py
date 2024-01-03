#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserGameopenpromoChallengeQueryModel(object):

    def __init__(self):
        self._open_id = None
        self._query_channel = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def query_channel(self):
        return self._query_channel

    @query_channel.setter
    def query_channel(self, value):
        self._query_channel = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.query_channel:
            if hasattr(self.query_channel, 'to_alipay_dict'):
                params['query_channel'] = self.query_channel.to_alipay_dict()
            else:
                params['query_channel'] = self.query_channel
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
        o = AlipayUserGameopenpromoChallengeQueryModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'query_channel' in d:
            o.query_channel = d['query_channel']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


