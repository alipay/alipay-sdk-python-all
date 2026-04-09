#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FindTextRequest(object):

    def __init__(self):
        self._key_list = None
        self._language = None

    @property
    def key_list(self):
        return self._key_list

    @key_list.setter
    def key_list(self, value):
        if isinstance(value, list):
            self._key_list = list()
            for i in value:
                self._key_list.append(i)
    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value


    def to_alipay_dict(self):
        params = dict()
        if self.key_list:
            if isinstance(self.key_list, list):
                for i in range(0, len(self.key_list)):
                    element = self.key_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.key_list[i] = element.to_alipay_dict()
            if hasattr(self.key_list, 'to_alipay_dict'):
                params['key_list'] = self.key_list.to_alipay_dict()
            else:
                params['key_list'] = self.key_list
        if self.language:
            if hasattr(self.language, 'to_alipay_dict'):
                params['language'] = self.language.to_alipay_dict()
            else:
                params['language'] = self.language
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FindTextRequest()
        if 'key_list' in d:
            o.key_list = d['key_list']
        if 'language' in d:
            o.language = d['language']
        return o


