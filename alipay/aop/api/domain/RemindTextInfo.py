#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RemindTextInfo(object):

    def __init__(self):
        self._has_special_text = None
        self._length = None
        self._start_index = None
        self._text = None

    @property
    def has_special_text(self):
        return self._has_special_text

    @has_special_text.setter
    def has_special_text(self, value):
        self._has_special_text = value
    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value
    @property
    def start_index(self):
        return self._start_index

    @start_index.setter
    def start_index(self, value):
        self._start_index = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


    def to_alipay_dict(self):
        params = dict()
        if self.has_special_text:
            if hasattr(self.has_special_text, 'to_alipay_dict'):
                params['has_special_text'] = self.has_special_text.to_alipay_dict()
            else:
                params['has_special_text'] = self.has_special_text
        if self.length:
            if hasattr(self.length, 'to_alipay_dict'):
                params['length'] = self.length.to_alipay_dict()
            else:
                params['length'] = self.length
        if self.start_index:
            if hasattr(self.start_index, 'to_alipay_dict'):
                params['start_index'] = self.start_index.to_alipay_dict()
            else:
                params['start_index'] = self.start_index
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
        o = RemindTextInfo()
        if 'has_special_text' in d:
            o.has_special_text = d['has_special_text']
        if 'length' in d:
            o.length = d['length']
        if 'start_index' in d:
            o.start_index = d['start_index']
        if 'text' in d:
            o.text = d['text']
        return o


