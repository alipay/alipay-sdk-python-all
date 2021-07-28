#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FsServiceDynamicInfo(object):

    def __init__(self):
        self._content_key = None
        self._content_type = None
        self._content_value = None
        self._end_valid_date = None
        self._start_valid_date = None

    @property
    def content_key(self):
        return self._content_key

    @content_key.setter
    def content_key(self, value):
        self._content_key = value
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def content_value(self):
        return self._content_value

    @content_value.setter
    def content_value(self, value):
        self._content_value = value
    @property
    def end_valid_date(self):
        return self._end_valid_date

    @end_valid_date.setter
    def end_valid_date(self, value):
        self._end_valid_date = value
    @property
    def start_valid_date(self):
        return self._start_valid_date

    @start_valid_date.setter
    def start_valid_date(self, value):
        self._start_valid_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_key:
            if hasattr(self.content_key, 'to_alipay_dict'):
                params['content_key'] = self.content_key.to_alipay_dict()
            else:
                params['content_key'] = self.content_key
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        if self.content_value:
            if hasattr(self.content_value, 'to_alipay_dict'):
                params['content_value'] = self.content_value.to_alipay_dict()
            else:
                params['content_value'] = self.content_value
        if self.end_valid_date:
            if hasattr(self.end_valid_date, 'to_alipay_dict'):
                params['end_valid_date'] = self.end_valid_date.to_alipay_dict()
            else:
                params['end_valid_date'] = self.end_valid_date
        if self.start_valid_date:
            if hasattr(self.start_valid_date, 'to_alipay_dict'):
                params['start_valid_date'] = self.start_valid_date.to_alipay_dict()
            else:
                params['start_valid_date'] = self.start_valid_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FsServiceDynamicInfo()
        if 'content_key' in d:
            o.content_key = d['content_key']
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'content_value' in d:
            o.content_value = d['content_value']
        if 'end_valid_date' in d:
            o.end_valid_date = d['end_valid_date']
        if 'start_valid_date' in d:
            o.start_valid_date = d['start_valid_date']
        return o


