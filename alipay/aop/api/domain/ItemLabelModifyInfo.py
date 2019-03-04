#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemLabelModifyInfo(object):

    def __init__(self):
        self._label_key = None
        self._label_value = None

    @property
    def label_key(self):
        return self._label_key

    @label_key.setter
    def label_key(self, value):
        self._label_key = value
    @property
    def label_value(self):
        return self._label_value

    @label_value.setter
    def label_value(self, value):
        self._label_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.label_key:
            if hasattr(self.label_key, 'to_alipay_dict'):
                params['label_key'] = self.label_key.to_alipay_dict()
            else:
                params['label_key'] = self.label_key
        if self.label_value:
            if hasattr(self.label_value, 'to_alipay_dict'):
                params['label_value'] = self.label_value.to_alipay_dict()
            else:
                params['label_value'] = self.label_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemLabelModifyInfo()
        if 'label_key' in d:
            o.label_key = d['label_key']
        if 'label_value' in d:
            o.label_value = d['label_value']
        return o


