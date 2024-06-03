#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TabFilterTag(object):

    def __init__(self):
        self._id = None
        self._show_type = None
        self._text = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def show_type(self):
        return self._show_type

    @show_type.setter
    def show_type(self, value):
        self._show_type = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.show_type:
            if hasattr(self.show_type, 'to_alipay_dict'):
                params['show_type'] = self.show_type.to_alipay_dict()
            else:
                params['show_type'] = self.show_type
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
        o = TabFilterTag()
        if 'id' in d:
            o.id = d['id']
        if 'show_type' in d:
            o.show_type = d['show_type']
        if 'text' in d:
            o.text = d['text']
        return o


