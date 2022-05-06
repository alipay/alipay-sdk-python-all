#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GoodsTagResult(object):

    def __init__(self):
        self._tag_code = None
        self._tag_name = None

    @property
    def tag_code(self):
        return self._tag_code

    @tag_code.setter
    def tag_code(self, value):
        self._tag_code = value
    @property
    def tag_name(self):
        return self._tag_name

    @tag_name.setter
    def tag_name(self, value):
        self._tag_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.tag_code:
            if hasattr(self.tag_code, 'to_alipay_dict'):
                params['tag_code'] = self.tag_code.to_alipay_dict()
            else:
                params['tag_code'] = self.tag_code
        if self.tag_name:
            if hasattr(self.tag_name, 'to_alipay_dict'):
                params['tag_name'] = self.tag_name.to_alipay_dict()
            else:
                params['tag_name'] = self.tag_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GoodsTagResult()
        if 'tag_code' in d:
            o.tag_code = d['tag_code']
        if 'tag_name' in d:
            o.tag_name = d['tag_name']
        return o


