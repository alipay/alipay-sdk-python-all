#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SupportFunction(object):

    def __init__(self):
        self._card_name = None
        self._card_type = None
        self._function_type = None
        self._goto_url = None

    @property
    def card_name(self):
        return self._card_name

    @card_name.setter
    def card_name(self, value):
        self._card_name = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def function_type(self):
        return self._function_type

    @function_type.setter
    def function_type(self, value):
        if isinstance(value, list):
            self._function_type = list()
            for i in value:
                self._function_type.append(i)
    @property
    def goto_url(self):
        return self._goto_url

    @goto_url.setter
    def goto_url(self, value):
        self._goto_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_name:
            if hasattr(self.card_name, 'to_alipay_dict'):
                params['card_name'] = self.card_name.to_alipay_dict()
            else:
                params['card_name'] = self.card_name
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.function_type:
            if isinstance(self.function_type, list):
                for i in range(0, len(self.function_type)):
                    element = self.function_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.function_type[i] = element.to_alipay_dict()
            if hasattr(self.function_type, 'to_alipay_dict'):
                params['function_type'] = self.function_type.to_alipay_dict()
            else:
                params['function_type'] = self.function_type
        if self.goto_url:
            if hasattr(self.goto_url, 'to_alipay_dict'):
                params['goto_url'] = self.goto_url.to_alipay_dict()
            else:
                params['goto_url'] = self.goto_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SupportFunction()
        if 'card_name' in d:
            o.card_name = d['card_name']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'function_type' in d:
            o.function_type = d['function_type']
        if 'goto_url' in d:
            o.goto_url = d['goto_url']
        return o


