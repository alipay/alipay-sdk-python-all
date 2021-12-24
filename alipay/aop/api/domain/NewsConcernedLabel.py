#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NewsConcernedLabel(object):

    def __init__(self):
        self._label_code = None
        self._label_name = None
        self._label_show_name = None
        self._label_type = None

    @property
    def label_code(self):
        return self._label_code

    @label_code.setter
    def label_code(self, value):
        self._label_code = value
    @property
    def label_name(self):
        return self._label_name

    @label_name.setter
    def label_name(self, value):
        self._label_name = value
    @property
    def label_show_name(self):
        return self._label_show_name

    @label_show_name.setter
    def label_show_name(self, value):
        self._label_show_name = value
    @property
    def label_type(self):
        return self._label_type

    @label_type.setter
    def label_type(self, value):
        self._label_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.label_code:
            if hasattr(self.label_code, 'to_alipay_dict'):
                params['label_code'] = self.label_code.to_alipay_dict()
            else:
                params['label_code'] = self.label_code
        if self.label_name:
            if hasattr(self.label_name, 'to_alipay_dict'):
                params['label_name'] = self.label_name.to_alipay_dict()
            else:
                params['label_name'] = self.label_name
        if self.label_show_name:
            if hasattr(self.label_show_name, 'to_alipay_dict'):
                params['label_show_name'] = self.label_show_name.to_alipay_dict()
            else:
                params['label_show_name'] = self.label_show_name
        if self.label_type:
            if hasattr(self.label_type, 'to_alipay_dict'):
                params['label_type'] = self.label_type.to_alipay_dict()
            else:
                params['label_type'] = self.label_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NewsConcernedLabel()
        if 'label_code' in d:
            o.label_code = d['label_code']
        if 'label_name' in d:
            o.label_name = d['label_name']
        if 'label_show_name' in d:
            o.label_show_name = d['label_show_name']
        if 'label_type' in d:
            o.label_type = d['label_type']
        return o


