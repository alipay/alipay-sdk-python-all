#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InteligentClauseTerm(object):

    def __init__(self):
        self._descriptions = None
        self._title = None

    @property
    def descriptions(self):
        return self._descriptions

    @descriptions.setter
    def descriptions(self, value):
        if isinstance(value, list):
            self._descriptions = list()
            for i in value:
                self._descriptions.append(i)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.descriptions:
            if isinstance(self.descriptions, list):
                for i in range(0, len(self.descriptions)):
                    element = self.descriptions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.descriptions[i] = element.to_alipay_dict()
            if hasattr(self.descriptions, 'to_alipay_dict'):
                params['descriptions'] = self.descriptions.to_alipay_dict()
            else:
                params['descriptions'] = self.descriptions
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InteligentClauseTerm()
        if 'descriptions' in d:
            o.descriptions = d['descriptions']
        if 'title' in d:
            o.title = d['title']
        return o


