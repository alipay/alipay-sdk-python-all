#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppMessageTopicUnsubscribeModel(object):

    def __init__(self):
        self._auth_token = None
        self._auth_type = None
        self._tag = None
        self._topic = None

    @property
    def auth_token(self):
        return self._auth_token

    @auth_token.setter
    def auth_token(self, value):
        self._auth_token = value
    @property
    def auth_type(self):
        return self._auth_type

    @auth_type.setter
    def auth_type(self, value):
        self._auth_type = value
    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value
    @property
    def topic(self):
        return self._topic

    @topic.setter
    def topic(self, value):
        self._topic = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_token:
            if hasattr(self.auth_token, 'to_alipay_dict'):
                params['auth_token'] = self.auth_token.to_alipay_dict()
            else:
                params['auth_token'] = self.auth_token
        if self.auth_type:
            if hasattr(self.auth_type, 'to_alipay_dict'):
                params['auth_type'] = self.auth_type.to_alipay_dict()
            else:
                params['auth_type'] = self.auth_type
        if self.tag:
            if hasattr(self.tag, 'to_alipay_dict'):
                params['tag'] = self.tag.to_alipay_dict()
            else:
                params['tag'] = self.tag
        if self.topic:
            if hasattr(self.topic, 'to_alipay_dict'):
                params['topic'] = self.topic.to_alipay_dict()
            else:
                params['topic'] = self.topic
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppMessageTopicUnsubscribeModel()
        if 'auth_token' in d:
            o.auth_token = d['auth_token']
        if 'auth_type' in d:
            o.auth_type = d['auth_type']
        if 'tag' in d:
            o.tag = d['tag']
        if 'topic' in d:
            o.topic = d['topic']
        return o


