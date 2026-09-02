#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExternalItemLabel(object):

    def __init__(self):
        self._label_id = None
        self._label_value = None

    @property
    def label_id(self):
        return self._label_id

    @label_id.setter
    def label_id(self, value):
        self._label_id = value
    @property
    def label_value(self):
        return self._label_value

    @label_value.setter
    def label_value(self, value):
        self._label_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.label_id:
            if hasattr(self.label_id, 'to_alipay_dict'):
                params['label_id'] = self.label_id.to_alipay_dict()
            else:
                params['label_id'] = self.label_id
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
        o = ExternalItemLabel()
        if 'label_id' in d:
            o.label_id = d['label_id']
        if 'label_value' in d:
            o.label_value = d['label_value']
        return o


