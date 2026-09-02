#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnswerContent(object):

    def __init__(self):
        self._data_content = None
        self._data_type = None
        self._meta_type = None

    @property
    def data_content(self):
        return self._data_content

    @data_content.setter
    def data_content(self, value):
        self._data_content = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def meta_type(self):
        return self._meta_type

    @meta_type.setter
    def meta_type(self, value):
        self._meta_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_content:
            if hasattr(self.data_content, 'to_alipay_dict'):
                params['data_content'] = self.data_content.to_alipay_dict()
            else:
                params['data_content'] = self.data_content
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.meta_type:
            if hasattr(self.meta_type, 'to_alipay_dict'):
                params['meta_type'] = self.meta_type.to_alipay_dict()
            else:
                params['meta_type'] = self.meta_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnswerContent()
        if 'data_content' in d:
            o.data_content = d['data_content']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'meta_type' in d:
            o.meta_type = d['meta_type']
        return o


