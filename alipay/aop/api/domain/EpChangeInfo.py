#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpChangeInfo(object):

    def __init__(self):
        self._change_field_code = None
        self._change_field_desc = None
        self._change_type = None
        self._new_value = None
        self._old_value = None
        self._source = None

    @property
    def change_field_code(self):
        return self._change_field_code

    @change_field_code.setter
    def change_field_code(self, value):
        self._change_field_code = value
    @property
    def change_field_desc(self):
        return self._change_field_desc

    @change_field_desc.setter
    def change_field_desc(self, value):
        self._change_field_desc = value
    @property
    def change_type(self):
        return self._change_type

    @change_type.setter
    def change_type(self, value):
        self._change_type = value
    @property
    def new_value(self):
        return self._new_value

    @new_value.setter
    def new_value(self, value):
        self._new_value = value
    @property
    def old_value(self):
        return self._old_value

    @old_value.setter
    def old_value(self, value):
        self._old_value = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.change_field_code:
            if hasattr(self.change_field_code, 'to_alipay_dict'):
                params['change_field_code'] = self.change_field_code.to_alipay_dict()
            else:
                params['change_field_code'] = self.change_field_code
        if self.change_field_desc:
            if hasattr(self.change_field_desc, 'to_alipay_dict'):
                params['change_field_desc'] = self.change_field_desc.to_alipay_dict()
            else:
                params['change_field_desc'] = self.change_field_desc
        if self.change_type:
            if hasattr(self.change_type, 'to_alipay_dict'):
                params['change_type'] = self.change_type.to_alipay_dict()
            else:
                params['change_type'] = self.change_type
        if self.new_value:
            if hasattr(self.new_value, 'to_alipay_dict'):
                params['new_value'] = self.new_value.to_alipay_dict()
            else:
                params['new_value'] = self.new_value
        if self.old_value:
            if hasattr(self.old_value, 'to_alipay_dict'):
                params['old_value'] = self.old_value.to_alipay_dict()
            else:
                params['old_value'] = self.old_value
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpChangeInfo()
        if 'change_field_code' in d:
            o.change_field_code = d['change_field_code']
        if 'change_field_desc' in d:
            o.change_field_desc = d['change_field_desc']
        if 'change_type' in d:
            o.change_type = d['change_type']
        if 'new_value' in d:
            o.new_value = d['new_value']
        if 'old_value' in d:
            o.old_value = d['old_value']
        if 'source' in d:
            o.source = d['source']
        return o


