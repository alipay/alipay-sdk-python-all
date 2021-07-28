#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniContentSyncModel(object):

    def __init__(self):
        self._content_data = None
        self._content_type = None
        self._extend_info = None
        self._operation = None

    @property
    def content_data(self):
        return self._content_data

    @content_data.setter
    def content_data(self, value):
        self._content_data = value
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, value):
        self._operation = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_data:
            if hasattr(self.content_data, 'to_alipay_dict'):
                params['content_data'] = self.content_data.to_alipay_dict()
            else:
                params['content_data'] = self.content_data
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.operation:
            if hasattr(self.operation, 'to_alipay_dict'):
                params['operation'] = self.operation.to_alipay_dict()
            else:
                params['operation'] = self.operation
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniContentSyncModel()
        if 'content_data' in d:
            o.content_data = d['content_data']
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'operation' in d:
            o.operation = d['operation']
        return o


