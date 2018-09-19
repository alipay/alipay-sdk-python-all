#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsProdTag(object):

    def __init__(self):
        self._tag_code = None
        self._tag_value = None

    @property
    def tag_code(self):
        return self._tag_code

    @tag_code.setter
    def tag_code(self, value):
        self._tag_code = value
    @property
    def tag_value(self):
        return self._tag_value

    @tag_value.setter
    def tag_value(self, value):
        self._tag_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.tag_code:
            if hasattr(self.tag_code, 'to_alipay_dict'):
                params['tag_code'] = self.tag_code.to_alipay_dict()
            else:
                params['tag_code'] = self.tag_code
        if self.tag_value:
            if hasattr(self.tag_value, 'to_alipay_dict'):
                params['tag_value'] = self.tag_value.to_alipay_dict()
            else:
                params['tag_value'] = self.tag_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsProdTag()
        if 'tag_code' in d:
            o.tag_code = d['tag_code']
        if 'tag_value' in d:
            o.tag_value = d['tag_value']
        return o


