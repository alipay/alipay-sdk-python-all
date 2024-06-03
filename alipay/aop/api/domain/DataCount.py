#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DataCount(object):

    def __init__(self):
        self._highlight_text = None
        self._text = None

    @property
    def highlight_text(self):
        return self._highlight_text

    @highlight_text.setter
    def highlight_text(self, value):
        self._highlight_text = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


    def to_alipay_dict(self):
        params = dict()
        if self.highlight_text:
            if hasattr(self.highlight_text, 'to_alipay_dict'):
                params['highlight_text'] = self.highlight_text.to_alipay_dict()
            else:
                params['highlight_text'] = self.highlight_text
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DataCount()
        if 'highlight_text' in d:
            o.highlight_text = d['highlight_text']
        if 'text' in d:
            o.text = d['text']
        return o


