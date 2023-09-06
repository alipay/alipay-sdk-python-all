#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PolicyBizData(object):

    def __init__(self):
        self._channel_user_tag = None
        self._entrance = None
        self._source = None

    @property
    def channel_user_tag(self):
        return self._channel_user_tag

    @channel_user_tag.setter
    def channel_user_tag(self, value):
        self._channel_user_tag = value
    @property
    def entrance(self):
        return self._entrance

    @entrance.setter
    def entrance(self, value):
        self._entrance = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_user_tag:
            if hasattr(self.channel_user_tag, 'to_alipay_dict'):
                params['channel_user_tag'] = self.channel_user_tag.to_alipay_dict()
            else:
                params['channel_user_tag'] = self.channel_user_tag
        if self.entrance:
            if hasattr(self.entrance, 'to_alipay_dict'):
                params['entrance'] = self.entrance.to_alipay_dict()
            else:
                params['entrance'] = self.entrance
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PolicyBizData()
        if 'channel_user_tag' in d:
            o.channel_user_tag = d['channel_user_tag']
        if 'entrance' in d:
            o.entrance = d['entrance']
        if 'source' in d:
            o.source = d['source']
        return o


