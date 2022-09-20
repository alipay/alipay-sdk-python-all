#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SlmCaseErrorInfo(object):

    def __init__(self):
        self._error_desc = None
        self._error_format = None
        self._error_info = None
        self._error_type = None

    @property
    def error_desc(self):
        return self._error_desc

    @error_desc.setter
    def error_desc(self, value):
        self._error_desc = value
    @property
    def error_format(self):
        return self._error_format

    @error_format.setter
    def error_format(self, value):
        self._error_format = value
    @property
    def error_info(self):
        return self._error_info

    @error_info.setter
    def error_info(self, value):
        self._error_info = value
    @property
    def error_type(self):
        return self._error_type

    @error_type.setter
    def error_type(self, value):
        self._error_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.error_desc:
            if hasattr(self.error_desc, 'to_alipay_dict'):
                params['error_desc'] = self.error_desc.to_alipay_dict()
            else:
                params['error_desc'] = self.error_desc
        if self.error_format:
            if hasattr(self.error_format, 'to_alipay_dict'):
                params['error_format'] = self.error_format.to_alipay_dict()
            else:
                params['error_format'] = self.error_format
        if self.error_info:
            if hasattr(self.error_info, 'to_alipay_dict'):
                params['error_info'] = self.error_info.to_alipay_dict()
            else:
                params['error_info'] = self.error_info
        if self.error_type:
            if hasattr(self.error_type, 'to_alipay_dict'):
                params['error_type'] = self.error_type.to_alipay_dict()
            else:
                params['error_type'] = self.error_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SlmCaseErrorInfo()
        if 'error_desc' in d:
            o.error_desc = d['error_desc']
        if 'error_format' in d:
            o.error_format = d['error_format']
        if 'error_info' in d:
            o.error_info = d['error_info']
        if 'error_type' in d:
            o.error_type = d['error_type']
        return o


