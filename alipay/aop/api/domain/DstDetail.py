#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DstDetail(object):

    def __init__(self):
        self._content = None
        self._intent = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def intent(self):
        return self._intent

    @intent.setter
    def intent(self, value):
        self._intent = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.intent:
            if hasattr(self.intent, 'to_alipay_dict'):
                params['intent'] = self.intent.to_alipay_dict()
            else:
                params['intent'] = self.intent
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DstDetail()
        if 'content' in d:
            o.content = d['content']
        if 'intent' in d:
            o.intent = d['intent']
        return o


