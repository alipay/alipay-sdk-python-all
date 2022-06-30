#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GravityParam(object):

    def __init__(self):
        self._content = None
        self._property = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def property(self):
        return self._property

    @property.setter
    def property(self, value):
        self._property = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.property:
            if hasattr(self.property, 'to_alipay_dict'):
                params['property'] = self.property.to_alipay_dict()
            else:
                params['property'] = self.property
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GravityParam()
        if 'content' in d:
            o.content = d['content']
        if 'property' in d:
            o.property = d['property']
        return o


