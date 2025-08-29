#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ResumeAttribute(object):

    def __init__(self):
        self._attribute_key = None
        self._attribute_value = None

    @property
    def attribute_key(self):
        return self._attribute_key

    @attribute_key.setter
    def attribute_key(self, value):
        self._attribute_key = value
    @property
    def attribute_value(self):
        return self._attribute_value

    @attribute_value.setter
    def attribute_value(self, value):
        self._attribute_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.attribute_key:
            if hasattr(self.attribute_key, 'to_alipay_dict'):
                params['attribute_key'] = self.attribute_key.to_alipay_dict()
            else:
                params['attribute_key'] = self.attribute_key
        if self.attribute_value:
            if hasattr(self.attribute_value, 'to_alipay_dict'):
                params['attribute_value'] = self.attribute_value.to_alipay_dict()
            else:
                params['attribute_value'] = self.attribute_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ResumeAttribute()
        if 'attribute_key' in d:
            o.attribute_key = d['attribute_key']
        if 'attribute_value' in d:
            o.attribute_value = d['attribute_value']
        return o


