#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommonTag(object):

    def __init__(self):
        self._heat_value = None
        self._tag_name = None

    @property
    def heat_value(self):
        return self._heat_value

    @heat_value.setter
    def heat_value(self, value):
        self._heat_value = value
    @property
    def tag_name(self):
        return self._tag_name

    @tag_name.setter
    def tag_name(self, value):
        self._tag_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.heat_value:
            if hasattr(self.heat_value, 'to_alipay_dict'):
                params['heat_value'] = self.heat_value.to_alipay_dict()
            else:
                params['heat_value'] = self.heat_value
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
        o = CommonTag()
        if 'heat_value' in d:
            o.heat_value = d['heat_value']
        if 'tag_name' in d:
            o.tag_name = d['tag_name']
        return o


