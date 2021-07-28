#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BoxExclusiveKeyword(object):

    def __init__(self):
        self._default_keywords = None
        self._keywords = None

    @property
    def default_keywords(self):
        return self._default_keywords

    @default_keywords.setter
    def default_keywords(self, value):
        if isinstance(value, list):
            self._default_keywords = list()
            for i in value:
                self._default_keywords.append(i)
    @property
    def keywords(self):
        return self._keywords

    @keywords.setter
    def keywords(self, value):
        if isinstance(value, list):
            self._keywords = list()
            for i in value:
                self._keywords.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.default_keywords:
            if isinstance(self.default_keywords, list):
                for i in range(0, len(self.default_keywords)):
                    element = self.default_keywords[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.default_keywords[i] = element.to_alipay_dict()
            if hasattr(self.default_keywords, 'to_alipay_dict'):
                params['default_keywords'] = self.default_keywords.to_alipay_dict()
            else:
                params['default_keywords'] = self.default_keywords
        if self.keywords:
            if isinstance(self.keywords, list):
                for i in range(0, len(self.keywords)):
                    element = self.keywords[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.keywords[i] = element.to_alipay_dict()
            if hasattr(self.keywords, 'to_alipay_dict'):
                params['keywords'] = self.keywords.to_alipay_dict()
            else:
                params['keywords'] = self.keywords
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BoxExclusiveKeyword()
        if 'default_keywords' in d:
            o.default_keywords = d['default_keywords']
        if 'keywords' in d:
            o.keywords = d['keywords']
        return o


