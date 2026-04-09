#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TextLanguageReq(object):

    def __init__(self):
        self._content = None
        self._locale = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def locale(self):
        return self._locale

    @locale.setter
    def locale(self, value):
        self._locale = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.locale:
            if hasattr(self.locale, 'to_alipay_dict'):
                params['locale'] = self.locale.to_alipay_dict()
            else:
                params['locale'] = self.locale
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TextLanguageReq()
        if 'content' in d:
            o.content = d['content']
        if 'locale' in d:
            o.locale = d['locale']
        return o


