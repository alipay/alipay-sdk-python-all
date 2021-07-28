#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FinAttachment(object):

    def __init__(self):
        self._agreement_code = None
        self._file_path = None
        self._file_suffix = None
        self._name = None
        self._type = None

    @property
    def agreement_code(self):
        return self._agreement_code

    @agreement_code.setter
    def agreement_code(self, value):
        self._agreement_code = value
    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        self._file_path = value
    @property
    def file_suffix(self):
        return self._file_suffix

    @file_suffix.setter
    def file_suffix(self, value):
        self._file_suffix = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_code:
            if hasattr(self.agreement_code, 'to_alipay_dict'):
                params['agreement_code'] = self.agreement_code.to_alipay_dict()
            else:
                params['agreement_code'] = self.agreement_code
        if self.file_path:
            if hasattr(self.file_path, 'to_alipay_dict'):
                params['file_path'] = self.file_path.to_alipay_dict()
            else:
                params['file_path'] = self.file_path
        if self.file_suffix:
            if hasattr(self.file_suffix, 'to_alipay_dict'):
                params['file_suffix'] = self.file_suffix.to_alipay_dict()
            else:
                params['file_suffix'] = self.file_suffix
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FinAttachment()
        if 'agreement_code' in d:
            o.agreement_code = d['agreement_code']
        if 'file_path' in d:
            o.file_path = d['file_path']
        if 'file_suffix' in d:
            o.file_suffix = d['file_suffix']
        if 'name' in d:
            o.name = d['name']
        if 'type' in d:
            o.type = d['type']
        return o


