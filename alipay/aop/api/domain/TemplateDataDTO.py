#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateDataDTO(object):

    def __init__(self):
        self._card_data = None
        self._text = None
        self._title = None

    @property
    def card_data(self):
        return self._card_data

    @card_data.setter
    def card_data(self, value):
        self._card_data = value
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
        if self.card_data:
            if hasattr(self.card_data, 'to_alipay_dict'):
                params['card_data'] = self.card_data.to_alipay_dict()
            else:
                params['card_data'] = self.card_data
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
        o = TemplateDataDTO()
        if 'card_data' in d:
            o.card_data = d['card_data']
        if 'text' in d:
            o.text = d['text']
        if 'title' in d:
            o.title = d['title']
        return o


