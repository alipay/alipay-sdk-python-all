#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AIChatCustomerLike(object):

    def __init__(self):
        self._first_chat = None
        self._input_method = None

    @property
    def first_chat(self):
        return self._first_chat

    @first_chat.setter
    def first_chat(self, value):
        self._first_chat = value
    @property
    def input_method(self):
        return self._input_method

    @input_method.setter
    def input_method(self, value):
        self._input_method = value


    def to_alipay_dict(self):
        params = dict()
        if self.first_chat:
            if hasattr(self.first_chat, 'to_alipay_dict'):
                params['first_chat'] = self.first_chat.to_alipay_dict()
            else:
                params['first_chat'] = self.first_chat
        if self.input_method:
            if hasattr(self.input_method, 'to_alipay_dict'):
                params['input_method'] = self.input_method.to_alipay_dict()
            else:
                params['input_method'] = self.input_method
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AIChatCustomerLike()
        if 'first_chat' in d:
            o.first_chat = d['first_chat']
        if 'input_method' in d:
            o.input_method = d['input_method']
        return o


