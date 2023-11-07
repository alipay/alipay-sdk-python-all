#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LegalAIChatHistory(object):

    def __init__(self):
        self._assistant = None
        self._user = None

    @property
    def assistant(self):
        return self._assistant

    @assistant.setter
    def assistant(self, value):
        self._assistant = value
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value


    def to_alipay_dict(self):
        params = dict()
        if self.assistant:
            if hasattr(self.assistant, 'to_alipay_dict'):
                params['assistant'] = self.assistant.to_alipay_dict()
            else:
                params['assistant'] = self.assistant
        if self.user:
            if hasattr(self.user, 'to_alipay_dict'):
                params['user'] = self.user.to_alipay_dict()
            else:
                params['user'] = self.user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LegalAIChatHistory()
        if 'assistant' in d:
            o.assistant = d['assistant']
        if 'user' in d:
            o.user = d['user']
        return o


