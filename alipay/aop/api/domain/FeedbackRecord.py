#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FeedbackRecord(object):

    def __init__(self):
        self._code = None
        self._name = None
        self._record_type = None
        self._type_list = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def record_type(self):
        return self._record_type

    @record_type.setter
    def record_type(self, value):
        self._record_type = value
    @property
    def type_list(self):
        return self._type_list

    @type_list.setter
    def type_list(self, value):
        self._type_list = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.record_type:
            if hasattr(self.record_type, 'to_alipay_dict'):
                params['record_type'] = self.record_type.to_alipay_dict()
            else:
                params['record_type'] = self.record_type
        if self.type_list:
            if hasattr(self.type_list, 'to_alipay_dict'):
                params['type_list'] = self.type_list.to_alipay_dict()
            else:
                params['type_list'] = self.type_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FeedbackRecord()
        if 'code' in d:
            o.code = d['code']
        if 'name' in d:
            o.name = d['name']
        if 'record_type' in d:
            o.record_type = d['record_type']
        if 'type_list' in d:
            o.type_list = d['type_list']
        return o


