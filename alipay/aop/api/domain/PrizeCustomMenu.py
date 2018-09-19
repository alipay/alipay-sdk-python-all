#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrizeCustomMenu(object):

    def __init__(self):
        self._text = None
        self._title = None

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
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
        o = PrizeCustomMenu()
        if 'text' in d:
            o.text = d['text']
        if 'title' in d:
            o.title = d['title']
        return o


