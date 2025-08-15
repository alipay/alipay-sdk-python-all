#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChatUsage(object):

    def __init__(self):
        self._input_count = None
        self._output_count = None
        self._token_count = None

    @property
    def input_count(self):
        return self._input_count

    @input_count.setter
    def input_count(self, value):
        self._input_count = value
    @property
    def output_count(self):
        return self._output_count

    @output_count.setter
    def output_count(self, value):
        self._output_count = value
    @property
    def token_count(self):
        return self._token_count

    @token_count.setter
    def token_count(self, value):
        self._token_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.input_count:
            if hasattr(self.input_count, 'to_alipay_dict'):
                params['input_count'] = self.input_count.to_alipay_dict()
            else:
                params['input_count'] = self.input_count
        if self.output_count:
            if hasattr(self.output_count, 'to_alipay_dict'):
                params['output_count'] = self.output_count.to_alipay_dict()
            else:
                params['output_count'] = self.output_count
        if self.token_count:
            if hasattr(self.token_count, 'to_alipay_dict'):
                params['token_count'] = self.token_count.to_alipay_dict()
            else:
                params['token_count'] = self.token_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChatUsage()
        if 'input_count' in d:
            o.input_count = d['input_count']
        if 'output_count' in d:
            o.output_count = d['output_count']
        if 'token_count' in d:
            o.token_count = d['token_count']
        return o


